# Recording Configuration Reference

All gear is permanently wired into the patchbay. Default guitar and vocal chains are normalled and always active. The only connections made at session time are the instruments themselves (guitar into DI, mic into input). Alternative routing requires only a single front-panel patch cable.

## Behringer Wing Rack -- Channel Assignments

Wing channels are inherently stereo — a single channel receives an L+R pair.

| Channel | Name              | Color  | Source                                        | Notes |
| ------- | ----------------- | ------ | --------------------------------------------- | ----- |
| 1       | Vocal Dry         | Blue   | LCL/1 (mic)                                   | Pre-fader send to Bus 1 (vocal outboard) |
| 2       | Guitar Dry        | Red    | LCL/2 (DI)                                    | Pre-fader send to Bus 5 (Electric) and Bus 6 (Acoustic); NOT on main |
| 3-4     | Open              |        | Local                                         |       |
| 5       | Gtr Acoustic DI   | Yellow | USR/5 (from Ch2, PRE tap)                     | Clean DI signal bypassing outboard; assigned to main; muted by default |
| 6       | Gtr Ac Mics       | Yellow | LCL/3+4 (stereo condensers, XLR direct)       | Sends to Bus 6 (Acoustic); NOT on main; muted by default |
| 7-8     | Open              |        | Local                                         |       |
| 9       | Bass              | Green  | USB/9-10 (Logic, stereo pair)                 | Assigned to main |
| 10      | Keyboard          | Green  | USB/11-12 (Logic, stereo pair)                |       |
| 11      | Synth/Piano       | Green  | USB/13-14 (Logic, stereo pair)                |       |
| 12      | Drums             | Green  | USB/15-16 (Logic, stereo pair)                |       |
| 13      | Tape Playback     | Coral (10) | USB/3-4 (Model 12 stereo out via Loopback) | Fader -12dB; assigned to main; returns Model 12 internal mix for overdub monitoring. Speakers must be muted during open-mic tracking. |
| 14-16   | Open              |        |                                               |       |
| 17      | Vocal Processed   | Blue   | LCL/17 (outboard return)                      |       |
| 18      | Guitar Processed  | Red    | LCL/18 (outboard return)                      |       |
| 19-40   | Open              |        |                                               |       |

**Mute behavior note:** Muting a channel kills its pre-fader sends. To keep sends flowing (e.g. for monitoring a silent channel), use main assign off instead of mute.

## USB Output Routing (Wing → Loopback → Model 12)

| USB Out | Source                      | Model 12 Track            |
| ------- | --------------------------- | ------------------------- |
| 1       | USR/1 (Bus 7L — Vocal Dry)  | Track 1 (vocal w/ tape)   |
| 2       | USR/2 (Bus 8L — Guitar Dry) | Track 2 (guitar w/ tape)  |
| 15      | USR/6 (Bus 9L — Mic L)      | Track 7 (condenser L w/ tape) |
| 16      | USR/7 (Bus 9R — Mic R)      | Track 8 (condenser R w/ tape) |
| 17      | Main 1 L                    | Track 11 (rough mix L)    |
| 18      | Main 1 R                    | Track 12 (rough mix R)    |

All dry channels record simultaneously. Tape emulation is baked in via recording buses (7/8/9) before the USR tap.

## USB Input Routing (Model 12 → Loopback → Wing)

| Model 12 USB Out | → Loopback → | Wing USB In | Wing Channel |
| ---------------- | ------------ | ----------- | ------------ |
| Stereo Out L (track 11/12 internal mix L) | → | USB In 3 | Ch13 L (Tape Playback) |
| Stereo Out R (track 11/12 internal mix R) | → | USB In 4 | Ch13 R (Tape Playback) |

Ch13 receives the Model 12 stereo mixdown for overdub monitoring. The Model 12 handles its own internal mixing per track (faders, mutes) before the stereo out. No feedback loop: tracks 11/12 on the Model 12 are the internal main capture bus, not a USB input.

## USR Routing (Virtual Patchbay)

| USR | Name              | Source | `grp` | `in`       | `lr` | Purpose                                          |
| --- | ----------------- | ------ | ----- | ---------- | ---- | ------------------------------------------------ |
| 1   | Vocal Dry         | Bus 7  | BUS   | 13 (Bus 7L)| L    | Tape-colored vocal for recording via USB Out 1   |
| 2   | Guitar Dry        | Bus 8  | BUS   | 15 (Bus 8L)| L    | Tape-colored guitar for recording via USB Out 2  |
| 3   | (free)            | —      | —     | —          | —    | Open                                             |
| 4   | (free)            | —      | —     | —          | —    | Open                                             |
| 5   | Gtr Acoustic DI   | Ch2    | CH    | 2          | PRE  | Clean DI tap for Ch5; bypasses outboard          |
| 6   | Mic Dry L         | Bus 9  | BUS   | 17 (Bus 9L)| L    | Tape-colored condenser L for recording via USB Out 15 |
| 7   | Mic Dry R         | Bus 9  | BUS   | 17 (Bus 9R)| R    | Tape-colored condenser R for recording via USB Out 16 |

## Tascam Model 12 -- Track Assignments (per project)

| Track | Source                                              | Format |
| ----- | --------------------------------------------------- | ------ |
| 1     | Vocal + TAPE (USB Out 1 / USR/1 / Bus 7)            | Mono   |
| 2     | Guitar + TAPE (USB Out 2 / USR/2 / Bus 8)           | Mono   |
| 3-6   | Open for overdubs / alternate takes                 | Mono   |
| 7/8   | Condenser mics + TAPE (USB Out 15/16 / USR/6+7 / Bus 9) | Stereo |
| 9/10  | Open                                                | Stereo |
| 11/12 | Rough mix (Main 1 L/R via USB 17/18) — always recording | Stereo |

The Model 12 internal stereo mix (its own tracks 11/12) routes back to the Wing via USB Stereo Out → Loopback → Wing USB In 3-4 → Ch13 (Tape Playback). This is the return path for overdub monitoring — the musician hears previous takes through Ch13 on the Wing.

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
| 9     | Wing LCL Out 3 (Bus 4L)     | Condenser Mic L                | Acoustic Mic |
| 10    | Wing LCL Out 4 (Bus 4R)     | Condenser Mic R                | Acoustic Mic |
| 11-24 |                             |                                | Open         |

## Bus Layout

| Bus | Name         | Color  | Output         | `/io/out/LCL/N/in` index | Purpose |
| --- | ------------ | ------ | -------------- | ------------------------ | ------- |
| 1   | Vocal Send   | Blue   | Wing Out 1     | 1 (Bus 1L)               | Pre-fader send from Ch1 → vocal outboard chain (P1–P4); clean signal, no TAPE |
| 2   | Guitar Send  | Red    | Wing Out 2     | 3 (Bus 2L)               | Receives from Bus 5 + Bus 6; sends to guitar outboard chain (P5–P8); no pre-insert; clean signal |
| 3   | Verb Return  | Green  | (Main only)    | —                        | Shared reverb bus — receives sends from Bus 1 and Bus 2; FX2 (PLATE) on pre-insert |
| 4   | Mic Send     | —      | Wing Out 3+4   | 7/8 (Bus 4L/R)           | Stereo condenser mic send to P9 (L) + P10 (R) |
| 5   | Electric     | Red    | → Bus 2 send   | —                        | FX1 (DELUXE) pre-insert; receives from Ch2; sends to Bus 2; muted by default |
| 6   | Acoustic     | Yellow | → Bus 2 send   | —                        | FX11 (RACKAMP, clean/bright) pre-insert; receives from Ch2 + Ch6; sends to Bus 2 |
| 7   | Vocal Rec    | Blue   | — (USR only)   | —                        | FX9 (TAPE) pre-insert; receives from Ch1 pre-fader; feeds USR/1 → USB 1 → Model 12 |
| 8   | Guitar Rec   | Red    | — (USR only)   | —                        | FX10 (TAPE) pre-insert; receives from Ch2 pre-fader; feeds USR/2 → USB 2 → Model 12 |
| 9   | Mic Rec      | Yellow | — (USR only)   | —                        | FX3 (TAPE) pre-insert; receives from Ch6 pre-fader; feeds USR/6+7 → USB 15/16 → Model 12 |

Bus output `in` parameter uses stereo channel indices, not bus numbers: Bus 1L = 1, Bus 1R = 2, Bus 2L = 3, Bus 2R = 4, Bus 4L = 7, Bus 4R = 8, Bus 7L = 13, Bus 7R = 14, Bus 8L = 15, Bus 8R = 16, Bus 9L = 17, Bus 9R = 18.

**Guitar mode switching:** Bus 5 (Electric) and Bus 6 (Acoustic) both feed into Bus 2 (outboard send). Mute Bus 5 for acoustic mode, mute Bus 6 for electric mode. Ch2 sends pre-fader to both buses simultaneously — the muted bus is silenced before it reaches Bus 2.

## Wing FX Pre-Insert Assignments

| FX Slot | Model   | Insert Location    | Purpose |
| ------- | ------- | ------------------ | ------- |
| FX1     | DELUXE  | Bus 5 pre-insert   | Electric guitar amp sim (Fender Deluxe) on Electric bus |
| FX2     | PLATE   | Bus 3 pre-insert   | Shared plate reverb return — Bus 1 and Bus 2 send to Bus 3 |
| FX3     | TAPE    | Bus 9 pre-insert   | Tape saturation on condenser mic recording path only (not outboard send) |
| FX9     | TAPE    | Bus 7 pre-insert   | Tape saturation on vocal recording path only (not outboard send) |
| FX10    | TAPE    | Bus 8 pre-insert   | Tape saturation on guitar recording path only (not outboard send) |
| FX11    | RACKAMP | Bus 6 pre-insert   | Acoustic amp sim (clean/bright: pre 7, buzz 1, punch 2, crunch 1, drive 1, output 8, leq 3, heq 7.5) |

Pre-inserts are assigned at `/ch/N/preins/ins` and `/bus/N/preins/ins`, enabled at `.../preins/on i 1`.

## Signal Chains (Normalled)

**Vocal (outboard):** Mic → Wing LCL/1 → Ch1 (preamp gain, no pre-insert) → Bus 1 send (pre-fader, 0dB) → Wing Out 1 → P1 → HA73 A → P2 → WA76 A → P3 → Opto → P4 → Wing LCL/17 → Ch17 (Vocal Processed)

**Vocal (recording):** Ch1 → Bus 7 send (pre-fader) → FX9/TAPE (Bus 7 pre-insert) → USR/1 (Bus 7L) → USB Out 1 → Loopback → Model 12 Track 1

**Guitar (Electric mode — outboard):** DI → Wing LCL/2 → Ch2 (preamp gain, no pre-insert) → Bus 5 send (pre-fader) → FX1/DELUXE (Bus 5 pre-insert) → Bus 5 → Bus 2 send → Wing Out 2 → P5 → HA73 B → P6 → WA76 B → P7 → Distressor → P8 → Wing LCL/18 → Ch18 (Guitar Processed)

**Guitar (Acoustic mode — outboard):** DI → Wing LCL/2 → Ch2 (preamp gain, no pre-insert) → Bus 6 send (pre-fader) → FX11/RACKAMP (Bus 6 pre-insert) → Bus 6 → Bus 2 send → Wing Out 2 → P5 → HA73 B → P6 → WA76 B → P7 → Distressor → P8 → Wing LCL/18 → Ch18 (Guitar Processed)

**Guitar (recording):** Ch2 → Bus 8 send (pre-fader) → FX10/TAPE (Bus 8 pre-insert) → USR/2 (Bus 8L) → USB Out 2 → Loopback → Model 12 Track 2

**Acoustic Mic path (Ch6 unmuted — outboard):** Condensers → Wing LCL/3+4 → Ch6 (no pre-insert) → Bus 6 send → FX11/RACKAMP (Bus 6 pre-insert) → Bus 6 → Bus 2 → outboard chain

**Acoustic Mic path (recording):** Ch6 → Bus 9 send (pre-fader) → FX3/TAPE (Bus 9 pre-insert) → USR/6 (Bus 9L) + USR/7 (Bus 9R) → USB Out 15/16 → Loopback → Model 12 Tracks 7/8

**Acoustic DI bypass (Ch5):** DI → Ch2 → USR/5 (PRE tap, grp=CH in=2) → Ch5 → Main 1 (clean DI, no outboard; muted by default)

**Shared Reverb:** Ch1/Ch2 → Bus 3 send → FX2/PLATE (Bus 3 pre-insert) → Bus 3 → Main 1

## Outboard Calibration

Calibrated settings for both chains. Do not adjust without retesting.

### Vocal Chain (HA73 A + WA76 A + Opto)

| Unit   | Setting                              | Notes |
| ------ | ------------------------------------ | ----- |
| HA73 A | Input: Line, Output: set for ~0 VU  | Not used as preamp — line-level only |
| HA73 A | EQ: Flat (all bands bypassed)        | Shape with Wing EQ unless analog color is wanted |
| WA76 A | Attack: 3, Release: 7, Ratio: 4:1   | Catching peaks, ~3–4dB GR on transients |
| WA76 A | Input/Output: unity through           | Adjust to match level into Opto |
| Opto   | Peak Reduction: ~40%, Mode: Compress | Smooth leveling, ~2–3dB GR average |
| Opto   | Gain: unity through                   | Ch17 return fader handles monitoring level |

### Guitar Chain (HA73 B + WA76 B + Distressor)

| Unit       | Setting                              | Notes |
| ---------- | ------------------------------------ | ----- |
| HA73 B     | Input: Line, Output: set for ~0 VU  | Not used as preamp — line-level only |
| HA73 B     | EQ: Flat or slight low shelf boost   | Optional warmth/body shaping |
| WA76 B     | Attack: 5, Release: 6, Ratio: 4:1   | Medium attack to let pick transient through |
| Distressor | Ratio: 4:1, Dist 2 (tape) engaged   | Leveling + warm harmonic color |
| Distressor | Attack: 5–6, Release: Auto           | Tracks guitar dynamics naturally |

## Loopback Software Routing

| From                                         | To                                    |
| -------------------------------------------- | ------------------------------------- |
| Wing USB Out 1 (USR/1 — Bus 7L, Vocal+TAPE)  | Model 12 Track 1 (vocal w/ tape)      |
| Wing USB Out 2 (USR/2 — Bus 8L, Guitar+TAPE) | Model 12 Track 2 (guitar w/ tape)     |
| Wing USB Out 15 (USR/6 — Bus 9L, Mic L+TAPE) | Model 12 Track 7 (condenser L w/ tape)|
| Wing USB Out 16 (USR/7 — Bus 9R, Mic R+TAPE) | Model 12 Track 8 (condenser R w/ tape)|
| Wing USB Out 17 (Main 1 L)                   | Model 12 Track 11 (rough mix L)       |
| Wing USB Out 18 (Main 1 R)                   | Model 12 Track 12 (rough mix R)       |
| Model 12 USB Stereo Out L (tracks 11/12 mix) | Wing USB In 3 → Ch13 L (Tape Playback)|
| Model 12 USB Stereo Out R (tracks 11/12 mix) | Wing USB In 4 → Ch13 R (Tape Playback)|

## Monitor / Speaker Routing

Speakers are driven through Matrix 1 (MX1), not directly from Main 1. MX1 sources from the monitor phones output via direct input — this enables solo to work through speakers (the monitor section switches to the solo bus on solo, and MX1 follows).

| Path | Detail |
| ---- | ------ |
| Monitor section (MON.PH) | → MX1 direct input (`/mtx/1/dir/in s "MON.PH"`, `/mtx/1/dir/on i 1`) |
| MX1 | → Wing Out 7 + Wing Out 8 (both sourced from MTX/1) |
| Wing Out 7 + 8 | → Speakers (direct wired, not through patchbay) |

Main 1 → MX1 send is **off**. To mute speakers without affecting headphones: `/mtx/1/mute i 1`.

Valid `dir/in` source values: `MON.SPK` (monitor speaker out), `MON.PH` (monitor phones out — current setting).

## A/B Testing: Hardware vs Plugin

To compare a hardware outboard unit against a Wing plugin emulation fairly, both paths must receive the same clean source and be independently level-matched.

**Key rules:**
- Source channel must have dynamics **OFF** and must **not** be assigned to main
- Plugin goes on a separate channel (not the source) — the pre-fader send tap (`ptap`) is post-dynamics, so a plugin on the source channel would color the hardware signal too
- Use `wingctl meter all` for level matching — adjust faders until outputs are within 0.5dB
- Single-channel meter reads (`wingctl meter /ch/N`) may return stale data; always use `all`

**Example setup (bass → Opto vs Wing LA-2A):**
1. Ch9 (source, Bass): dynamics OFF, sends to Bus 1 pre-fader, NOT assigned to main
2. Ch17 (hardware return): Opto → LCL/17 return, assigned to main
3. Ch19 (plugin): receives same USB/9 source directly, Wing LA-2A enabled, assigned to main
4. Disable Bus 1 → Bus 3 send to prevent reverb bus crosstalk

Solo Ch17 for hardware, solo Ch19 for plugin. Solo works through speakers because MX1 sources from MON.PH (see Monitor / Speaker Routing above).
