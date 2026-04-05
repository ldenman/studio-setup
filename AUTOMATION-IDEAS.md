# Automation Ideas

Ideas for studio automation scripts. All use OSC via `oscsend` or Python to communicate with the Wing Rack at 192.168.2.2:2223. Scripts live in `scripts/`.

## Session Setup

### studio-init.sh
Full studio reset. Run once after power-on or when things get out of whack.
- Set all channel names and colors (already built: `set-channel-names.sh`)
- Set default fader levels for all 16 channels
- Assign input sources (ensure ch 1-8 = LCL 1-8, ch 9-16 = LCL 9-16)
- Configure bus assignments (DRY channels to buses for analog outs)
- Reset all EQ, gate, and dynamics to flat/off
- Confirm Wing Rack state matches `studio.edn`

### new-song.sh [song-name] [bpm]
Create a fresh starting point for a new song.
- Save current Wing state as a snapshot
- Create a new Logic Pro project from template
- Set wing-sync BPM
- Load default FX presets (reverb on slot 1, delay on slot 2)
- Set FX delay time to match BPM

### setlist.sh [setlist.txt]
Walk through a setlist for a live recording session.
- Read a text file of song names and BPMs
- Generate a Wing snapshot per song
- Navigate with scene GO/NEXT/PREV via MIDI (Ch9 PC 1-5)
- Each scene recalls the right FX times, fader levels, and EQ settings

## Recording Workflow

### arm-and-record.sh
Synchronized recording across Wing Rack, Model 12, and Logic Pro.
- Verify all Loopback routes are active
- Confirm Model 12 is connected via USB
- Send transport commands to start recording on both the DAW and Model 12

### pre-take-checklist.sh
Run before every take. Catches problems before they become wasted takes.
- Query all channel levels — warn if any DRY channel is clipping or silent
- Verify channel names match config (detect accidental changes)
- Check that wing-sync is running and BPM is locked
- Verify Model 12 tracks 7/8 (synth/piano) and 9/10 (drums) have signal

### take-logger.sh
Keep a log of every take.
- Subscribe to Wing events
- Log timestamp, channel, and parameter for every change
- Write to a session log file alongside the Logic Pro project
- After session, you have a record of every fader move and mute toggle

## Monitoring

### monitor-presets.sh [preset-name]
Instant headphone mix recall.
- `vocals-loud` — boost vocal fader +3dB, dim guitar -3dB
- `guitar-loud` — boost guitar fader +3dB, dim vocals -3dB
- `flat` — all faders to unity
- `playback` — mute all local channels, solo DAW session tracks
- `practice` — mute DAW tracks, solo local channels

### dim-on-stop.sh
Auto-dim monitors when DAW stops.
- Subscribe to Logic Pro transport state via MIDI
- On stop: set main fader to -20dB
- On play: restore main fader to previous level
- Prevents blasting yourself between takes

### reference-toggle.sh
A/B your mix against a reference track.
- Load a reference track into an unused Model 12 channel
- One command toggles: mute your mix, unmute reference (level-matched)
- Run again to toggle back

## FX Management

### fx-presets.sh [preset-name]
Named FX configurations that load in one command.
- `vocal-plate` — Slot 1: plate reverb, 1.2s decay, 20ms pre-delay
- `vocal-hall` — Slot 1: hall reverb, 2.5s decay, 40ms pre-delay
- `guitar-slap` — Slot 2: tape delay, 1/8 note, 30% mix
- `guitar-ambient` — Slot 2: stereo delay + reverb, 1/4 note, 40% mix
- `drums-room` — Slot 3: room reverb, 0.8s decay, 10ms pre-delay
- Each preset stores the model, all parameters, and the mix level

### wet-dry-sweep.sh [fx-slot] [target-mix] [duration-seconds]
Gradually ramp FX mix from current value to target over a duration.
- Useful for building reverb into a chorus or fading delay out of a section
- Sends incremental `/fx/N/fxmix` updates at ~30fps

### bpm-fx-sync.sh [bpm]
Set all time-based FX to musically useful subdivisions.
- Delay slot: 1/4 note = 60000/BPM ms
- Reverb pre-delay: 1/64 note
- Modulation rate: 1/8 note in Hz
- Complements wing-sync for when you want manual one-shot sync

## Outboard Gear

### ab-compare.sh [channel-pair]
Rapid A/B between dry and processed channels.
- Toggle mute on ch 1 (Guitar Dry) and ch 2 (Guitar Processed) every N seconds
- Or toggle ch 3/4 for vocals
- Helps dial in outboard compressor and EQ settings by ear
- Configurable toggle interval (default 2 seconds)

### outboard-bypass.sh [chain]
Software bypass for hardware outboard.
- `guitar` — Mute ch 2 (processed), unmute ch 1 (dry) on the main bus
- `vocal` — Mute ch 4 (processed), unmute ch 3 (dry) on the main bus
- `restore` — Return to normal (processed channels active)
- Effectively bypasses the HA73 + compressor chain without touching cables

## State Management

### backup-state.sh
Dump the full Wing Rack state to a file.
- Query every channel, bus, main, DCA, and FX parameter via OSC
- Save as JSON with timestamp
- Store in `backups/` directory
- Run daily via cron or before major changes

### verify-state.sh
Compare current Wing state against expected config.
- Read `studio.edn`
- Query each channel name, color, input source, and bus assignment
- Report any differences
- Exit with error code if anything is out of spec

### diff-state.sh [file1] [file2]
Compare two backup files to see what changed between sessions.

## DAW Integration

### logic-template-sync.sh
Keep Logic Pro template in sync with Wing Rack config.
- Read channel assignments from `studio.edn`
- Generate a Logic Pro project template with matching track names and colors
- Ensures DAW and mixer always agree

### stem-export-mode.sh
Reconfigure Wing routing for stem export.
- Reassign USB outputs: each bus to its own stereo USB pair
- After export, run `studio-init.sh` to restore recording config

## Utilities

### discover-wing.sh
Find the Wing Rack on the network.
- Parse ARP table or send broadcast OSC
- Return the IP address
- Useful if the Wing IP changes

### color-map.sh
Display the Wing color palette.
- Set channels 1-12 to colors 1-12
- Print the mapping to stdout
- Restore original colors when done

### query-channel.sh [channel]
Quick status check on any channel.
- Query and display: name, color, fader, mute, input source, EQ state, dynamics state
- One-liner for troubleshooting
