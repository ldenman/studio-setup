#!/usr/bin/env python3
"""
MCP server for studio control — Wing mixer + Logic Pro transport.

Tools:
  wing_get      — Read a Wing parameter
  wing_set      — Set a Wing parameter
  wing_node     — Dump all children of a node
  wing_snapshot — Save complete board state to a JSON file
  wing_restore  — Restore board state from a JSON file
  logic         — Logic Pro transport control (play, stop, record, rewind, ffwd)

Protocol: MCP stdio transport — newline-delimited JSON on stdin/stdout.
"""

import json
import subprocess
import sys
import os
import time
from datetime import datetime

WINGCTL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wingctl")
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAPSHOTS_DIR = os.path.join(PROJECT_DIR, "snapshots")

# Every node path that must be captured for a complete board snapshot.
# Order matters: inputs/outputs before channels so routing context is preserved.
SNAPSHOT_NODES = []

# Input sources — names, colors, gain, phantom, mode
for i in range(1, 17):
    SNAPSHOT_NODES.append(f"/io/in/LCL/{i}")
# User signal routing (virtual patchbay) — 24 slots
for i in range(1, 25):
    SNAPSHOT_NODES.append(f"/io/in/USR/{i}")
# Output routing — where buses/mains physically go
for i in range(1, 9):
    SNAPSHOT_NODES.append(f"/io/out/LCL/{i}")
# USB output routing
for i in range(1, 49):
    SNAPSHOT_NODES.append(f"/io/out/USB/{i}")
# AES output
for i in range(1, 3):
    SNAPSHOT_NODES.append(f"/io/out/AES/{i}")

# Channels 1-40
for i in range(1, 41):
    SNAPSHOT_NODES.append(f"/ch/{i}")
# Aux channels 1-8
for i in range(1, 9):
    SNAPSHOT_NODES.append(f"/aux/{i}")
# Buses 1-16
for i in range(1, 17):
    SNAPSHOT_NODES.append(f"/bus/{i}")
# Mains 1-4
for i in range(1, 5):
    SNAPSHOT_NODES.append(f"/main/{i}")
# Matrix 1-8
for i in range(1, 9):
    SNAPSHOT_NODES.append(f"/mtx/{i}")
# DCAs 1-16
for i in range(1, 17):
    SNAPSHOT_NODES.append(f"/dca/{i}")
# Mute groups 1-8
for i in range(1, 9):
    SNAPSHOT_NODES.append(f"/mgrp/{i}")
# FX slots 1-16
for i in range(1, 17):
    SNAPSHOT_NODES.append(f"/fx/{i}")

# Configuration
SNAPSHOT_NODES.append("/cfg/mon/1")
SNAPSHOT_NODES.append("/cfg/mon/2")
SNAPSHOT_NODES.append("/cfg/solo")
SNAPSHOT_NODES.append("/cfg/talk")
SNAPSHOT_NODES.append("/cfg/osc/1")
SNAPSHOT_NODES.append("/cfg/osc/2")


def parse_node_dump(raw):
    """Parse wingctl node output into a dict of relative_path: value pairs.

    Node dump format uses a dot-prefix convention for nesting:
      .foo.bar.baz=val  — one leading dot: go up one level, then descend foo/bar/baz
      ..foo.bar=val     — two leading dots: go up two levels, then descend foo/bar
      key=val           — no dot: use current prefix as-is
      postins.on=val    — dot within key (no leading dot): expand dots, stay at prefix

    The prefix stack tracks the current nesting depth.
    Keys starting with $ are read-only (skipped during restore).
    """
    params = {}
    if not raw or raw.startswith("error:"):
        return params

    # prefix_stack tracks nesting: ["in", "set"] means current prefix is "in/set/"
    prefix_stack = []

    # Split on comma, respecting quoted strings
    entries = []
    in_quotes = False
    start = 0
    for i, c in enumerate(raw):
        if c == '"':
            in_quotes = not in_quotes
        elif c == ',' and not in_quotes:
            entries.append(raw[start:i])
            start = i + 1
    if start < len(raw):
        entries.append(raw[start:])

    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue

        if entry.startswith('.'):
            # Count leading dots — each dot pops one level from the prefix stack
            dot_count = 0
            while dot_count < len(entry) and entry[dot_count] == '.':
                dot_count += 1
            rest = entry[dot_count:]

            # Pop levels: 1 dot = pop 1 level, 2 dots = pop 2, etc.
            for _ in range(dot_count):
                if prefix_stack:
                    prefix_stack.pop()

            if '=' in rest:
                parts = rest.split('=', 1)
                key_path = parts[0]
                value = parts[1]
                segments = key_path.split('.')
                # Push all but last segment onto stack (they form the new prefix)
                for seg in segments[:-1]:
                    prefix_stack.append(seg)
                # Full key is prefix + last segment
                full_key = '/'.join(prefix_stack + [segments[-1]])
                # Update prefix to include the parent segments
                # (prefix_stack already has them from the push above)
                params[full_key] = value
            else:
                # No value — just a prefix change
                segments = rest.split('.')
                for seg in segments:
                    if seg:
                        prefix_stack.append(seg)

        elif '=' in entry:
            parts = entry.split('=', 1)
            key = parts[0]
            value = parts[1]
            # Handle dots within key names (e.g. postins.on -> postins/on)
            if '.' in key:
                segments = key.split('.')
                # Push parent segments, build full key
                for seg in segments[:-1]:
                    prefix_stack.append(seg)
                full_key = '/'.join(prefix_stack + [segments[-1]])
            else:
                full_key = '/'.join(prefix_stack + [key]) if prefix_stack else key
            params[full_key] = value

    return params


def take_snapshot(name):
    """Dump every node on the Wing and save to a JSON file."""
    os.makedirs(SNAPSHOTS_DIR, exist_ok=True)

    snapshot = {
        "snapshot": name,
        "timestamp": datetime.now().isoformat(),
        "description": f"Complete Wing board state",
        "nodes": {}
    }

    errors = []
    dumped = 0

    for node_path in SNAPSHOT_NODES:
        raw = run_wingctl("node", node_path)
        if raw.startswith("error:"):
            errors.append(f"{node_path}: {raw}")
            continue
        snapshot["nodes"][node_path] = raw
        dumped += 1

    filename = f"{name}.json"
    filepath = os.path.join(SNAPSHOTS_DIR, filename)
    with open(filepath, "w") as f:
        json.dump(snapshot, f, indent=2)

    result = f"Snapshot saved: {filepath}\nNodes captured: {dumped}/{len(SNAPSHOT_NODES)}"
    if errors:
        result += f"\nErrors ({len(errors)}):\n" + "\n".join(errors[:10])
    return result


def build_osc_message(path, value):
    """Build a raw OSC UDP message for a path and value.

    Auto-detects type: int, float, or string.
    Returns bytes ready to send, or None if can't encode.
    """
    import struct

    def osc_string(s):
        """Pad string to 4-byte boundary with null terminators."""
        s = s.encode('utf-8') + b'\x00'
        while len(s) % 4 != 0:
            s += b'\x00'
        return s

    # Determine type and encode
    type_tag = None
    value_bytes = b''

    # Try int first
    try:
        if '.' not in value and value.lstrip('-').isdigit():
            type_tag = 'i'
            value_bytes = struct.pack('>i', int(value))
        else:
            raise ValueError
    except (ValueError, OverflowError):
        pass

    # Try float
    if type_tag is None:
        try:
            f = float(value)
            type_tag = 'f'
            value_bytes = struct.pack('>f', f)
        except ValueError:
            pass

    # Fall back to string
    if type_tag is None:
        type_tag = 's'
        value_bytes = osc_string(value)

    return osc_string(path) + osc_string(',' + type_tag) + value_bytes


def logic_transport(command):
    """Send MCU transport commands to Logic Pro via MIDI.

    Uses 'Logic Pro Virtual In' MIDI port. Logic must have a Mackie Control
    surface configured with input set to 'Logic Pro Virtual In'.
    """
    import rtmidi

    MCU_NOTES = {
        "rewind": 0x5B,
        "ffwd": 0x5C,
        "stop": 0x5D,
        "play": 0x5E,
        "record": 0x5F,
    }

    cmd = command.lower().strip()
    if cmd not in MCU_NOTES:
        return f"error: unknown command '{command}'. Use: play, stop, record, rewind, ffwd"

    note = MCU_NOTES[cmd]

    try:
        midiout = rtmidi.MidiOut()
        ports = midiout.get_ports()

        # Find Logic Pro Virtual In
        port_idx = None
        for i, p in enumerate(ports):
            if "Logic Pro Virtual In" in p:
                port_idx = i
                break

        if port_idx is None:
            return "error: 'Logic Pro Virtual In' MIDI port not found. Is Logic running?"

        midiout.open_port(port_idx)
        midiout.send_message([0x90, note, 0x7F])  # button press
        time.sleep(0.05)
        midiout.send_message([0x90, note, 0x00])  # button release
        midiout.close_port()

        return f"OK — {cmd}"
    except Exception as e:
        return f"error: {e}"


def restore_snapshot(name):
    """Restore board state from a snapshot JSON file.

    Two-pass restore for speed + correctness:
      1. UDP OSC blast — fires all parameters at once (fast, no round-trip)
      2. TCP wingctl pass — sets paths that OSC can't reach (USR routing, etc.)

    The UDP blast handles ~95% of parameters in under a second.
    The TCP pass handles the remaining paths that need wapi.
    """
    import socket
    import time

    filepath = os.path.join(SNAPSHOTS_DIR, f"{name}.json")
    if not os.path.exists(filepath):
        if os.path.exists(name):
            filepath = name
        else:
            return f"error: snapshot not found: {filepath}"

    with open(filepath) as f:
        snapshot = json.load(f)

    nodes = snapshot.get("nodes", {})
    if not nodes:
        return "error: snapshot has no node data"

    wing_ip = os.environ.get("WING_IP", "192.168.2.2")
    wing_port = 2223

    # Paths that need TCP (wapi) because OSC can't reach them or is unreliable
    TCP_PREFIXES = ("/io/in/USR/", "/$CTL/")
    # Path suffixes that need TCP — insert and input assignments don't stick over UDP
    TCP_SUFFIXES = (
        "/preins/ins", "/preins/on",
        "/postins/ins", "/postins/on", "/postins/w", "/postins/mode",
        "/in/conn/grp", "/in/conn/in", "/in/conn/altgrp", "/in/conn/altin",
    )

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Increase send buffer for burst
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 262144)

    udp_count = 0
    tcp_count = 0
    skip_count = 0
    tcp_errors = 0
    tcp_queue = []

    # Restore order: FX first (clear slots), then IO/routing, then channels/buses
    # This prevents FX auto-assign from overriding channel insert settings
    PRIORITY_ORDER = [
        "/fx/",       # Clear FX slots first
        "/io/out/",   # Output routing
        "/io/in/",    # Input sources (LCL names, USR routing handled by TCP)
        "/cfg/",      # Config
        "/dca/",      # DCAs
        "/mgrp/",     # Mute groups
        "/mtx/",      # Matrix
        "/main/",     # Mains
        "/bus/",      # Buses
        "/aux/",      # Aux channels
        "/ch/",       # Channels last (after FX cleared, inserts won't be overridden)
    ]

    def sort_key(node_path):
        for i, prefix in enumerate(PRIORITY_ORDER):
            if node_path.startswith(prefix):
                return i
        return len(PRIORITY_ORDER)

    sorted_nodes = sorted(nodes.items(), key=lambda x: sort_key(x[0]))

    BATCH_SIZE = 50  # Pause every N messages to let the Wing process

    for node_path, raw in sorted_nodes:
        params = parse_node_dump(raw)
        for rel_path, value in params.items():
            # Skip read-only params ($ prefix on any segment)
            # Exception: $solo is writable and must be restored
            segments = rel_path.split('/')
            has_dollar = any(s.startswith('$') for s in segments)
            if has_dollar and not rel_path.endswith('$solo'):
                skip_count += 1
                continue

            full_path = f"{node_path}/{rel_path}"

            # Strip surrounding quotes from string values
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]

            # Route to TCP or UDP
            needs_tcp = (any(full_path.startswith(p) for p in TCP_PREFIXES) or
                         any(full_path.endswith(s) for s in TCP_SUFFIXES))
            if needs_tcp:
                tcp_queue.append((full_path, value))
            else:
                msg = build_osc_message(full_path, value)
                if msg:
                    try:
                        sock.sendto(msg, (wing_ip, wing_port))
                        udp_count += 1
                        # Pace the sends so the Wing can keep up
                        if udp_count % BATCH_SIZE == 0:
                            time.sleep(0.005)
                    except Exception:
                        tcp_queue.append((full_path, value))

    sock.close()

    # Small delay to let UDP settle before TCP pass
    if tcp_queue:
        time.sleep(0.1)

    # TCP pass for paths that need wapi
    for full_path, value in tcp_queue:
        result = run_wingctl("set", full_path, value)
        if result == "OK":
            tcp_count += 1
        else:
            tcp_errors += 1

    total = udp_count + tcp_count
    return (f"Restore complete from: {os.path.basename(filepath)}\n"
            f"Timestamp: {snapshot.get('timestamp', 'unknown')}\n"
            f"Parameters restored: {total} ({udp_count} UDP + {tcp_count} TCP)\n"
            f"Read-only skipped: {skip_count}\n"
            f"TCP errors: {tcp_errors}")


TOOLS = [
    {
        "name": "wing_get",
        "description": "Read a parameter from the Behringer Wing mixer. Returns the current value. Use OSC-style paths like /ch/1/fdr, /ch/5/dyn/mdl, /io/in/USR/1/user/grp. Use this before modifying a value to know the baseline.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "OSC path to the parameter (e.g. /ch/1/fdr, /ch/5/dyn/mdl, /io/in/USR/1/name)"
                },
                "type": {
                    "type": "string",
                    "enum": ["auto", "string", "int", "float"],
                    "description": "Value type. Default 'auto' detects from Wing. Use 'string' for names/models, 'int' for mutes/on-off, 'float' for faders/levels.",
                    "default": "auto"
                }
            },
            "required": ["path"]
        }
    },
    {
        "name": "wing_set",
        "description": "Set a parameter on the Behringer Wing mixer. Use OSC-style paths. Returns OK on success.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "OSC path to the parameter (e.g. /ch/1/fdr, /ch/5/dyn/mdl)"
                },
                "value": {
                    "type": "string",
                    "description": "Value to set. Strings for names/models (e.g. 'LA'), numbers for faders/levels (e.g. '-10.0'), integers for on/off (e.g. '1')"
                }
            },
            "required": ["path", "value"]
        }
    },
    {
        "name": "wing_node",
        "description": "Dump all parameters under a Wing node. Returns a comma-separated list of key=value pairs. Use for troubleshooting, discovering parameters, or checking full channel/source state at once.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "OSC path to the node (e.g. /ch/5, /io/in/USR/1, /fx/1)"
                }
            },
            "required": ["path"]
        }
    },
    {
        "name": "wing_snapshot",
        "description": "Save a complete board snapshot to a JSON file. Captures ALL state: channels 1-40, aux 1-8, buses 1-16, mains 1-4, matrix 1-8, DCAs 1-16, mute groups 1-8, FX 1-16, all input sources (LCL, USR routing), all output routing (LCL, USB, AES), and config (monitor, solo, talkback, oscillator). Saves to snapshots/<name>.json.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Snapshot name (used as filename). e.g. 'blank', 'tracking-setup', 'verse-mix', '2026-03-19_session'"
                }
            },
            "required": ["name"]
        }
    },
    {
        "name": "wing_restore",
        "description": "Restore the Wing board state from a previously saved snapshot JSON file. Pushes every captured parameter back to the Wing, skipping read-only values. Use with caution — this overwrites the current board state.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Snapshot name to restore (without .json extension). e.g. 'blank', 'tracking-setup'"
                }
            },
            "required": ["name"]
        }
    },
    {
        "name": "logic",
        "description": "Control Logic Pro transport via MCU MIDI. Commands: play, stop, record, rewind, ffwd.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "command": {
                    "type": "string",
                    "enum": ["play", "stop", "record", "rewind", "ffwd"],
                    "description": "Transport command to send to Logic Pro"
                }
            },
            "required": ["command"]
        }
    }
]


def run_wingctl(*args):
    try:
        result = subprocess.run(
            [WINGCTL] + list(args),
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"error: {result.stderr.strip()}"
    except subprocess.TimeoutExpired:
        return "error: wingctl timed out"
    except FileNotFoundError:
        return f"error: wingctl not found at {WINGCTL}"


def handle_tool_call(name, arguments):
    if name == "wing_get":
        path = arguments["path"]
        typ = arguments.get("type", "auto")
        cmd = {"auto": "get", "string": "gets", "int": "geti", "float": "getf"}[typ]
        return run_wingctl(cmd, path)

    elif name == "wing_set":
        return run_wingctl("set", arguments["path"], arguments["value"])

    elif name == "wing_node":
        return run_wingctl("node", arguments["path"])

    elif name == "wing_snapshot":
        return take_snapshot(arguments["name"])

    elif name == "wing_restore":
        return restore_snapshot(arguments["name"])

    elif name == "logic":
        return logic_transport(arguments["command"])

    return f"error: unknown tool {name}"


def send(msg):
    """Send a JSON-RPC message as a single line to stdout."""
    line = json.dumps(msg, separators=(",", ":"))
    sys.stdout.write(line + "\n")
    sys.stdout.flush()


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue

        method = msg.get("method", "")
        msg_id = msg.get("id")

        if method == "initialize":
            send({
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": "wing-mcp", "version": "2.0.0"}
                }
            })

        elif method == "notifications/initialized":
            pass

        elif method == "tools/list":
            send({
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {"tools": TOOLS}
            })

        elif method == "tools/call":
            params = msg.get("params", {})
            tool_name = params.get("name", "")
            arguments = params.get("arguments", {})
            result = handle_tool_call(tool_name, arguments)
            send({
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [{"type": "text", "text": result}]
                }
            })

        elif msg_id is not None:
            send({
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32601, "message": f"Unknown method: {method}"}
            })


if __name__ == "__main__":
    main()
