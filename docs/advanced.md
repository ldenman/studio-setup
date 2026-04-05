# Advanced Capabilities

## Parallel Compression
Blend dry and compressed signals using the Wing's dynamics mix control — no extra routing needed.
- "parallel compress the vocals" → enable dynamics on ch3/ch4, set ratio high (8:1+), threshold low, then blend with `/ch/N/dyn/mix f 0.3` (30% wet keeps punch while adding density)
- "more parallel" / "less parallel" → adjust dyn mix up or down
- Works independently of the outboard 1176/Opto chain — you can parallel compress on the Wing AND have the outboard chain running

## Bus Routing and Subgroups
Use buses to group instruments for shared processing, parallel sends, or stem management.
- "send guitar to bus 3" → `/ch/1/send/3/on i 1`, `/ch/1/send/3/lvl f 0.0`, `/ch/2/send/3/on i 1`, `/ch/2/send/3/lvl f 0.0`
- "create a drum bus" → assign ch13/ch14 sends to a bus, name the bus "Drums", apply bus-level EQ/compression
- "route all DAW tracks through bus 4" → assign ch9-16 sends to bus 4 for group processing
- Buses 1-2 are reserved for the outboard analog send (guitar and vocal chains). Use buses 3+ for subgroups.
- "compress the drum bus" → enable dynamics on the bus: `/bus/N/dyn/on i 1`, set glue-style settings (low ratio, slow attack, auto release)

## Bus Compression (Glue)
Apply mix-bus or subgroup compression for cohesion.
- "glue the mix" → enable dynamics on main 1 with gentle settings: ratio 2:1, threshold -15, slow attack (30ms), auto release, auto makeup
- "glue the drums" → same on the drum bus
- "harder glue" → lower threshold, faster attack
- "remove the glue" → `/main/1/dyn/on i 0` or `/bus/N/dyn/on i 0`

## Main Bus Processing
Full mix-bus chain on the main output.
- "sweeten the main" → gentle high shelf boost (+1.5dB @ 12kHz), slight low end bump (+1dB @ 80Hz) on `/main/1/eq/...`
- "main bus EQ off" → `/main/1/eq/on i 0`
- "cut the subs on main" → low cut on main at 30Hz to clean up rumble
- Always use subtle moves on the main bus — 1-2dB max

## Matrix Outputs (/mtx/N/...)
8 matrix buses for alternate monitor feeds, recording sends, or broadcast splits.
- "set up a cue mix on matrix 1" → route selected channels via direct inputs: `/mtx/1/dir/1/in s "CH"`, `/mtx/1/dir/1/on i 1`
- "name the matrix" → `/mtx/1/name s "Headphones"`
- Matrix buses have their own 8-band EQ, dynamics, delay, and inserts — fully independent processing
- "route main to matrix for broadcast" → `/mtx/1/dir/1/in s "MAIN"`, with separate EQ/limiting
- "add delay to matrix" → `/mtx/1/dly/on i 1`, `/mtx/1/dly/m f 10.0` (delay in meters)
- Matrix buses receive from main/bus sends AND direct inputs — flexible routing

## Insert Routing
Manage the Wing's insert points for integrating FX in-line rather than via sends.
- "insert FX 3 on guitar" → `/ch/1/postins/ins s "FX3"`, `/ch/1/postins/on i 1` (inserts FX slot 3 directly into the channel strip)
- "remove the insert" → `/ch/1/postins/ins s "NONE"`, `/ch/1/postins/on i 0`
- Pre-insert vs post-insert: pre is before EQ/dynamics, post is after — use pre for character FX (saturation, tape), post for time-based FX
- "insert before EQ" → use `/ch/N/preins/...`
- "insert after EQ" → use `/ch/N/postins/...`
- Insert wet/dry: `/ch/N/postins/w f 0.5` for 50% blend (parallel insert)
- Insert slot values are strings: "FX1" through "FX16", or "NONE"
- An FX slot can only be inserted on one channel at a time — assigning it elsewhere removes it from the previous channel

## Processing Order
The Wing lets you reorder the channel processing chain (Gate, EQ, Dynamics, Insert).
- "put compression before EQ on vocals" → `/ch/3/proc s "GDEI"` (Gate → Dynamics → EQ → Insert)
- "EQ before compression" → `/ch/3/proc s "GEDI"` (Gate → EQ → Dynamics → Insert — default)
- Common choices: EQ before comp for surgical work, comp before EQ for tonal shaping

## Phase Alignment and Delay
Time-align channels when sources are captured at different distances or through different signal paths.
- "delay guitar dry by 1ms" → `/ch/1/in/set/dlyon i 1`, `/ch/1/in/set/dly f 1.0`
- "align the outboard return" → add delay to ch1 (dry) to match the latency of the analog chain returning on ch2 (processed), so they can be blended without phase issues
- "remove delay" → `/ch/N/in/set/dlyon i 0`
- Rule of thumb: sound travels ~1ms per foot. Outboard analog round-trip is typically 1-3ms depending on converters.

## Creative EQ Presets
Instant character shapes using the Wing's 6-band EQ.
- "telephone voice" → high pass at 500Hz, low pass at 3.5kHz, mid boost at 1.5kHz (+6dB, narrow Q)
- "radio voice" → high pass at 300Hz, low pass at 5kHz, presence boost at 2kHz
- "lo-fi guitar" → high pass at 200Hz, low pass at 4kHz, mid honk at 800Hz
- "air on vocals" → gentle high shelf boost at 12kHz (+2dB), cut 300Hz mud (-2dB)
- "warm guitar" → low shelf boost at 200Hz (+2dB), slight cut at 2.5kHz (-1.5dB), roll off above 10kHz
- "scooped metal" → cut 400-800Hz (-6dB wide Q), boost 100Hz (+3dB), boost 3kHz (+3dB)
- "Nashville scoop" → slight cut at 250Hz, boost at 3-5kHz for clarity, gentle low shelf warmth
- Always apply these to the appropriate channels (both dry and processed when blending, or just processed when using outboard)

## Creative FX Chains
Combine multiple FX slots for complex effects.
- "shimmer reverb" → slot 1: pitch shift up octave, slot 2: long hall reverb fed from slot 1's output
- "slapback into reverb" → slot 1: tape delay (80-120ms, 1 repeat), slot 2: plate reverb
- "modulated delay" → slot 1: chorus or flanger, slot 2: stereo delay
- "vocal doubler" → short delay (20-40ms) with slight pitch shift, low mix (15-20%)
- When chaining, use sends from channel to first slot, then route first slot output to second

## FX Automation (Gradual Changes)
Use Python scripts to ramp FX parameters over time for builds and transitions.
- "swell the reverb over 8 bars" → at current BPM, calculate duration, write a Python script that ramps `/fx/N/fxmix` from current value to target over that duration at ~30fps
- "fade the delay out over 4 bars" → same approach, ramping mix down to 0
- "build the chorus" → gradually increase FX send levels, widen stereo, boost high shelf
- These are one-shot Python scripts — run them and they execute the automation in real time

## Stereo Pair Management

**Wing channels are inherently stereo.** Each channel strip handles a stereo pair of inputs. When a channel's input source is a stereo group (e.g., USB/9-10, LCL/3+4), both L and R are received on that single channel — no need for two channels. The channel's pan and width controls manage the stereo image.

Two ways to handle stereo sources:
1. **Single channel (preferred):** One channel receives both L+R. Set input source to the group (e.g., `USB`, `LCL`), and the Wing automatically pairs consecutive inputs (9+10, 3+4, etc.). Pan/width controls manage stereo image. Simpler routing, one fader controls both sides.
2. **Two channels:** Use two mono channels panned L/R for independent L/R processing. More flexible but uses two channel strips.

**Important: The input source must be set to stereo mode.** New channels default to mono (`M`). To enable stereo, set the mode on the **input source** (not the channel): `/io/in/GRP/N/mode s "ST"`. The channel's `$mode` field is read-only — it reflects the input source mode. Available modes: `M` (mono), `ST` (stereo), `M/S` (mid-side).

Example — set USB/3 to stereo for Ch13:
```
/io/in/USB/3/mode s "ST"
```

See `studio.edn` :stereo-pairs for current stereo source assignments.

Commands:
- "link drums" → ensure ch13 panned hard left, ch14 hard right, faders matched
- "check stereo pairs" → query pan and fader on ch11/12 (synth) and ch13/14 (drums), flag if mismatched
- "swap drum L/R" → swap pan positions on ch13 and ch14 (audience vs drummer perspective)
- "narrow the synth" → bring ch11/12 pan positions closer to center (e.g., -0.7/+0.7 instead of -1.0/+1.0)
- "widen the drums" → push ch13/14 pan positions further apart

## Output Routing
Reassign the Wing's analog and digital outputs for different workflows.

**Important: Bus output `in` uses stereo channel indices, not bus numbers.** Bus 1L=1, Bus 1R=2, Bus 2L=3, Bus 2R=4, Bus 3L=5, Bus 3R=6, etc. Formula: `in = (bus_number - 1) * 2 + 1` for L, `+2` for R.

- "route bus 3 to analog out 3" → `/io/out/LCL/3/grp s "BUS"`, `/io/out/LCL/3/in i 5`
- "stem export mode" → reassign USB outputs so each bus goes to its own stereo pair for multitrack export
- "restore default routing" → reset outputs to match `studio.edn` :wing-io
- "what's going to output 1?" → query `/io/out/LCL/1/grp` and `/io/out/LCL/1/in`

Default output assignments:
- Out 1: Bus 1 L (`in=1`) — vocal outboard send
- Out 2: Bus 2 L (`in=3`) — guitar outboard send

## Channel Strip FX (Full Console Emulations)
The Wing has complete channel strip emulations that combine gate + EQ + compressor in one FX slot. These are loaded as FX effects and inserted on channels.

**Available channel strips:**

| Model      | Name               | Emulation          |
| ---------- | ------------------ | ------------------ |
| \*EVEN\*   | Even Channel       | Neve console       |
| \*SOUL\*   | Soul Channel       | SSL console        |
| \*VINTAGE\*| Vintage Channel    | Vintage console    |
| \*BUS\*    | Bus Channel        | Bus comp channel   |
| \*MASTER\* | Master Channel     | Mastering strip    |

**How to use:**
- "put a Neve strip on guitar" →
  1. `/fx/12/mdl s "*EVEN*"` (load into available FX slot)
  2. `/ch/2/postins/ins s "FX12"` (assign to channel)
  3. `/ch/2/postins/on i 1` (enable insert)
  4. `/ch/2/postins/w f 1.0` (set wet/dry to 100%)
- "SSL strip on vocals" → same flow with `*SOUL*` into another FX slot for ch4
- "remove the channel strip" → `/ch/2/postins/ins s "NONE"`, `/ch/2/postins/on i 0`
- **Each instance requires its own FX slot.** Two channels = two FX slots.
- Channel strip parameters are accessed via `/fx/N/...` (e.g. `/fx/12/eq_on`, `/fx/12/d_cthr`)
- Query `/fx/N` node to discover available parameters for the loaded strip

## Dynamics Sidechain
Use sidechain filtering to make compression frequency-aware.
- "sidechain the vocal comp to 3kHz" → `/ch/3/dynsc/type s "BP"`, `/ch/3/dynsc/f f 3000.0` — compresses only when 3kHz is loud (de-essing via sidechain)
- "sidechain from bass" → `/ch/N/dynsc/src s "CH"` with appropriate channel — compress guitar when bass hits
- "remove sidechain filter" → `/ch/N/dynsc/type s "OFF"`
- Crossover: `/ch/N/dynxo/type`, `/ch/N/dynxo/f` — for frequency-dependent compression

## Gate Sidechain
- "key the gate from the kick" → `/ch/N/gatesc/src` set to kick channel — gate opens only when kick hits (for triggered samples or bass tightening)
- "filter the gate sidechain" → `/ch/N/gatesc/type s "HP6"`, `/ch/N/gatesc/f f 5000.0` — hi-hat triggered gate

## Talkback
The Wing has a built-in talkback system via `/cfg/talk/...`:
- "set up talkback" → `/cfg/talk/assign s "LCL"` (or specific input), configure which buses receive it
- "talkback to bus 5" → `/cfg/talk/A/B5 i 1` — routes talkback to bus 5 (headphone mix)
- "talkback to main" → `/cfg/talk/A/M1 i 1`
- "dim monitors during talkback" → `/cfg/talk/A/mondim i 1`
- Can also use an open channel (ch5-8) as manual talkback by muting/unmuting

## Troubleshooting Workflows
- "I'm not hearing guitar" → check ch1/ch2 mute states, fader levels, input source assignment (`/ch/N/in/conn/grp`), bus routing, main assign (`/ch/N/main/1/on`), insert state. Report what's wrong.
- "there's a buzz" → likely a ground loop or cable issue. Check polarity flip as a quick test: `/ch/N/in/set/inv i 1`. Guide through systematic isolation (mute channels one by one).
- "the outboard sounds weird" → query ch1 and ch2 fader levels, check if bus 1 send is active and at proper level, verify ch2 input source is still LCL/2, check insert state, check processing order
- "something changed" → run verify against `studio.edn`, diff current state against last backup. Use node discovery (`/ch/N`) to inspect full channel state.
- "phase issues" → flip polarity on one channel of a pair, listen for improvement. Try adding small delays to align. Use all-pass filter (`/ch/N/flt/mdl s "AP1"`) for phase rotation at specific frequencies.
- "vocals are thin" → could be phase cancellation between ch3 (dry) and ch4 (processed) if both are going to main. Check polarity, check delay alignment, or mute one.
- "what model is loaded?" → query `/ch/N/eq/mdl`, `/ch/N/dyn/mdl`, `/ch/N/gate/mdl`, `/ch/N/flt/mdl` to see what plugins are on each section
- "what's on the insert?" → query `/ch/N/postins/ins` and `/ch/N/preins/ins` to see FX slot assignments
- "check the console" → send `/?` to verify Wing is responding and get firmware version

## Patchbay Guidance
You can't control the patchbay via OSC, but you can guide Lake through re-patching for alternate signal chains.
- "I want to use the Distressor instead of the 1176 on guitar" → guide: patch cable from HA73 ch1 out (point 2 top) to Distressor in, patch cable from Distressor out to Wing ch2 in (point 3 bottom). Patchbay points 2 and 3 normals are broken.
- "add the Distressor after the Opto on vocals" → guide: patch Opto out to Distressor in, Distressor out to point 7 bottom (Wing ch4 in). Point 7 normal is broken.
- "restore default patching" → guide: remove all front-panel patch cables, normals restore automatically

## Monitor Section (/cfg/mon/...)
Control room monitoring with dedicated controls.
- "dim the monitors" → `/cfg/mon/1/dim f 20.0` — 20dB dim
- "change monitor source" → `/cfg/mon/1/src s "MAIN.1"` — or route from a bus/matrix
- "monitor delay" → `/cfg/mon/1/dly/on i 1`, `/cfg/mon/1/dly/m f 3.0` — 3 meters delay for time-aligned monitors
- "solo mode" → `/cfg/solo/mode s "LIVE"`, `/cfg/solo/chtap s "PFL"` or `"AFL"`
- "mute speakers, keep headphones" → `/mtx/1/mute i 1`. Muting the matrix kills speakers without affecting headphones.
- "restore speakers" → `/mtx/1/mute i 0`

**Speaker routing (current):** Monitor section (MON.PH) → MX1 direct input → Wing Out 7 (MTX/1 L, `in=1`) + Out 8 (MTX/1 R, `in=2`) → P23 top + P24 top (patchbay, normalled) → P23 bottom + P24 bottom → Speakers

Out 7 = MX1 L (`/io/out/LCL/7`: grp=MTX, in=1). Out 8 = MX1 R (`/io/out/LCL/8`: grp=MTX, in=2). Note the stereo indexing — both must NOT be `in=1` or you get mono.

MX1 sources from the monitor phone output via direct input (`/mtx/1/dir/on i 1`, `/mtx/1/dir/in s "MON.PH"`). The Main 1 → MX1 send is **off**. This ensures solo works through speakers — when you solo a channel, the monitor section switches to the solo bus, and MX1 follows.

**Speakers on patchbay (P23/P24):** Speakers are normalled through the patchbay, not direct-wired. This allows switching speaker sources without repatching the Wing. To monitor the Model 12 playback: plug Model 12 main outs into P23 top + P24 top on the front panel — this breaks the Wing normal and sends Model 12 directly to speakers. Pull the cables to restore Wing monitoring. This keeps Model 12 playback completely outside the Wing's signal path, eliminating any feedback risk from open mics.

**Monitor direct input source values:**
- `MON.SPK` — monitor speaker output
- `MON.PH` — monitor phones output (current setting — needed for solo to work through speakers)

**Note:** `/cfg/mon/...` and `/cfg/solo/...` paths are not accessible via wapi (TCP). Use oscsend for fire-and-forget, or configure on the Wing touchscreen.

## Mute Groups (/mgrp/N/...)
8 mute groups for instant muting of assigned channels.
- "set up mute group 1 for local channels" → `/mgrp/1/name s "Local"`, assign ch1-8
- "mute group 1" → `/mgrp/1/mute i 1` — mutes all assigned channels at once
- Useful for quick scene changes: mute all local instruments between songs

## Oscillator / Test Tone
Built-in signal generator for testing and calibration.
- "test tone" → `/cfg/osc/1/mode s "SINE"`, `/cfg/osc/1/f f 1000.0`, `/cfg/osc/1/lvl f -20.0`
- Route oscillator to a channel by setting input source to OSC group

## Scheduled / Timed Operations
Use background Python scripts for operations that happen over time.
- "fade out over 10 seconds" → ramp main fader from current level to -inf over 10s
- "crossfade from guitar to keys over 4 bars" → simultaneously fade ch1/ch2 down and ch10 up over the calculated duration
- "auto-dim after 30 seconds of silence" → monitor levels via subscription, dim main fader if no signal detected

## Headphone / Cue Mixes
Build separate mixes for different monitoring needs using bus sends.
- "build me a vocal practice mix" → create a bus with vocals louder (+6dB), instruments softer (-6dB), more reverb
- "guitarist mix on bus 5" → guitar dry up, everything else down, no FX
- "click track to bus 6" → if using a click in the DAW, route it to a dedicated bus for headphones
- Each bus has independent send levels per channel — fully separate from the main mix
