# Recording Configuration Reference

All gear is permanently wired into the patchbay. Default guitar and vocal chains are normalled and always active. The only connections made at session time are the instruments themselves (guitar into DI, mic into input). Alternative routing requires only a single front-panel patch cable.

## Behringer Wing Rack -- Channel Assignments

Wing channels are inherently stereo — a single channel receives an L+R pair.

| Channel | Name              | Color  | Source                                        | Notes |
| ------- | ----------------- | ------ | --------------------------------------------- | ----- |
| 1       | Vocal Dry         | Blue   | LCL/1 (mic)                                   | GATE dynamics. Pre-fader send to Bus 1 (vocal outboard) |
| 2       | Guitar Dry        | Red    | LCL/2 (DI)                                    | Pre-fader send to Bus 5 (Electric) and Bus 6 (Acoustic); NOT on main |
| 3-4     | Open              |        | Local                                         |       |
| 5       | Gtr Acoustic DI   | Yellow | USR/5 (from Ch2, PRE tap)                     | Clean DI signal bypassing outboard; assigned to main; muted by default |
| 6       | Gtr Ac Mics       | Yellow | LCL/3+4 (stereo condensers, XLR direct)       | Sends to Bus 6 (Acoustic); NOT on main; muted by default |
| 7       | Model 12 Mix      | Orange (8) | USB/3-4 (Model 12 Main Out L/R via Loopback, stereo) | Solo to monitor Model 12 mix during mixing phase |
| 8       | Open              |        | Local                                         |       |
| 9       | Bass              | Green  | USB/9-10 (Logic, stereo pair)                 | Assigned to main |
| 10      | (open)            |        | USB/11-12 (was Keyboard -- use Piano/Synth instead) |       |
| 11      | Piano/Synth       | Green  | USB/13-14 (Logic, stereo pair)                |       |
| 12      | Drums             | Green  | USB/15-16 (Logic, stereo pair)                |       |
| 13-16   | Open              |        |                                               |       |
| 17      | Vocal Processed   | Blue   | LCL/17 (outboard return)                      | DE-ES dynamics. Sends to Bus 7 (recording). Dedicated to live input. |
| 18      | Guitar Processed  | Red    | LCL/18 (outboard return)                      | Sends to Bus 8 (recording). Dedicated to live input. |
| 19-24   | Open              |        |                                               |       |
| 25      | Tape Return 1     | Coral (10) | USB/17 (Model 12 Track 1 via Loopback)     | Individual track return. Assigned to main. Bus sends per project. |
| 26      | Tape Return 2     | Coral (10) | USB/18 (Model 12 Track 2 via Loopback)     | Individual track return. Assigned to main. Bus sends per project. |
| 27      | Tape Return 3     | Coral (10) | USB/19 (Model 12 Track 3 via Loopback)     | Individual track return. Assigned to main. Bus sends per project. |
| 28      | Tape Return 4     | Coral (10) | USB/20 (Model 12 Track 4 via Loopback)     | Individual track return. Assigned to main. Bus sends per project. |
| 29      | Tape Return 5     | Coral (10) | USB/21 (Model 12 Track 5 via Loopback)     | Individual track return. Assigned to main. Bus sends per project. |
| 30      | Tape Return 6     | Coral (10) | USB/22 (Model 12 Track 6 via Loopback)     | Individual track return. Assigned to main. Bus sends per project. |
| 31      | Tape Return 7/8   | Coral (10) | USB/23-24 (Model 12 Tracks 7/8 via Loopback, stereo) | Individual track return. Assigned to main. Bus sends per project. |
| 32      | Tape Return 9/10  | Coral (10) | USB/25-26 (Model 12 Tracks 9/10 via Loopback, stereo) | Individual track return. Assigned to main. Bus sends per project. |
| 33      | Tape Send         | Coral (10) | LCL/3 (Model 12 AUX 1 Out, gain 10dB, phantom OFF) | TAPE (FX13) pre-insert + TAPE-DL (FX6) post-insert. Not on main. Feeds USR/3 (POST tap) -> USB 38 -> Model 12 Ch 6. |
| 34-40   | Open              |        |                                               |       |

**Mute behavior note:** Muting a channel kills its pre-fader sends. To keep sends flowing (e.g. for monitoring a silent channel), use main assign off instead of mute.

## Recording Output Routing (Wing -> Logic)

Logic is the primary multi-track recorder. Recording buses send clean outboard signal (no tape saturation) to Logic via USB.

| USB Out | Source                      | -> Logic Track           | Default State |
| ------- | --------------------------- | ------------------------ | ------------- |
| 1       | USR/1 (Bus 7L -- Vocal Rec) | Vocal (outboard only)    | ON            |
| 3       | USR/8 (Ch18 -- Re-amp out)  | Re-amp return            | OFF -- enable only during re-amping |
| 5       | USR/6 (Bus 9L -- Mic L)     | Condenser L              | OFF -- enable when recording condensers |
| 6       | USR/7 (Bus 9R -- Mic R)     | Condenser R              | OFF -- enable when recording condensers |

USB 2 is no longer used for recording (guitar records via Bus 8 -> USR/2 -> USB 2, or analog). DAW instruments (Ch9-12, Logic session players) are heard directly on the Wing and are not recorded back to Logic.

## Mix Matrix Routing (Wing -> Model 12)

Matrices route processed stems to the Model 12 for hands-on analog mixing. Each matrix feeds a dedicated USB output -> Loopback -> Model 12 channel. Model 12 channels set to USB mode.

| Matrix | Name         | Color      | USB Out | -> M12 Ch | Default Source |
| ------ | ------------ | ---------- | ------- | --------- | -------------- |
| MX1    | Speakers     | --         | Out 7-8 | --        | Main monitor output (P23-P24) |
| MX2    | Mix Vocal    | Blue (2)   | 33      | 1         | Ch25 (vocal tape return). FX3 (DOUBLE/THICK) on post-insert. |
| MX3    | Mix Rhythm   | Red (9)    | 34      | 2         | Bus 10 (RACKAMP) |
| MX4    | Mix Lead     | Red (9)    | 35      | 3         | Bus 11 (ANGEL) |
| MX5    | Mix Overdub  | Coral (10) | 36      | 4         | As needed |
| MX6    | Mix Bass     | Green (5)  | 37      | 5         | Ch9 (Logic bass). FX4 (SUB/MID) on post-insert. |
| MX7    | Mix Drums    | Green (5)  | 39-40   | 7/8       | Ch12 (Logic drums, stereo) |
| MX8    | Mix Piano    | Green (5)  | 41-42   | 9/10      | Ch11 (Logic piano/synth, stereo) |

Model 12 Ch 6 is the tape return (AUX 1 -> Wing TAPE -> USB 38 -> Loopback). Not a matrix -- dedicated analog send/return loop.

### Loopback Routing (Wing USB -> Model 12)

| Wing USB Out | -> M12 USB In | M12 Ch | Content |
| ------------ | ------------- | ------ | ------- |
| 33           | 1             | 1      | Vocal (MX2) |
| 34           | 2             | 2      | Rhythm guitar (MX3) |
| 35           | 3             | 3      | Lead guitar (MX4) |
| 36           | 4             | 4      | Overdub (MX5) |
| 37           | 5             | 5      | Bass (MX6) |
| 38           | 6             | 6      | Tape return (USR/3, Ch33 post-TAPE) |
| 39-40        | 7-8           | 7/8    | Drums stereo (MX7) |
| 41-42        | 9-10          | 9/10   | Piano/Synth stereo (MX8) |

## USB Input Routing (Model 12 -> Loopback -> Wing)

### Individual Track Returns (Tape Returns)

All Model 12 tracks return individually to Ch25-32 via Loopback. Tracks 7/8 and 9/10 are stereo pairs on single channels. Bus sends configured per project.

| Model 12 USB Out | -> Loopback -> | Wing USB In | Wing Channel |
| ---------------- | ------------ | ----------- | ------------ |
| Track 1 | -> | USB In 17 | Ch25 (Tape Return 1) |
| Track 2 | -> | USB In 18 | Ch26 (Tape Return 2) |
| Track 3 | -> | USB In 19 | Ch27 (Tape Return 3) |
| Track 4 | -> | USB In 20 | Ch28 (Tape Return 4) |
| Track 5 | -> | USB In 21 | Ch29 (Tape Return 5) |
| Track 6 | -> | USB In 22 | Ch30 (Tape Return 6) |
| Track 7/8 | -> | USB In 23-24 | Ch31 (Tape Return 7/8, stereo) |
| Track 9/10 | -> | USB In 25-26 | Ch32 (Tape Return 9/10, stereo) |

### Model 12 Stereo Main Return

| Model 12 USB Out | -> Loopback -> | Wing USB In | Wing Channel |
| ---------------- | ------------ | ----------- | ------------ |
| Main L/R | -> | USB In 3-4 | Ch7 (Model 12 Mix, stereo) |

**Per-project routing:** Assign bus sends on each tape return based on content:
- Vocal tracks -> Bus 3 (reverb). Outboard already baked in.
- Guitar tracks -> Bus 10/11 (amp sim) + Bus 3 (reverb). Outboard already baked in.
- Unused tracks -> mute the return channel.

Outboard chains stay dedicated to live input. Tape returns go straight to main with FX via bus sends. Both run simultaneously -- no mode switching.

**Feedback prevention:** Tape return channels are on Main 1 but never re-enter the Model 12. Recording outputs (USB 1-6) go to Logic, not Model 12. Mix matrix outputs (USB 33-42) go to Model 12 but source from processed tape returns/session players -- no loop. USB 3 (re-amp) must be turned OFF after use.

## USR Routing (Virtual Patchbay)

USR `in` values use simple bus numbering (Bus 7 = in=7, Bus 8 = in=8, Bus 9 = in=9), not stereo channel indices.

| USR | Name              | Source | `grp` | `in` | `lr` | USB Out | Purpose                                          |
| --- | ----------------- | ------ | ----- | ---- | ---- | ------- | ------------------------------------------------ |
| 1   | Vocal Dry         | Bus 7  | BUS   | 7    | L    | 1       | Clean outboard vocal for recording (no tape)     |
| 2   | (free)            | --     | --    | --   | --   | --      | Freed -- guitar recording now uses analog (Out 3 -> P9) |
| 3   | Tape Return       | Ch33   | CH    | 33   | POST | 38      | Tape-processed signal (TAPE + TAPE-DL) from Model 12 AUX 1 loop -> Model 12 Ch 6 |
| 4   | (free)            | --     | --    | --   | --   | --      | Open                                             |
| 5   | Gtr Acoustic DI   | Ch2    | CH    | 2    | L+R  | --      | Clean DI tap for Ch5; bypasses outboard          |
| 6   | Mic Dry L         | Bus 9  | BUS   | 9    | L    | 5       | Clean condenser L recording (OFF by default)     |
| 7   | Mic Dry R         | Bus 9  | BUS   | 9    | R    | 6       | Clean condenser R recording (OFF by default)     |
| 8   | Re-amp Out        | Ch18   | CH    | 18   | L    | 3       | Guitar Processed output for re-amping (OFF by default) |

## Bus Layout

| Bus | Name         | Color  | Output         | `/io/out/LCL/N/in` index | Purpose |
| --- | ------------ | ------ | -------------- | ------------------------ | ------- |
| 1   | Vocal Send   | Blue   | Wing Out 1     | 1 (Bus 1L)               | Pre-fader send from Ch1 -> vocal outboard chain (P1-P4); clean signal |
| 2   | Guitar Send  | Red    | Wing Out 2     | 3 (Bus 2L)               | Receives from Bus 5 + Bus 6; sends to guitar outboard chain (P5-P8); no pre-insert; clean signal |
| 3   | Reverb       | Green  | (Main only)    | --                       | Shared reverb bus -- receives sends from Bus 1 and Bus 2; FX2 (PLATE) on pre-insert |
| 4   | Mic Send     | --     | Wing Out 4     | 8 (Bus 4R)               | Condenser mic R send to P10 (R only) |
| 5   | Electric     | Red    | -> Bus 2 send  | --                       | FX6 (ANGEL) pre-insert for lead; FX1 (DELUXE) available for rhythm. Receives from Ch2; sends to Bus 2; muted by default |
| 6   | Acoustic     | Yellow | -> Bus 2 send  | --                       | FX11 (RACKAMP, clean/bright) pre-insert; receives from Ch2 + Ch6; sends to Bus 2 |
| 7   | Vocal Rec    | Blue   | -- (USR only)  | --                       | No pre-insert; receives from Ch17 pre-fader (outboard return); feeds USR/1 -> USB 1 -> Logic |
| 8   | Guitar Rec   | Red    | Wing Out 3     | 15 (Bus 8L)              | No pre-insert; receives from Ch18 pre-fader (outboard return); -> P9 (tape return) |
| 9   | Mic Rec      | Yellow | -- (USR only)  | --                       | No pre-insert; receives from Ch6 pre-fader; feeds USR/6+7 -> USB 5/6 -> Logic (OFF by default) |
| 10  | Rhythm Monitor | --   | --             | --                       | FX7 (RACKAMP) pre-insert. Receives from Ch26/Ch18. Sends to MX3 (Mix Rhythm). Not on main. |
| 11  | Lead Monitor   | --   | --             | --                       | FX12 (ANGEL) pre-insert. Receives from Ch27/Ch18. Sends to MX4 (Mix Lead). Not on main. |

Bus output `in` parameter uses stereo channel indices, not bus numbers: Bus 1L = 1, Bus 1R = 2, Bus 2L = 3, Bus 2R = 4, Bus 4L = 7, Bus 4R = 8, Bus 7L = 13, Bus 7R = 14, Bus 8L = 15, Bus 8R = 16, Bus 9L = 17, Bus 9R = 18.

**Guitar mode switching:** Bus 5 (Electric) and Bus 6 (Acoustic) both feed into Bus 2 (outboard send). Mute Bus 5 for acoustic mode, mute Bus 6 for electric mode. Ch2 sends pre-fader to both buses simultaneously -- the muted bus is silenced before it reaches Bus 2.

**Recording buses have no TAPE pre-inserts.** Logic records clean outboard signal. Tape saturation is applied during mixing via Model 12 AUX 1 send/return loop (see Tape Saturation section below).

## Tascam Model 12 -- Role and Track Assignments

The Model 12 is the analog mixing console, not the primary recorder. It receives processed stems from the Wing via USB (Loopback) and mixes them with real faders, EQ, and compression. Logic handles all recording. Model 12 captures its stereo mixdown on tracks 11/12.

### Model 12 Channel Assignments (Mixing)

| M12 Ch | Source (USB In) | Wing Source | Content |
| ------ | --------------- | ----------- | ------- |
| 1      | USB 33 (MX2)   | Ch25 vocal tape return | Processed vocal |
| 2      | USB 34 (MX3)   | Bus 10 (RACKAMP) | Rhythm guitar |
| 3      | USB 35 (MX4)   | Bus 11 (ANGEL) | Lead guitar |
| 4      | USB 36 (MX5)   | Per project | Overdub |
| 5      | USB 37 (MX6)   | Ch9 (Logic bass) | Bass |
| 6      | USB 38 (USR/3) | Ch33 (tape return) | Tape saturation aux return |
| 7/8    | USB 39-40 (MX7) | Ch12 (Logic drums) | Drums stereo |
| 9/10   | USB 41-42 (MX8) | Ch11 (Logic piano/synth) | Piano/Synth stereo |
| 11/12  | Internal        | --          | Stereo mixdown capture (always recording) |

### Model 12 Track Assignments (Legacy Recording)

| Track | Mode     | Source                                              | Format |
| ----- | -------- | --------------------------------------------------- | ------ |
| 1     | USB      | Vocal + outboard (Wing USB Out 1 / USR/1 / Bus 7)   | Mono   |
| 2     | MTR      | Guitar processed (Wing Out 3 -> P9 -> analog line in) | Mono   |
| 3-6   | MTR      | Previous takes / overdub slots. Track 3 for re-amp (USB 3 / USR/8 / Ch18). | Mono |
| 7/8   | MTR      | Free. Can be USB for condenser mics (USB 5/6). | Stereo |
| 9/10  | MTR      | Free for overdubs / additional takes                | Stereo |
| 11/12 | Internal | Model 12 main capture (always recording)            | Stereo |

The Model 12 internal stereo mix (tracks 11/12) returns to the Wing via USB Stereo Out -> Loopback -> Wing USB In 3-4 -> Ch7 (Model 12 Mix). Solo Ch7 to monitor the Model 12 mix during mixing.

## Tape Saturation (Mixing Phase)

Tape is a mixing effect, not a recording effect. Logic records clean outboard signal. During mixing, the Model 12's AUX 1 send routes selected channels through the Wing's TAPE + TAPE-DL effects on Ch33.

**Signal path:**
- Model 12 AUX 1 Out (pre-fader) -> Wing LCL 3 (gain 10dB, phantom OFF) -> Ch33
- Ch33 pre-insert: FX13 (TAPE, drive 10, speed 30)
- Ch33 post-insert: FX6 (TAPE-DL, time 60ms min, no feedback, drive 30, flutter 55)
- Ch33 -> USR/3 (POST tap) -> USB 38 -> Loopback -> Model 12 Ch 6 line in (USB mode)

**Controls:**
- Per-channel AUX 1 knobs control tape send amount
- Ch 6 fader controls tape return blend level
- **Do not send drums to tape** -- transient latency from the round-trip creates audible slapback on percussive material

## Patchbay -- Samson 48-Point TRS

### How Normalled Connections Work

Each patchbay point has a top jack and a bottom jack. In a normalled configuration, the top jack internally routes to the bottom jack without any cable. This means the default signal path is always active.

- **Top jack** = output from a piece of gear
- **Bottom jack** = input to the next piece of gear
- **No cable inserted** = signal flows from top to bottom automatically (normalled)
- **Cable inserted into top** = breaks the normal, signal goes to wherever the cable leads
- **Cable inserted into bottom** = breaks the normal, bottom jack receives from wherever the cable comes from

This allows the default recording chains (guitar, vocal) to work without patching any cables, while still giving full flexibility to reroute through different outboard gear when needed.

### Default Vocal Chain (Points 1-4)

Signal flows through these four normalled points without any cables patched:

1. Wing Rack analog out 1 (Bus 1) -> HA73-EQX2 channel A input
2. HA73-EQX2 channel A output -> WA76 channel A input
3. WA76 channel A output -> Audioscape Opto input
4. Audioscape Opto output -> Wing Rack LCL input 17 (Vocal Processed, ch17)

### Default Guitar Chain (Points 5-8)

Signal flows through these four normalled points without any cables patched:

1. Wing Rack analog out 2 (Bus 2) -> HA73-EQX2 channel B input
2. HA73-EQX2 channel B output -> WA76 channel B input
3. WA76 channel B output -> Distressor input
4. Distressor output -> Wing Rack LCL input 18 (Guitar Processed, ch18)

### Patch Points

| Point | Top (Output From)           | Bottom (Input To)              | Chain        |
| ----- | --------------------------- | ------------------------------ | ------------ |
| 1     | Wing LCL Out 1 (Bus 1)      | HA73 A In                      | Vocal        |
| 2     | HA73 A Out                  | WA76 A In                      | Vocal        |
| 3     | WA76 A Out                  | Opto In                        | Vocal        |
| 4     | Opto Out                    | Wing LCL In 17                 | Vocal        |
| 5     | Wing LCL Out 2 (Bus 2)      | HA73 B In                      | Guitar       |
| 6     | HA73 B Out                  | WA76 B In                      | Guitar       |
| 7     | WA76 B Out                  | Distressor In                  | Guitar       |
| 8     | Distressor Out              | Wing LCL In 18                 | Guitar       |
| 9     | Wing Out 3 (USR/3)          | Model 12 Ch 6 line in          | Tape Return  |
| 10    | Wing Out 4 (Bus 4R)         | (open)                         | Acoustic Mic |
| 11-22 |                             |                                | Open         |
| 23    | Wing LCL Out 7 (MTX/1 L)    | Speakers L                     | Monitors     |
| 24    | Wing LCL Out 8 (MTX/1 R)    | Speakers R                     | Monitors     |

## Wing FX Pre-Insert Assignments

| FX Slot | Model   | Insert Location    | Purpose |
| ------- | ------- | ------------------ | ------- |
| FX1     | DELUXE  | (available)        | Electric guitar amp sim (Fender Deluxe) -- rhythm mode option for Bus 5 |
| FX2     | PLATE   | Bus 3 pre-insert   | Shared plate reverb return -- Bus 1 and Bus 2 send to Bus 3 |
| FX3     | DOUBLE  | MX2 post-insert    | Vocal doubler (THICK mode) on Mix Vocal matrix |
| FX4     | SUB     | MX6 post-insert    | Bass octaver (MID mode) on Mix Bass matrix |
| FX6     | TAPE-DL | Ch33 post-insert   | Tape delay on tape aux loop (time 60ms, drive 30, flutter 55) |
| FX7     | RACKAMP | Bus 10 pre-insert  | Rhythm guitar amp sim for mixing (shared bus for tape returns + live) |
| FX11    | RACKAMP | Bus 6 pre-insert   | Acoustic amp sim (clean/bright: pre 7, buzz 1, punch 2, crunch 1, drive 1, output 8, leq 3, heq 7.5) |
| FX12    | ANGEL   | Bus 11 pre-insert  | Lead guitar amp sim for mixing (shared bus for tape returns + live) |
| FX13    | TAPE    | Ch33 pre-insert    | Tape saturation on tape aux loop (drive 10, speed 30) |

**Freed FX slots:** FX5, FX8, FX9, FX10, FX14, FX15 are available.

Pre-inserts are assigned at `/ch/N/preins/ins` and `/bus/N/preins/ins`, enabled at `.../preins/on i 1`.

## Signal Chains (Normalled)

**Vocal (outboard):** Mic -> Wing LCL/1 -> Ch1 (preamp gain, GATE dynamics) -> Bus 1 send (pre-fader, 0dB) -> Wing Out 1 -> P1 -> HA73 A -> P2 -> WA76 A -> P3 -> Opto -> P4 -> Wing LCL/17 -> Ch17 (Vocal Processed, DE-ES dynamics)

**Vocal (recording):** Ch1 (GATE) -> Bus 1 -> outboard (HA73 A -> WA76 A -> Opto) -> Ch17 (DE-ES) -> Bus 7 send (pre-fader) -> USR/1 (Bus 7L) -> USB 1 -> Logic. Records gate + outboard + de-esser. No tape, no reverb.

**Guitar (Electric mode -- outboard):** DI -> Wing LCL/2 -> Ch2 (preamp gain, no pre-insert) -> Bus 5 send (pre-fader) -> FX6/ANGEL (Bus 5 pre-insert, lead; or FX1/DELUXE for rhythm) -> Bus 5 -> Bus 2 send -> Wing Out 2 -> P5 -> HA73 B -> P6 -> WA76 B -> P7 -> Distressor -> P8 -> Wing LCL/18 -> Ch18 (Guitar Processed)

**Guitar (Acoustic mode -- outboard):** DI -> Wing LCL/2 -> Ch2 (preamp gain, no pre-insert) -> Bus 6 send (pre-fader) -> FX11/RACKAMP (Bus 6 pre-insert) -> Bus 6 -> Bus 2 send -> Wing Out 2 -> P5 -> HA73 B -> P6 -> WA76 B -> P7 -> Distressor -> P8 -> Wing LCL/18 -> Ch18 (Guitar Processed)

**Guitar (recording -- with amp sim):** Ch2 -> Bus 5/6 (amp sim) -> Bus 2 -> outboard (HA73 B -> WA76 B -> Distressor) -> Ch18 -> Bus 8 send (pre-fader) -> Bus 8 -> Logic. Bus 5 or 6 unmuted, Ch2->Bus 2 send OFF. Records outboard only (no tape).

**Guitar (recording -- clean DI, no amp sim):** Ch2 -> Bus 2 (direct send) -> outboard (HA73 B -> WA76 B -> Distressor) -> Ch18 -> Bus 8 send (pre-fader) -> Bus 8 -> Logic. Bus 5+6 muted, Ch2->Bus 2 send ON. Records outboard only (no tape).

**Acoustic Mic path (Ch6 unmuted -- outboard):** Condensers -> Wing LCL/3+4 -> Ch6 (no pre-insert) -> Bus 6 send -> FX11/RACKAMP (Bus 6 pre-insert) -> Bus 6 -> Bus 2 -> outboard chain

**Acoustic Mic path (recording):** Ch6 -> Bus 9 send (pre-fader) -> Bus 9 -> USR/6 (Bus 9L) + USR/7 (Bus 9R) -> USB Out 5/6 -> Logic (USB 5/6 OFF by default)

**Acoustic DI bypass (Ch5):** DI -> Ch2 -> USR/5 (PRE tap, grp=CH in=2) -> Ch5 -> Main 1 (clean DI, no outboard; muted by default)

**Shared Reverb:** Ch1/Ch2 -> Bus 3 send -> FX2/PLATE (Bus 3 pre-insert) -> Bus 3 -> Main 1

**Tape Aux Loop (mixing):** Model 12 AUX 1 Out -> Wing LCL/3 -> Ch33 -> FX13/TAPE (pre-insert) -> FX6/TAPE-DL (post-insert) -> USR/3 (POST tap) -> USB 38 -> Loopback -> Model 12 Ch 6

## Re-Amping Workflow

Re-amping sends a recorded dry guitar track back through the Wing's amp sim buses and outboard chain to capture a new processed take.

**Signal path:** Ch13 (Tape Playback) -> Bus 5 (amp sim) -> Bus 2 -> outboard -> Ch18 (Guitar Processed) -> USR/8 -> USB Out 3 -> Loopback -> Model 12 Track 3

**Procedure:**
1. Set Model 12 Track 3 to USB mode (receives from Wing USB Out 3 / USR/8)
2. Enable USR/8: source = Ch18 (Guitar Processed), tap = L, grp=CH, in=18
3. Confirm USB Out 3 is active in Loopback routing
4. Send the dry guitar playback from Ch13 through Bus 5 (Electric) for amp sim processing
5. Record the processed output on Model 12 Track 3
6. When done: turn off USB Out 3 (disable in Loopback), set Track 3 back to MTR mode

**Critical:** USB Out 3 must be turned OFF after re-amping. Leaving it on creates a feedback path: Ch18 -> USB 3 -> Model 12 Track 3 -> stereo mix -> Wing Ch7 -> Main.

## Stereo Pair Configuration

Wing channels are inherently stereo. For stereo sources, set the input mode to stereo: `/io/in/GRP/N/mode s "ST"`. This pairs consecutive inputs (e.g., USB/9+10, LCL/3+4).

Current stereo sources:
- Ch6 (Gtr Ac Mics): LCL/3+4, mode ST
- Ch7 (Model 12 Mix): USB/3-4, mode ST
- Ch9 (Bass): USB/9-10, mode ST
- Ch11 (Piano/Synth): USB/13-14, mode ST
- Ch12 (Drums): USB/15-16, mode ST

## Outboard Calibration

Calibrated settings for both chains. Do not adjust without retesting.

### Vocal Chain (HA73 A + WA76 A + Opto)

| Unit   | Setting                              | Notes |
| ------ | ------------------------------------ | ----- |
| HA73 A | Input: Line, Output: set for ~0 VU  | Not used as preamp -- line-level only |
| HA73 A | EQ: Flat (all bands bypassed)        | Shape with Wing EQ unless analog color is wanted |
| WA76 A | Attack: 3, Release: 7, Ratio: 4:1   | Catching peaks, ~3-4dB GR on transients |
| WA76 A | Input/Output: unity through           | Adjust to match level into Opto |
| Opto   | Peak Reduction: ~40%, Mode: Compress | Smooth leveling, ~2-3dB GR average |
| Opto   | Gain: unity through                   | Ch17 return fader handles monitoring level |

### Guitar Chain (HA73 B + WA76 B + Distressor)

| Unit       | Setting                              | Notes |
| ---------- | ------------------------------------ | ----- |
| HA73 B     | Input: Line, Output: set for ~0 VU  | Not used as preamp -- line-level only |
| HA73 B     | EQ: Flat or slight low shelf boost   | Optional warmth/body shaping |
| WA76 B     | Attack: 5, Release: 6, Ratio: 4:1   | Medium attack to let pick transient through |
| Distressor | Ratio: 4:1, Dist 2 (tape) engaged   | Leveling + warm harmonic color |
| Distressor | Attack: 5-6, Release: Auto           | Tracks guitar dynamics naturally |

## Loopback Software Routing

### Wing -> Logic (Recording)

| From                                          | To                                         | Default State |
| --------------------------------------------- | ------------------------------------------ | ------------- |
| Wing USB Out 1 (USR/1 -- Bus 7L, Vocal)       | Logic input (vocal outboard, no tape)      | ON            |
| Wing USB Out 3 (USR/8 -- Ch18, Re-amp out)    | Logic input (re-amp return)                | OFF           |
| Wing USB Out 5 (USR/6 -- Bus 9L, Mic L)       | Logic input (condenser L)                  | OFF           |
| Wing USB Out 6 (USR/7 -- Bus 9R, Mic R)       | Logic input (condenser R)                  | OFF           |

### Wing -> Model 12 (Mix Matrices)

| From                                          | To                                         | Default State |
| --------------------------------------------- | ------------------------------------------ | ------------- |
| Wing USB Out 33 (MX2 -- Mix Vocal)            | Model 12 Ch 1 (via Loopback)              | ON            |
| Wing USB Out 34 (MX3 -- Mix Rhythm)           | Model 12 Ch 2 (via Loopback)              | ON            |
| Wing USB Out 35 (MX4 -- Mix Lead)             | Model 12 Ch 3 (via Loopback)              | ON            |
| Wing USB Out 36 (MX5 -- Mix Overdub)          | Model 12 Ch 4 (via Loopback)              | ON            |
| Wing USB Out 37 (MX6 -- Mix Bass)             | Model 12 Ch 5 (via Loopback)              | ON            |
| Wing USB Out 38 (USR/3 -- Tape Return)        | Model 12 Ch 6 (via Loopback)              | ON            |
| Wing USB Out 39-40 (MX7 -- Mix Drums)         | Model 12 Ch 7/8 (via Loopback, stereo)    | ON            |
| Wing USB Out 41-42 (MX8 -- Mix Piano)         | Model 12 Ch 9/10 (via Loopback, stereo)   | ON            |

### Model 12 -> Wing (Tape Returns -- permanent)

| From                                            | To                                         | Default State |
| ----------------------------------------------- | ------------------------------------------ | ------------- |
| Model 12 USB Track 1                            | Wing USB In 17 -> Ch25 (Tape Return 1)      | ON            |
| Model 12 USB Track 2                            | Wing USB In 18 -> Ch26 (Tape Return 2)      | ON            |
| Model 12 USB Track 3                            | Wing USB In 19 -> Ch27 (Tape Return 3)      | ON            |
| Model 12 USB Track 4                            | Wing USB In 20 -> Ch28 (Tape Return 4)      | ON            |
| Model 12 USB Track 5                            | Wing USB In 21 -> Ch29 (Tape Return 5)      | ON            |
| Model 12 USB Track 6                            | Wing USB In 22 -> Ch30 (Tape Return 6)      | ON            |
| Model 12 USB Tracks 7/8                         | Wing USB In 23-24 -> Ch31 (Tape Return 7/8 stereo) | ON     |
| Model 12 USB Tracks 9/10                        | Wing USB In 25-26 -> Ch32 (Tape Return 9/10 stereo) | ON    |

### Model 12 -> Wing (Stereo Main Return)

| From                                            | To                                         | Default State |
| ----------------------------------------------- | ------------------------------------------ | ------------- |
| Model 12 USB Main L/R                           | Wing USB In 3-4 -> Ch7 (Model 12 Mix, stereo) | ON         |

DAW instruments do not route to the Model 12 directly -- they reach it via mix matrices (MX6-MX8).

## Monitor / Speaker Routing

Speakers are driven through Matrix 1 (MX1), not directly from Main 1. MX1 sources from the monitor phones output via direct input -- this enables solo to work through speakers (the monitor section switches to the solo bus on solo, and MX1 follows).

| Path | Detail |
| ---- | ------ |
| Monitor section (MON.PH) | -> MX1 direct input (`/mtx/1/dir/in s "MON.PH"`, `/mtx/1/dir/on i 1`) |
| MX1 | -> Wing Out 7 + Wing Out 8 (both sourced from MTX/1) |
| Wing Out 7 + 8 | -> Speakers (direct wired, not through patchbay) |

Main 1 -> MX1 send is **off**. To mute speakers without affecting headphones: `/mtx/1/mute i 1`.

Valid `dir/in` source values: `MON.SPK` (monitor speaker out), `MON.PH` (monitor phones out -- current setting).

## A/B Testing: Hardware vs Plugin

To compare a hardware outboard unit against a Wing plugin emulation fairly, both paths must receive the same clean source and be independently level-matched.

**Key rules:**
- Source channel must have dynamics **OFF** and must **not** be assigned to main
- Plugin goes on a separate channel (not the source) -- the pre-fader send tap (`ptap`) is post-dynamics, so a plugin on the source channel would color the hardware signal too
- Use `wingctl meter all` for level matching -- adjust faders until outputs are within 0.5dB
- Single-channel meter reads (`wingctl meter /ch/N`) may return stale data; always use `all`

**Example setup (bass -> Opto vs Wing LA-2A):**
1. Ch9 (source, Bass): dynamics OFF, sends to Bus 1 pre-fader, NOT assigned to main
2. Ch17 (hardware return): Opto -> LCL/17 return, assigned to main
3. Ch19 (plugin): receives same USB/9 source directly, Wing LA-2A enabled, assigned to main
4. Disable Bus 1 -> Bus 3 send to prevent reverb bus crosstalk

Solo Ch17 for hardware, solo Ch19 for plugin. Solo works through speakers because MX1 sources from MON.PH (see Monitor / Speaker Routing above).
