# Command Reference

Quick reference for all mixing commands. When Lake says something in quotes, this is how to execute it.

## Mute, Unmute, and Solo
- "mute guitar" → `/ch/1/mute i 1` and `/ch/2/mute i 1` (always both dry and processed)
- "unmute vocals" → `/ch/3/mute i 0` and `/ch/4/mute i 0`
- "solo vocals" → mute everything except ch3 and ch4
- "mute the DAW" → mute ch9-16
- "mute everything" → mute ch1-16
- "unmute all" → unmute ch1-16

## Fader Levels
- "turn up the guitar" / "guitar louder" → bump ch1 and ch2 faders up ~3dB
- "guitar at -6" → set `/ch/1/fdr f -6.0` and `/ch/2/fdr f -6.0`
- "vocals up 3" → increase ch3 and ch4 faders by 3dB (query current level first, then add)
- "everything to unity" → set all active channel faders to 0.0 dB
- "dim everything" → drop main fader by 20dB

## Pan and Width
- "pan keyboard left" → `/ch/10/pan f -1.0`
- "center the bass" → `/ch/9/pan f 0.0`
- Synth/Piano (ch11-12) and Drums (ch13-14) are stereo pairs — pan L hard left, R hard right

## EQ
- "cut the lows on guitar" → enable EQ on ch1/ch2, cut low shelf
- "roll off below 100 on vocals" → enable low cut filter: `/ch/3/flt/lc i 1`, `/ch/3/flt/lcf f 100.0` (and ch4)
- "brighten the vocals" → boost high shelf on ch3/ch4
- "scoop the mids on guitar" → cut a mid band on ch1/ch2
- "flat EQ on everything" → disable EQ on all channels: `/ch/N/eq/on i 0`
- Use sensible defaults: gentle 3dB boosts/cuts, musical Q values (1.0-2.0)

### EQ Plugin Models
The Wing's EQ engine can be swapped for emulations via `/ch/N/eq/mdl`:
- "Neve EQ on guitar" → `/ch/2/eq/mdl s "E84"` (Neve 1084 — 3 fixed-freq bands, gain/trim)
- "Neve 1088 EQ" → `/ch/N/eq/mdl s "E88"` (Neve 1088 Formant — 4-band with bell/shelf select)
- "SSL EQ" → `/ch/N/eq/mdl s "SOUL"` (SSL 4000 Analogue — lf/lm/hm/hf)
- "Focusrite EQ" → `/ch/N/eq/mdl s "F110"` (Focusrite ISA 110 — parametric + shelves)
- "Pultec EQ" → `/ch/N/eq/mdl s "PULSAR"` (Pultec EQP-1A/MEQ-5 — boost/atten with fixed freqs)
- "Massive Passive" → `/ch/N/eq/mdl s "MACH4"` (Manley Massive Passive — sub/40/160/650/2k5/air)
- "back to standard" → `/ch/N/eq/mdl s "STD"`
- All EQ plugins have a mix control for parallel EQ: `/ch/N/eq/mix` (0-125%)

### Filters (High Pass / Low Cut)
- "high pass vocals at 80" → `/ch/3/flt/lc i 1`, `/ch/3/flt/lcf f 80.0` (and ch4)
- "low pass guitar at 8k" → `/ch/1/flt/hc i 1`, `/ch/1/flt/hcf f 8000.0` (and ch2)
- "remove the filter on vocals" → `/ch/3/flt/lc i 0`, `/ch/3/flt/hc i 0` (and ch4)
- "tilt filter" → `/ch/N/flt/mdl s "TILT"`, `/ch/N/flt/tf i 1` — tilts entire spectrum bright/dark
- "all-pass filter at 1kHz" → `/ch/N/flt/mdl s "AP1"`, set freq — for phase alignment tricks

## Dynamics (Wing's Built-in Compressor)
- "compress the vocals" → enable dynamics on ch3/ch4 with gentle settings (threshold -20, ratio 3:1, auto makeup)
- "heavier compression on guitar" → lower threshold, higher ratio
- "remove compression" → `/ch/N/dyn/on i 0`
- Note: this is the Wing's digital compressor, separate from the outboard 1176/Opto chain

### Dynamics Plugin Models
The Wing's compressor can be swapped for emulations of classic hardware via `/ch/N/dyn/mdl`:
- "use the 1176 on vocals" → `/ch/3/dyn/mdl s "76LA"` (UREI 1176 — in, out, att, rel, ratio [4/8/12/20/ALL])
- "use the LA2A on vocals" → `/ch/3/dyn/mdl s "LA"` (LA-2A — gain, peak, comp/lim mode)
- "use the SSL comp on vocals" → `/ch/3/dyn/mdl s "9000C"` (SSL 9000 channel comp)
- "use the Fairchild" → `/ch/N/dyn/mdl s "F670"` (Fairchild 670 — in, thr, time, bias)
- "use the Distressor" → `/ch/N/dyn/mdl s "NSTR"` (Empirical Labs Distressor)
- "use the DBX" → `/ch/N/dyn/mdl s "B160"` (DBX 160)
- "bus glue comp" → `/bus/N/dyn/mdl s "SBUS"` (SSL G Bus Compressor — thr, ratio, att, rel)
- "Neve comp" → `/ch/N/dyn/mdl s "ECL33"` (Neve 33609 — separate comp + limiter sections)
- "back to standard" → `/ch/N/dyn/mdl s "COMP"`
- All models have mix control for parallel compression: `/ch/N/dyn/mix`

## Gate
- "gate the drums" → enable gate on ch13/ch14 with sensible threshold
- "remove the gate" → `/ch/N/gate/on i 0`

### Gate Plugin Models
The gate section can also be swapped for different processors via `/ch/N/gate/mdl`:
- "de-ess the vocals" → `/ch/3/gate/mdl s "DS902"` (DBX 902 DeEsser — freq, range, mode)
- "use the Neve gate" → `/ch/N/gate/mdl s "E88"` (Neve 1088 gate — thr, hyst, range, rel, fast)
- "SSL gate" → `/ch/N/gate/mdl s "9000G"` (SSL 9000 gate — thr, range, hold, rel, fast, gate/exp mode)
- "transient shaper" → `/ch/N/gate/mdl s "WAVE"` (SPL Wave Designer — attack, sustain, gain)
- "warmth/saturation" → `/ch/N/gate/mdl s "WARM"` (Soul Warmth Preamp — drive, harmonics, color, trim)
- "auto level" → `/ch/N/gate/mdl s "RIDE"` (Auto Rider — threshold, target, speed, ratio)
- "ducker" → `/ch/N/gate/mdl s "DUCK"` (Ducker — thr, range, att, hold, rel)
- "dynamic EQ" → `/ch/N/gate/mdl s "DEQ"` (threshold, ratio, filter, freq, Q)
- "back to standard gate" → `/ch/N/gate/mdl s "GATE"`

## Outboard Bypass
- "bypass the outboard on guitar" → mute ch2, route ch1 to main bus
- "bypass the outboard on vocals" → mute ch4, route ch3 to main bus
- "restore outboard" → unmute processed channels, re-route as normal

## FX (Reverb, Delay, Modulation)
- "give me a plate reverb on vocals" → load model into an FX slot, set send from ch3/ch4, sensible defaults (1.2s decay, 20ms pre-delay)
- "hall reverb on vocals" → load hall model, 2.5s decay, 40ms pre-delay
- "slap delay on guitar" → load tape delay, 1/8 note time, 30% mix
- "ambient guitar" → stereo delay + reverb, 1/4 note, 40% mix
- "room verb on drums" → room reverb on ch13/ch14 send, 0.8s decay
- "kill the reverb" → set FX mix to 0 or mute the send
- "more reverb" / "less delay" → adjust FX mix level up or down
- "wet/dry at 30%" → `/fx/N/fxmix f 30.0` (0-100 scale)
- Use slots 1-8 (premium) for reverbs/delays. Slots 9-16 (standard) for utilities, EQ, amps, channel strips.
- Query what's loaded before overwriting: read `/fx/N/mdl`
- Query `/fx/N` node to discover all available parameters for a loaded effect

**FX via bus pre-insert (current studio pattern):**
FX are loaded as pre-inserts on buses, not as standalone send/return slots. To route a channel's signal through an FX bus:
1. Load the FX model on the bus pre-insert: `/bus/N/preins/ins s "FX2"`, `/bus/N/preins/on i 1`
2. Enable the send from the source bus/channel: `/bus/1/send/3/on i 1`, `/bus/1/send/3/lvl f 0.0`
3. **Assign the FX bus to main** (easy to forget): `/bus/3/main/1/on i 1`

Current setup: Bus 3 has FX2 (plate reverb) on its pre-insert. Bus 1 (vocal) and Bus 2 (guitar) send to Bus 3 for shared reverb.

### Premium FX Models (slots 1-8)
Reverbs: HALL, ROOM, CHAMBER, PLATE, CONCERT, AMBI, V-ROOM (VSS3), V-REV, V-PLATE, GATED, REVERSE, SHIMMER, SPRING
Delays: ST-DL, TAP-DL, TAPE-DL, OILCAN, BBD-DL, DEL/REV
Modulation: DIMCRS (Dimension), CHORUS, FLANGER
Pitch: PITCH, D-PITCH

### Standard FX Models (slots 9-16, also work in 1-8)
Utilities: GEQ, PIA (560 GEQ), C5-CMB (5-band multiband comp), LIMITER, DE-S2, ENHANCE, EXCITER, P-BASS, BODY, SUB, PCORR (Pitch Fix), DOUBLE (Vocal Doubler)
Modulation: PHASER, PANNER, MOOD (Mood Filter), ROTARY, TAPE (Tape Machine)
Amps: RACKAMP, UKROCK, ANGEL, JAZZC, DELUXE
EQ (as FX): SOUL, E88, E84, F110, PULSAR, MACH4
Channel Strips: \*EVEN\* (Neve), \*SOUL\* (SSL), \*VINTAGE\*, \*BUS\*, \*MASTER\*

## BPM and Tempo Sync
- "set BPM to 120" → calculate delay times and push to all time-based FX slots:
  - 1/4 note = 60000/BPM ms (500ms at 120)
  - 1/8 note = 30000/BPM ms (250ms at 120)
  - Dotted 1/8 = 45000/BPM ms (375ms at 120)
  - 1/16 note = 15000/BPM ms (125ms at 120)
  - Modulation rate: (BPM/60)/subdivision Hz
- Also update wing-sync if running

## Input Trim and Polarity
- "add some trim to guitar" → increase `/ch/1/in/set/trim` by a few dB
- "trim guitar to +6" → `/ch/1/in/set/trim f 6.0`
- "flip polarity on vocal" → `/ch/3/in/set/inv i 1`

## Monitoring Modes
- "practice mode" → mute DAW channels (ch9-16), unmute local channels (ch1-4)
- "playback mode" → mute local channels (ch1-4), unmute DAW channels (ch9-16)
- "full mix" → unmute everything
- "vocals only" → mute everything except ch3/ch4

## A/B Comparison
- "compare dry vs processed guitar" → alternate muting ch1 and ch2 on a timer (every 2s)
- "compare dry vs processed vocals" → same for ch3 and ch4
- "stop comparing" → restore both channels to previous state

### A/B Testing Hardware vs Plugin (e.g., Opto vs Wing LA-2A)

The key challenge: both paths must receive the **same clean source** and be **level matched**. If the plugin is on the source channel, it colors the signal feeding the hardware too.

**Setup (using bass → Opto as example):**
1. **Source channel (Ch9)**: receives USB/9 (bass). Dynamics OFF. Sends to Bus 1 pre-fader for hardware path. NOT assigned to main.
2. **Hardware return (Ch17)**: receives from outboard chain via Bus 1 → Out 1 → patchbay → outboard → LCL/17. Assigned to main.
3. **Plugin channel (Ch19)**: receives same USB/9 source directly (`/ch/19/in/conn/grp s "USB"`, `/ch/19/in/conn/in i 9`). Wing LA-2A enabled (`/ch/19/dyn/mdl s "LA"`, `/ch/19/dyn/on i 1`). Assigned to main.
4. **Kill crosstalk**: turn off Bus 1 → Bus 3 send so bass doesn't leak through the reverb bus to main.

**Why not use USR routing?** USR works but gives you less control. Having both Ch9 and Ch19 on USB/9 directly means independent trim/gain on each.

**Why not put the plugin on Ch9?** The pre-fader send tap (`ptap`) is after dynamics processing on the Wing. Any plugin on Ch9 colors the signal going to the hardware — not a fair test.

**Level matching:**
- Use `wingctl meter all` to read output levels on both channels
- Adjust faders until outputs are within 0.5dB
- Re-check multiple times — dynamic material fluctuates
- Louder always sounds "better" so this step is critical

**A/B by soloing:** Solo Ch17 for hardware, solo Ch19 for plugin. Requires monitor section routed through MX1 (see Monitor Section docs) so solo works through speakers.

**Blind test:** Use a Python script to randomly solo one channel, save the answer to a file, then check after guessing.

## DCA Groups (/dca/N/...)
8 DCAs available for group volume control without affecting processing.
- "set up DCA 1 for all instruments" → `/dca/1/name s "Instruments"`, `/dca/1/col i 9` (red), assign ch1-4
- "set up DCA 2 for DAW tracks" → `/dca/2/name s "DAW"`, `/dca/2/col i 5` (green), assign ch9-16
- "DCA 1 down 3dB" → adjust `/dca/1/fdr` — all assigned channels move together
- "mute DCA 2" → `/dca/2/mute i 1` — mutes all assigned channels
- DCAs control volume only — no EQ, dynamics, or processing. Signal flows through the original channel.

## Channel Status / Troubleshooting
- "what's the guitar fader at?" → query `/ch/1/fdr` and report
- "is anything muted?" → query mute state on all channels, report which are muted
- "check levels" → query fader positions on all active channels
- "what FX are loaded?" → query `/fx/N/mdl` on all slots, report what's active
- "verify the board" → compare current Wing state against expected config from `studio.edn`

## Session Management
- "reset the board" → run `scripts/set-channel-names.sh` and restore all defaults (names, colors, faders, EQ flat, FX off)
- "back it up" → query full Wing state via Python and save to `backups/` with timestamp
- "new song at 95 BPM" → save current state, set BPM, sync FX times, load default FX presets

## Writing Scripts
- When Lake asks to automate something → write a shell script in `scripts/`, make it executable, using `oscsend` for simple tasks or Python with raw UDP for anything that needs to read values back

## Batch Operations
Apply the same change across multiple channels efficiently.
- "high pass everything at 60Hz" → loop through all active channels, enable low cut at 60Hz
- "reset all EQ" → disable EQ on ch1-16: loop `/ch/N/eq/on i 0`
- "unmute all sends to bus 3" → loop through channels enabling bus 3 sends
- "all DAW channels to -6" → set faders on ch9-16 to -6.0
- Use bash loops: `for i in $(seq 1 16); do oscsend 192.168.2.2 2223 /ch/$i/eq/on i 0; done`
- **Node batch commands** (Python only): set multiple params in one OSC message using dot notation:
  - `/ ,s /ch.1.fdr=-10,mute=0,.2.fdr=-6,mute=0` — set ch1 and ch2 faders and mutes in one packet
  - Wing replies `/* ,s OK` on success or error string on failure
