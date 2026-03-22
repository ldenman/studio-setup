# Recording Configuration Reference

All gear is permanently wired into the patchbay. Default guitar and vocal chains are normalled and always active. The only connections made at session time are the instruments themselves (guitar into DI, mic into input). Alternative routing requires only a single front-panel patch cable.

## Behringer Wing Rack -- Channel Assignments

| Channel | Name             | Color | Source                            |
| ------- | ---------------- | ----- | --------------------------------- |
| 1       | Vocal Dry        | Blue  | LCL/1 (mic)                       |
| 2       | Guitar Dry       | Red   | LCL/2 (DI)                        |
| 3-8     | Open             |       | Local                             |
| 9       | Bass             | Green | USB/9-10 (Logic, stereo pair)     |
| 10      | Keyboard         | Green | USB/11-12 (Logic, stereo pair)    |
| 11      | Synth/Piano      | Green | USB/13-14 (Logic, stereo pair)    |
| 12      | Drums            | Green | USB/15-16 (Logic, stereo pair)    |
| 13-16   | Open             |       |                                   |
| 17      | Vocal Processed  | Blue  | LCL/17 (outboard return)          |
| 18      | Guitar Processed | Red   | LCL/18 (outboard return)          |
| 19-40   | Open             |       |                                   |

## USB Output Routing (Wing → Loopback → Model 12)

| USB Out | Source                | Model 12 Track            |
| ------- | --------------------- | ------------------------- |
| 1       | USR/1 (Vocal Dry)     | Track 1 (dry vocal)       |
| 2       | USR/2 (Guitar Dry)    | Track 2 (dry guitar)      |
| 17      | Main 1 L              | Track 11 (rough mix L)    |
| 18      | Main 1 R              | Track 12 (rough mix R)    |

USB 1 and 2 record simultaneously — vocal on track 1, guitar on track 2.

## USR Routing (Virtual Patchbay)

| USR | Name       | Source | Tap | Purpose                             |
| --- | ---------- | ------ | --- | ----------------------------------- |
| 1   | Vocal Dry  | Ch1    | PRE | Clean vocal for dry recording via USB |
| 2   | Guitar Dry | Ch2    | PRE | Clean guitar for dry recording via USB |

## Tascam Model 12 -- Track Assignments (per project)

| Track | Source                                     | Format |
| ----- | ------------------------------------------ | ------ |
| 1     | Vocal Dry (Wing USB Out 1 / USR/1)         | Mono   |
| 2     | Guitar Dry (Wing USB Out 2 / USR/2)        | Mono   |
| 3-6   | Open for overdubs / alternate takes        | Mono   |
| 7/8   | Open                                       | Stereo |
| 9/10  | Open                                       | Stereo |
| 11/12 | Rough mix (Main 1 L/R via USB 17/18)       | Stereo |

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

| Point | Top (Output From)           | Bottom (Input To)              | Chain  |
| ----- | --------------------------- | ------------------------------ | ------ |
| 1     | Wing LCL Out 1 (Bus 1)      | HA73 A In                      | Vocal  |
| 2     | HA73 A Out                  | WA76 A In                      | Vocal  |
| 3     | WA76 A Out                  | Opto In                        | Vocal  |
| 4     | Opto Out                    | Wing LCL In 17                 | Vocal  |
| 5     | Wing LCL Out 2 (Bus 2)      | HA73 B In                      | Guitar |
| 6     | HA73 B Out                  | WA76 B In                      | Guitar |
| 7     | WA76 B Out                  | Distressor In                  | Guitar |
| 8     | Distressor Out              | Wing LCL In 18                 | Guitar |
| 9-24  |                             |                                | Open   |

## Bus Layout

| Bus | Name         | Output       | `/io/out/LCL/N/in` index | Purpose |
| --- | ------------ | ------------ | ------------------------ | ------- |
| 1   | Vocal Send   | Wing Out 1   | 1 (Bus 1L)               | Pre-fader send from Ch1 → vocal outboard chain (P1–P4) |
| 2   | Guitar Send  | Wing Out 2   | 3 (Bus 2L)               | Pre-fader send from Ch2 → guitar outboard chain (P5–P8); FX1 (RACKAMP) on pre-insert |
| 3   | Verb Return  | (Main only)  | —                        | Shared reverb bus — receives sends from Bus 1 and Bus 2; FX2 (PLATE) on pre-insert |

Bus output `in` parameter uses stereo channel indices, not bus numbers: Bus 1L = 1, Bus 1R = 2, Bus 2L = 3, Bus 2R = 4, etc.

## Wing FX Pre-Insert Assignments

| FX Slot | Model   | Insert Location    | Purpose |
| ------- | ------- | ------------------ | ------- |
| FX1     | RACKAMP | Bus 2 pre-insert   | Acoustic guitar amp sim on guitar send (pre 7, buzz 2, punch 3, crunch 1, drive 1, output 8, EQ flat, cab on) |
| FX2     | PLATE   | Bus 3 pre-insert   | Shared plate reverb return — Bus 1 and Bus 2 send to Bus 3 |
| FX9     | TAPE    | Ch1 pre-insert     | Tape saturation/warmth on dry vocal before outboard send |
| FX10    | TAPE    | Ch2 pre-insert     | Tape saturation/warmth on dry guitar before outboard send |

Pre-inserts are assigned at `/ch/N/preins/ins` and `/bus/N/preins/ins`, enabled at `.../preins/on i 1`.

## Signal Chains (Normalled)

**Vocal:** Mic → Wing LCL/1 → Ch1 (preamp gain) → FX9/TAPE (pre-insert) → Bus 1 send (pre-fader, 0dB) → Wing Out 1 → P1 → HA73 A → P2 → WA76 A → P3 → Opto → P4 → Wing LCL/17 → Ch17 (Vocal Processed)

**Guitar:** DI → Wing LCL/2 → Ch2 (preamp gain) → FX10/TAPE (pre-insert) → Bus 2 send (pre-fader, 0dB) → FX1/RACKAMP (Bus 2 pre-insert) → Wing Out 2 → P5 → HA73 B → P6 → WA76 B → P7 → Distressor → P8 → Wing LCL/18 → Ch18 (Guitar Processed)

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

| From                              | To                              |
| --------------------------------- | ------------------------------- |
| Wing USB Out 1 (USR/1 Vocal Dry)  | Model 12 Track 1 (dry vocal)    |
| Wing USB Out 2 (USR/2 Guitar Dry) | Model 12 Track 2 (dry guitar)   |
| Wing USB Out 17 (Main 1 L)        | Model 12 Track 11 (rough mix L) |
| Wing USB Out 18 (Main 1 R)        | Model 12 Track 12 (rough mix R) |
| Model 12 stereo out L             | Wing Rack (monitoring L)        |
| Model 12 stereo out R             | Wing Rack (monitoring R)        |

Note: USB 1 and 2 record simultaneously — vocal to track 1, guitar to track 2.

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
