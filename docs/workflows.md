# Production Workflows

Multi-step production workflows, snapshots, gain staging, and metering.

## Multi-Step Production Workflows

### "Get me a vocal sound"
1. High pass ch3/ch4 at 80Hz
2. Cut 300Hz mud (-2dB)
3. Boost presence at 3kHz (+2dB)
4. Add air at 12kHz (+1.5dB)
5. Enable gentle compression (ratio 3:1, threshold -18, slow attack)
6. Load plate reverb on FX slot 1, set send from ch3/ch4 at -15dB
7. Load delay on FX slot 2, sync to BPM, set send at -20dB

### "Get me a Neve vocal sound"
1. High pass ch3/ch4 at 80Hz
2. Load E84 EQ: `/ch/3/eq/mdl s "E84"` (and ch4)
3. Set Neve EQ: low freq 110Hz +2dB, mid freq 3k2 +1.5dB, high freq 12k +1dB
4. Load Neve comp: `/ch/3/dyn/mdl s "ECL33"` — gentle limiter threshold, comp ratio 2:1
5. Or go full Neve channel strip: load `*EVEN*` into FX slot, insert on ch4

### "Get me a guitar tone"
1. High pass ch1/ch2 at 80Hz
2. Warm low shelf boost at 200Hz (+1.5dB)
3. Cut boxy 400Hz (-2dB)
4. Boost pick attack at 3kHz (+1.5dB)
5. Roll off above 10kHz
6. Load slapback delay on FX slot, sync to BPM, 20% mix

### "Make it sound vintage"
1. Load tape machine on an FX slot: `/fx/N/mdl s "TAPE"` — adds tape saturation
2. Load Pultec EQ: `/ch/N/eq/mdl s "PULSAR"` — musical boost/atten curves
3. Load LA-2A comp: `/ch/N/dyn/mdl s "LA"` — smooth optical compression
4. Or load `*VINTAGE*` channel strip for the full vintage console vibe

### "Set up for tracking"
1. Reset all EQ to flat, models to STD
2. Remove all dynamics, models to COMP
3. Reset all gate models to GATE
4. Set all faders to unity
5. Verify channel names and colors match config
6. High pass vocals at 80Hz (always)
7. Confirm outboard chain is active (ch2 and ch4 unmuted, bus sends active)
8. Load basic reverb for headphone monitoring
9. Clear all inserts: set preins/postins to "NONE"

### "Set up for mixing" (Model 12 as analog console)

The Model 12 receives fully processed stems from the Wing and mixes them with real faders, EQ, and compression. Logic handles playback. The Wing handles FX. The Model 12 handles the mix.

**Routing setup:**
1. Mix matrices MX2-MX8 permanently route processed stems to Model 12 via USB 33-42 (Loopback)
2. Model 12 channels set to USB mode to receive from Wing
3. Assign Wing bus sends on each tape return per project:
   - Vocal tracks → MX2 (with FX3/DOUBLE post-insert)
   - Guitar tracks → Bus 10/11 (amp sim) → MX3/MX4
   - Session players → MX6 (bass, FX4/SUB), MX7 (drums), MX8 (piano/synth)
4. Tape saturation via AUX 1 send/return loop (AUX 1 → Wing Ch33 TAPE+TAPE-DL → M12 Ch 6)

**Model 12 channel assignments (via mix matrices):**

| Model 12 Ch | Wing USB Out | Wing Source | Content |
|---|---|---|---|
| 1 | 33 (MX2) | Ch25 vocal tape return | Processed vocal (FX3/DOUBLE on MX2 post-insert) |
| 2 | 34 (MX3) | Bus 10 (RACKAMP) | Rhythm guitar |
| 3 | 35 (MX4) | Bus 11 (ANGEL) | Lead guitar |
| 4 | 36 (MX5) | Per project | Overdub |
| 5 | 37 (MX6) | Ch9 (Logic bass) | Bass (FX4/SUB on MX6 post-insert) |
| 6 | 38 (USR/3) | Ch33 (TAPE + TAPE-DL) | Tape aux return |
| 7/8 | 39-40 (MX7) | Ch12 (Logic drums) | Drums stereo |
| 9/10 | 41-42 (MX8) | Ch11 (Logic piano/synth) | Piano/Synth stereo |
| 11/12 | Internal | -- | Stereo mixdown (always recording) |

**Mixing procedure:**
1. Press play in Logic (or use Model 12 transport if synced)
2. Balance levels with Model 12 faders
3. Shape tone with Model 12 per-channel EQ
4. Add compression on individual channels as needed
5. Model 12 tracks 11/12 capture the stereo mix automatically
6. A/B different balances by adjusting faders — each pass is a new mix
7. Swap takes in Logic if needed, run the mix again

**Optional: outboard on stems**
Route individual stems through the Wing's outboard chains before they hit the Model 12:
- Vocal stem → Bus 1 Vocal Send → outboard A side (HA73 A → WA76 A → Opto) → Ch17 → Model 12
- Guitar stem → Bus 2 Guitar Send → outboard B side (HA73 B → WA76 B → Distressor) → Ch18 → Model 12

**Monitoring the Model 12 mix:**
The Model 12 stereo main mix returns to the Wing via USB (Loopback → USB In 3-4 → Ch7 Model 12 Mix). Solo Ch7 to hear only the Model 12 mix:
- OSC: `/ch/7/$solo i 1` (solo on), `/ch/7/$solo i 0` (solo off)
- Or press the solo button on Ch7's strip on the Wing

Speakers work with solo because MX1 sources from MON.PH (monitor phones output), which switches to the solo bus automatically. No cable swapping — the Wing is always the monitoring hub for both tracking and mixing.

**One-button shortcut:** The Wing has 4 GPIO ports with user-assignable buttons (1/4" TRS jacks on the back panel). A simple momentary footswitch or desktop button plugged into GPIO 1 can be configured to toggle Ch7 solo. Set up via `/$CTL/USER/GPIO/1/BU/1` to assign the solo toggle action. One physical button to switch between full monitoring and Model 12 mix only.

**Tips:**
- The Model 12's built-in compressors and EQ add their own character — use them
- Don't overthink it — move faders, listen, commit
- Every mix pass is captured on 11/12. Compare multiple passes later.
- Takes are Logic's job. The Model 12 just mixes what it receives.

### "Shut it down"
1. Save full state backup with timestamp
2. Mute all channels
3. Main fader to -inf
4. Report: backup saved, board muted

## Mix Snapshots and Recall

Two snapshot systems are available — use both:

### Wing-native Snapshots (on-device)
The Wing stores scenes inside a Show file on internal storage. This is the fastest way to save and recall.

- **Save to Wing:** `wing_set /$CTL/$GLOBALS/$savenow 1` — saves current board state to the active scene's `.snap` file
- **Check active show:** `wing_get /$CTL/LIB/$actshow` → returns path like `I:/A.show`
- **Check active scene:** `wing_get /$CTL/LIB/$active` → returns path like `I:/TEST.snap`
- **Check scene list:** `wing_get /$CTL/LIB/$scenes` → returns comma-separated scene names
- **Navigate scenes:** `wing_set /$CTL/$GLOBALS/showscene <index>` or use MIDI GO/NEXT/PREV

**Important:** Creating new scenes/snaps within a show can only be done from the Wing touchscreen (LIBRARY > Add > Snap). The API can **save to** and **recall** existing scenes, but not create new ones. A show must be loaded first (LIBRARY > New Show on the touchscreen).

### Local JSON Snapshots (on this machine)
- "save this mix as 'verse'" → query all channels via `wing_node`, save to `snapshots/verse.json`
- "recall verse mix" → read the JSON and push all parameters back via `wing_set`
- "compare verse and chorus" → toggle between two saved snapshots
- More flexible than Wing-native: can diff, version control, and selectively restore parts of a mix

### When to Use Which
- Wing-native for fast recall during a session or on power-up (the Wing auto-loads its last show)
- Local JSON for backups, version history, diffing changes, and restoring specific parameters

### Setting Up a New Project (requires Lake's help on the Wing touchscreen)
1. **Initialize the console** (optional but recommended for a clean start):
   - On the Wing: SETUP > INIT > select ALL scopes (or specific ones) > tap **INIT**
   - This resets all channels, EQ, dynamics, routing, FX, etc. to factory defaults
   - Claude **cannot** trigger INIT remotely — it's touchscreen-only
   - Safe settings that survive INIT: network/IP, console name, clock, USB host speed, library contents
2. Press **LIBRARY** on the Wing
3. Tap **New Show** — give it a name (e.g. the song or session name)
4. Tap **+** (Add) > **Snap** — name it (e.g. "Base", "Tracking", "Verse")
5. Tell Claude the show is ready — from here, Claude can:
   - Set up all channel names, colors, routing, EQ, dynamics, FX via API
   - Run `scripts/set-channel-names.sh` and `scripts/setup-vocal-la2a.sh`
   - Save the current state: `/$CTL/$GLOBALS/$savenow → 1`
   - Verify the show: `/$CTL/LIB/$actshow` and `/$CTL/LIB/$active`
   - Save local JSON snapshots to `snapshots/`
   - Navigate between scenes once multiple exist
6. To add more scenes later, repeat step 4 on the touchscreen — Claude can't create scenes, only save to existing ones

## MIDI Scene Control
Trigger Wing scenes from scripts for setlist-based workflows.
- "go to next scene" → send MIDI Ch9 PC 5 (Scene GO NEXT)
- "previous scene" → send MIDI Ch9 PC 4 (Scene GO PREV)
- "recall scene 12" → send MIDI Ch7 CC32 + PC for bank/program select
- Build setlists: a text file of songs with their BPMs and scene numbers, navigate with simple commands

## Gain Staging
Proper gain structure prevents noise and distortion across the chain.
- "check gain staging" → query input trim, fader level, and bus send levels on all active channels. Flag anything where trim is above +20dB or fader is above +6dB.
- "reset gain staging" → set all trims to 0, all faders to 0 (unity), adjust from there
- "pad the guitar" → reduce input trim if signal is too hot: `/ch/1/in/set/trim f -10.0`
- When outboard is in the chain, gain staging matters more — the HA73 and 1176 have sweet spots. If the Wing's output to the patchbay is too hot, lower the bus send level, not the fader.

## Level Matching for A/B
Critical for honest comparisons — louder always sounds "better."
- "level match dry and processed guitar" → query fader levels on ch1 and ch2, adjust so they produce the same perceived volume (processed is usually louder due to compression — drop ch2 a few dB)
- "level match the reference" → when A/B-ing against a reference track, match RMS levels before comparing
- Use `wingctl meter all` to get live output levels across all channels — adjust faders until matched within 0.5dB
- Take multiple readings (dynamic material fluctuates) — `for i in 1 2 3; do wingctl meter all | grep "ch(17|19)"; sleep 1; done`

## Metering and Analysis
- "how hot is the vocal?" → query the channel fader and trim, report the gain structure
- "check all levels" → query faders on all 16 channels, report a quick summary table
- "anything clipping?" → check for channels with fader or trim above safe levels
