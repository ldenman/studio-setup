# Plan: Move Tape Emulation to Recording-Only Path

## Context

Tape emulation (TAPE FX) is currently on channel pre-inserts (Ch1=FX9, Ch2=FX10, Ch6=FX3). Pre-inserts sit before everything in the signal chain, so both the outboard bus sends AND dry recordings get tape color. This is backwards from how a real studio works — in a real studio, signal goes Mic → Preamp → Outboard → Tape. The tape machine is the destination, not an effect before the console send.

The goal is tape ONLY on the dry recordings going to the Model 12, so each layer accumulates tape saturation like a real tape machine bouncing tracks. The outboard chain (HA73, 1176, Distressor, Opto) should receive clean signal.

## Approach: Dedicated Recording Buses

Move TAPE from channel pre-inserts to dedicated recording buses. Channels send clean signal to outboard (existing Bus 1/5/6) and separately to new recording buses (Bus 7/8/9) that have TAPE on their pre-inserts. USR outputs source from these recording buses instead of from channels.

### New Bus Layout

| Bus | Name       | Color  | Pre-insert | Receives from      | Purpose                    |
|-----|------------|--------|------------|---------------------|----------------------------|
| 7   | Vocal Rec  | Blue   | FX9 (TAPE) | Ch1 pre-fader send | Tape-colored vocal for dry recording |
| 8   | Guitar Rec | Red    | FX10 (TAPE)| Ch2 pre-fader send | Tape-colored guitar for dry recording |
| 9   | Mic Rec    | Yellow | FX3 (TAPE) | Ch6 pre-fader send | Tape-colored mic for dry recording |

Recording buses: NOT assigned to main, faders at unity, unmuted.

### Updated USR Routing

| USR | Name       | Old Source    | New Source   | Tap | Purpose                    |
|-----|------------|---------------|--------------|-----|----------------------------|
| 1   | Vocal Dry  | grp=CH, in=1  | grp=BUS, in=13 | PRE | Vocal dry recording via USB 1 |
| 2   | Guitar Dry | grp=CH, in=2  | grp=BUS, in=15 | PRE | Guitar dry recording via USB 2 |
| 6   | Mic Dry L  | grp=CH, in=6, lr=L | grp=BUS, in=17, lr=L | PRE | Condenser L via USB 15 |
| 7   | Mic Dry R  | grp=CH, in=6, lr=R | grp=BUS, in=17, lr=R | PRE | Condenser R via USB 16 |

Bus stereo indexing: `in = (bus_number - 1) * 2 + 1` for L. Bus 7L=13, Bus 8L=15, Bus 9L=17.

### Updated Signal Chains

**Vocal (after change):**
- Mic → Ch1 (preamp) → Bus 1 send (pre-fader, **clean**) → outboard chain → Ch17
- Mic → Ch1 (preamp) → Bus 7 send (pre-fader) → FX9/TAPE (Bus 7 pre-insert) → USR/1 → USB 1 → Model 12

**Guitar (after change):**
- DI → Ch2 (preamp) → Bus 5/6 send (pre-fader, **clean**) → amp sim → Bus 2 → outboard → Ch18
- DI → Ch2 (preamp) → Bus 8 send (pre-fader) → FX10/TAPE (Bus 8 pre-insert) → USR/2 → USB 2 → Model 12

**Condensers (after change):**
- Mics → Ch6 → Bus 6 send (pre-fader, **clean**) → RACKAMP → Bus 2 → outboard → Ch18
- Mics → Ch6 → Bus 9 send (pre-fader) → FX3/TAPE (Bus 9 pre-insert) → USR/6+7 → USB 15/16 → Model 12

## Implementation Steps

### 1. Wing Routing Changes (via wing_set / oscsend)

**a. Remove TAPE from channel pre-inserts:**
```
/ch/1/preins/ins s "NONE"    # was FX9
/ch/1/preins/on i 0
/ch/2/preins/ins s "NONE"    # was FX10
/ch/2/preins/on i 0
/ch/6/preins/ins s "NONE"    # was FX3
/ch/6/preins/on i 0
```

**b. Set up recording buses (Bus 7, 8, 9):**
```
# Bus 7 - Vocal Rec
/bus/7/name s "Vocal Rec"
/bus/7/col i 2               # Blue
/bus/7/preins/ins s "FX9"    # TAPE
/bus/7/preins/on i 1
/bus/7/fdr f 0.0             # Unity
/bus/7/mute i 0              # Unmuted
/bus/7/main/1/on i 0         # NOT on main

# Bus 8 - Guitar Rec
/bus/8/name s "Guitar Rec"
/bus/8/col i 9               # Red
/bus/8/preins/ins s "FX10"   # TAPE
/bus/8/preins/on i 1
/bus/8/fdr f 0.0
/bus/8/mute i 0
/bus/8/main/1/on i 0

# Bus 9 - Mic Rec
/bus/9/name s "Mic Rec"
/bus/9/col i 7               # Yellow
/bus/9/preins/ins s "FX3"    # TAPE
/bus/9/preins/on i 1
/bus/9/fdr f 0.0
/bus/9/mute i 0
/bus/9/main/1/on i 0
```

**c. Add channel sends to recording buses:**
```
# Ch1 → Bus 7 (vocal recording)
/ch/1/send/7/on i 1
/ch/1/send/7/lvl f 0.0
/ch/1/send/7/mode s "PRE"

# Ch2 → Bus 8 (guitar recording)
/ch/2/send/8/on i 1
/ch/2/send/8/lvl f 0.0
/ch/2/send/8/mode s "PRE"

# Ch6 → Bus 9 (mic recording)
/ch/6/send/9/on i 1
/ch/6/send/9/lvl f 0.0
/ch/6/send/9/mode s "PRE"
```

**d. Reroute USR outputs to recording buses:**
```
# USR/1 - Vocal Dry (was CH/1, now BUS/7)
/io/in/USR/1/user/grp s "BUS"
/io/in/USR/1/user/in i 13       # Bus 7L index
/io/in/USR/1/user/tap s "PRE"

# USR/2 - Guitar Dry (was CH/2, now BUS/8)
/io/in/USR/2/user/grp s "BUS"
/io/in/USR/2/user/in i 15       # Bus 8L index
/io/in/USR/2/user/tap s "PRE"

# USR/6 - Mic Dry L (was CH/6 L, now BUS/9 L)
/io/in/USR/6/user/grp s "BUS"
/io/in/USR/6/user/in i 17       # Bus 9L index
/io/in/USR/6/user/tap s "PRE"
/io/in/USR/6/user/lr s "L"

# USR/7 - Mic Dry R (was CH/6 R, now BUS/9 R)
/io/in/USR/7/user/grp s "BUS"
/io/in/USR/7/user/in i 17       # Bus 9L index (same bus, R channel)
/io/in/USR/7/user/tap s "PRE"
/io/in/USR/7/user/lr s "R"
```

### 2. Documentation Updates

**CLAUDE.md — sections to update:**
- **Bus Layout table** (~line 33): Add Bus 7/8/9 entries
- **USR Routing table** (~line 48): Change source from CH to BUS for USR 1, 2, 6, 7
- **Signal Chains - Vocal** (~line 96): Remove TAPE from chain, note tape is on recording bus
- **Signal Chains - Guitar** (~line 106): Same
- **Signal Chains - Condenser mic routing** (~line 134): Same
- **Tape pre-inserts section** (~line 140): Rewrite — tape is now on Bus 7/8/9 pre-inserts, not channel pre-inserts
- **Tape Emulation section** (~line 143): Rewrite to reflect new routing and rationale
- **Recording Workflow** (~line 69): Update "The Wing handles" to reflect tape on recording buses
- **USB Output Routing note** (~line 67): Update "Dry recordings include tape emulation" sentence

**RECORDING-CONFIG.md — sections to update:**
- **Bus Layout table** (line 108): Add Bus 7/8/9 rows
- **USR Routing table** (line 39): Update sources
- **Wing FX Pre-Insert Assignments table** (line 123): Move FX9/FX10/FX3 from channels to buses
- **Signal Chains** (line 135): Remove TAPE from channel chains, note recording bus path

### 3. Script Updates

**scripts/set-channel-names.sh** — Add bus naming:
```bash
# Recording buses (tape machine path)
oscsend "$WING_IP" "$WING_PORT" /bus/7/name s "Vocal Rec"
oscsend "$WING_IP" "$WING_PORT" /bus/7/col i 2
oscsend "$WING_IP" "$WING_PORT" /bus/8/name s "Guitar Rec"
oscsend "$WING_IP" "$WING_PORT" /bus/8/col i 9
oscsend "$WING_IP" "$WING_PORT" /bus/9/name s "Mic Rec"
oscsend "$WING_IP" "$WING_PORT" /bus/9/col i 7
```

**New script: scripts/setup-recording-buses.sh** — Full recording bus setup (buses, sends, USR routing, clear channel pre-inserts). Idempotent.

### 4. Verification

After applying Wing changes:
1. `wing_node /ch/1` — confirm no pre-insert
2. `wing_node /ch/2` — confirm no pre-insert
3. `wing_node /ch/6` — confirm no pre-insert
4. `wing_node /bus/7` — confirm TAPE pre-insert, fader 0, not on main
5. `wing_node /bus/8` — same
6. `wing_node /bus/9` — same
7. `wing_node /io/in/USR/1` — confirm grp=BUS, in=13
8. `wing_node /io/in/USR/2` — confirm grp=BUS, in=15
9. `wing_node /io/in/USR/6` — confirm grp=BUS, in=17, lr=L
10. `wing_node /io/in/USR/7` — confirm grp=BUS, in=17, lr=R
11. Play signal through Ch1/Ch2 and verify outboard return on Ch17/Ch18 sounds clean (no tape color)
12. Check USB 1/2 recordings include tape saturation

## Notes

- USR/5 (Gtr Acoustic DI) is unchanged — it's a monitoring path, not a recording path
- No new FX slots consumed — FX3, FX9, FX10 just move from channels to buses
- Muting a source channel still kills the recording bus send (Wing behavior: mute kills pre-fader sends)
- Channel dynamics (gate/EQ/comp) are still baked into recordings — pre-fader bus sends tap after dynamics
- FX slot reassignment: assigning FX9 to Bus 7 should auto-remove it from Ch1, but verify and explicitly clear if needed
