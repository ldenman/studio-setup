# Session Guide

What I can help with during a session, how the MCP server enables it, and what's outside my reach.

## Before You Play
- **Board reset and setup** — reset the Wing to a known state, set channel names/colors, verify routing matches RECORDING-CONFIG.md
- **Load a starting template** — "set up for tracking" or "set up for mixing" to get the board ready for the task at hand
- **Tune the room** — set up monitor routing, cue mixes, talkback, headphone feeds before anyone plugs in
- **BPM and sync** — set tempo, calculate delay times, push sync to all time-based FX

## While You're Playing
- **Hands-free mixing** — "turn up the vocals," "mute the drums," "guitar louder" — talk to me instead of reaching for the board
- **Quick A/B** — toggle between dry and processed signals, compare EQ settings, level-match for honest comparisons
- **Dial in sounds** — "get me a vocal sound," "warm up the guitar," "Neve EQ on vocals" — I'll load models and set sensible starting points
- **FX on the fly** — add reverb, delay, modulation without interrupting the flow
- **Monitor adjustments** — change headphone mixes, dim monitors, solo an instrument for a quick check
- **Practice and playback modes** — instantly switch between hearing yourself, hearing the DAW, or both

## Troubleshooting
- **"I'm not hearing anything"** — I'll walk the signal path: mute states, fader levels, input assignments, bus routing, main assign, inserts
- **"Something sounds off"** — check phase, polarity, delay alignment, gain staging, what models are loaded
- **"What changed?"** — diff current board state against the last known config or backup
- **Verify the board** — audit every channel against the expected config and report what's out of place

## Between Takes
- **Tweak the mix** — adjust EQ, compression, FX levels, panning between takes without losing momentum
- **Save snapshots** — capture the current mix state so you can recall it later or compare verse vs chorus settings
- **Swap signal chains** — guide you through patchbay changes for different outboard routing (e.g., Distressor instead of 1176)
- **Reset for another pass** — flatten EQ, remove dynamics, clear FX back to a clean slate

## Production and Arrangement
- **Build FX automation** — swell reverb over 8 bars, fade delay out, crossfade between instruments on a timeline
- **Creative presets** — telephone voice, lo-fi guitar, vintage warmth, shimmer reverb — instant character
- **Parallel processing** — set up parallel compression, blended inserts, wet/dry balances
- **Bus routing** — create subgroups for drums, instruments, or stems with shared processing and glue compression

## Session Management
- **Backup the board** — snapshot full Wing state to a timestamped file
- **Recall a mix** — load a saved snapshot back onto the Wing
- **New song setup** — save current state, set new BPM, sync FX, load defaults
- **Shut it down** — backup, mute everything, pull the main fader to -inf

## Scripting and Automation
- **Write shell scripts** — automate anything repetitive (batch mute, channel setup, FX chains)
- **Real-time automation** — Python scripts that ramp parameters over time for builds and transitions
- **Setlist management** — navigate scenes by song, recall BPM and FX per song

## What the MCP Server Enables

The Wing MCP server (`tools/wing-mcp.py`) gives me three native tools — `wing_get`, `wing_set`, and `wing_node` — that talk directly to the Wing over TCP via `wingctl`. This is what makes me a real assistant engineer instead of a script generator. Here's what it specifically unlocks:

**Read before write** — I can check any parameter before changing it. "Turn up the guitar 3dB" means I read the current fader, do the math, and set the new value. Without MCP, I'd have to guess or ask you what it's at.

**Verify after write** — After setting a value, I can read it back to confirm it took. No more fire-and-forget hoping it worked.

**Intelligent troubleshooting** — When something's wrong, I can walk the signal path myself: read mute states, fader levels, input assignments, bus routing, insert states, and plugin models across every channel. I don't need you to read the screen to me.

**Node discovery** — `wing_node` dumps every parameter under a path. If I don't know what controls something, I can explore it. "What's on channel 5?" gives me the full picture in one call — input source, EQ model, dynamics model, gate model, fader, mute, sends, inserts, everything.

**Conversational mixing** — Because I can read and write in real time, you can talk to me naturally. "Vocals are a bit loud" → I check the fader, drop it 2dB, confirm the new level. The whole loop happens in one exchange.

**State awareness** — I can audit the entire board against expected config, diff what changed between takes, and detect when something drifted from where it should be.

**No shell required for single operations** — MCP tools are native Claude tools, not bash commands. I don't need to spawn a subprocess or write a script to check a fader. This makes simple operations instant and keeps the conversation clean.

**Access to parameters OSC can't reach** — `wingctl` uses the Wing's native TCP protocol (wapi), which exposes paths that the UDP OSC interface doesn't — particularly User Signal routing (`/io/in/USR/N/user/...`) and some deep config nodes.

**What MCP doesn't change:** For batch operations across many channels, I still drop to bash with `oscsend` loops or Python scripts — MCP tools are one-call-at-a-time, so a 16-channel mute is faster as a loop. For real-time automation (fades, ramps, crossfades), I still write Python scripts that run over time. MCP is for interactive, conversational control — the stuff that happens while you're playing.

## What I Can't Do
- **Touch the patchbay** — I can guide you through cable changes, but I can't physically repatch
- **Hear what you hear** — I can read levels and parameters, but I can't listen. You're the ears, I'm the hands on the board.
- **Control the DAW** — Logic Pro isn't in my reach. I handle the Wing and the studio infrastructure around it.
- **Adjust outboard knobs** — the HA73, 1176, Distressor, and Opto are analog. I can route signal to and from them, but the knobs are yours.
