# Lake's Studio

## Design Philosophy

**Zero friction.** The studio should be ready to record at all times. Every piece of outboard gear is permanently wired into the patchbay. Default signal chains for guitar and vocals are normalled and always active. The only thing that ever needs to be plugged in is the instrument itself — guitar into the DI, mic into the input. No setup, no patching, no configuration. Sit down and record.

When an alternative routing is needed (e.g. swapping a compressor), a single front-panel patchbay cable is all it takes — no rewiring behind the rack.

**Everything through the patchbay or Loopback.** No direct cable runs between gear. Every analog connection goes through the patchbay — that's the single point of flexibility. Every digital audio connection between apps goes through Loopback software. This means routing changes happen in one place (front of the patchbay or Loopback config), never behind the rack.

**Automate everything.** Any configuration that can be pushed to hardware programmatically should be. Channel names, routing, snapshots — if it can be scripted, it should be scripted. This eliminates manual entry errors, makes the setup reproducible, and means a full studio reset is one command away. Scripts live in `scripts/`.

## Studio Priorities

1. **Zero latency** — the musician hears everything in real time. The Wing handles all monitoring. Logic's Software Monitoring stays OFF. No plugins in the recording input path.
2. **Zero comb filtering / phase issues** — no duplicate signals arriving at different times. Only one signal path per source. No parallel send/return loops with round-trip delay.
3. **Zero unnecessary noise** — Main 1 trim at 0dB. Outboard returns off main when not tracking. Unused FX bypassed. USB 3 off when not re-amping. No stale channel assignments.

## Studio Goals

The studio is actually two parts: Recording and Mixing

### Recording
Low latency tracking with simple, modular routing. Everything connected to the patchbay. Patchbay stores default configuration through normalled connections, and provides flexibility for alternative routing options. Microphones and DI instruments can patch through any configuration of outboard gear.

**Logic Pro is the primary multi-track recorder.** It records directly from the Wing Rack via USB — unlimited tracks, non-destructive editing, full undo, take comping. Logic also provides virtual studio session players (bass, keyboard, synth, drums) as backing tracks routed into the Wing Rack.

The Wing Rack handles all monitoring with low latency effects. Recording captures the clean outboard chain (gate + EQ/compression + de-esser). Tape saturation is applied in Logic via IK Multimedia T-RackS Tape Machine plugin on every playback track — per-track tape settings, zero latency, zero phase issues.

### Mixing
The Tascam Model 12 is the **analog mixing console**. Logic plays back all tracks through the Wing, the Wing adds FX (amp sims, reverb, outboard), and sends processed stems to the Model 12 for hands-on mixing with real faders, EQ, and compression.

**Why this works:**
- Real faders, real EQ, real compression — not a mouse
- The Model 12's built-in processing adds its own analog character
- Tracks 11/12 automatically capture every mix pass — instant rough bounce
- Takes are handled by Logic. Find a better take? Swap it in Logic, run the mix again.
- A/B different mixes by just moving faders — mixing becomes a performance
- Tape saturation handled by T-RackS in Logic — per-track settings, zero latency, already in the signal before it hits the Wing

### Mastering
This section is still to be determined. However, the WA76-D2 and the HA73-EQX2 can be used for master bus compression and EQ.

## Gear

- Behringer Wing Rack (mixer / effects / monitor controller)
- Samson 48-point TRS patchbay
- HA73-EQX2 (Neve 1073 preamp/EQ clone, dual channel)
- WA76-D2 Black (1176 compressor clone, dual channel)
- Distressor (compressor)
- Audioscape Opto (LA-2A compressor clone)
- Tascam Model 12 (mixing console / DAW controller)
- Mac (Logic Pro, Loopback, wing-sync)

## Software

- Mac OS
- Logic Pro (DAW — primary recorder, session players, mixing)
- Band-in-a-Box (arrangement and songwriting — generates full backing tracks from chord charts)
- Wing Edit (remote Wing control)
- wing-sync (custom BPM sync app, ~/src/wing-sync)
- Loopback (virtual audio routing between Wing Rack and Logic)
- Harrison Mixbus 10

## Plugins

- IK Multimedia MixBox (70+ effect modules — channel strip rack plugin)
- IK Multimedia AmpliTube 5 (guitar/bass amp and effects sim)
- IK Multimedia TONEX (AI tone modeling — amp/cab/pedal capture)
- IK Multimedia T-RackS Tape Machine (Tascam 388 tape emulation)

See `EFFECTS-REFERENCE.md` for a complete catalog of every effect across all hardware and software.

## Configuration

See `studio.edn` for full configuration — all channel assignments, bus layout, matrix routing, USB I/O, patchbay points, FX slots, signal chains, calibration settings, and physical connections.

## Gear Notes

### HA73-EQX2
Neve 1073 clone, dual channel. Transistor preamp with 3-band EQ. Guitar and vocals run through this first, then into the compressors. In mixing, can be used standalone as an EQ. In mastering, dual channels for stereo bus EQ.

### WA76-D2
1176 clone, dual channel FET compressor. DRY/WET knob for parallel compression. In recording, tames transient peaks. In mastering, dual channels for stereo bus compression.

### Distressor
Single-channel compressor. In the default guitar chain (P7-P8, after the WA76 B). Patch via patchbay to use elsewhere or remove from the chain.

### Audioscape Opto
LA-2A clone. Optical compressor. Smooth, musical compression. In the default vocal chain (P3-P4, after the WA76 A). Great for vocals and bass guitar.

### Tascam Model 12
Mixing console and DAW controller. During the mixing phase, operates as a physical control surface for Logic (Mackie Control over USB) or as a standalone analog mixer. 12 channels with EQ, compression, and 2 aux sends. Not used for recording — Logic Pro is the primary recorder.

### Behringer Wing Rack (Creative Uses)
Beyond mixing: snapshots for song recall, built-in FX for sound design, channel strip emulations (Neve, SSL, Vintage), guitar amp sims, OSC automation.
