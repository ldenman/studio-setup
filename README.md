# Lake's Studio

## Design Philosophy

**Zero friction.** The studio should be ready to record at all times. Every piece of outboard gear is permanently wired into the patchbay. Default signal chains for guitar and vocals are normalled and always active. The only thing that ever needs to be plugged in is the instrument itself — guitar into the DI, mic into the input. No setup, no patching, no configuration. Sit down and record.

When an alternative routing is needed (e.g. swapping a compressor), a single front-panel patchbay cable is all it takes — no rewiring behind the rack.

**Everything through the patchbay or Loopback.** No direct cable runs between gear. Every analog connection goes through the patchbay — that's the single point of flexibility. Every digital audio connection between apps goes through Loopback software. This means routing changes happen in one place (front of the patchbay or Loopback config), never behind the rack.

**Automate everything.** Any configuration that can be pushed to hardware programmatically should be. Channel names, routing, snapshots — if it can be scripted, it should be scripted. This eliminates manual entry errors, makes the setup reproducible, and means a full studio reset is one command away. Scripts live in `scripts/`.

## Studio Goals

The studio is actually two parts: Recording and Mixing

### Recording
Low latency tracking, computer free operation. Simple, modular routing. Everything connected to patchbay. Patchbay stores default configuration through normalled connections, and provides flexibility for alternative routing options. Microphones and DI instruments should be able to patch through any configuration of outboard gear. 

Recording is comprised of "local/real" instruments namely: guitar and vocals, but could also be a miced keyboard, percussion instruments (like a cajon or hang drum), even singing bowls. 

The DAW (Logic Pro) will have virtual studio session players and/or other backing tracks. Session player instruments include bass, keyboard, synth, and drums. These tracks will be routed into the Wing Rack. 

Everything will be recorded DRY into the tascam model 12. 

Monitoring with low latency effects will be available through the wing rack. 

Loopback software will be enlisted to allow connections between the Model 12 and the Behringer Wing Rack without any physical cables (other than the USB cables of course). With this setup, no aggregate device in Mac OS will be necessary. 


### Mixing
This section is still to be determined. There are many mixing options available. I would encourage the most simple setup.

### Mastering
This section is still to be determined. However, the WA76-D2 and the HA76EQX2 can be used to apply master bus compression and EQ.

## Gear

- Behringer Wing Rack (mixer / effects / monitor controller)
- Samson 48-point TRS patchbay
- HA73-EQX2 (Neve 1073 preamp/EQ clone, dual channel)
- WA76-D2 Black (1176 compressor clone, dual channel)
- Distressor (compressor)
- Audioscape Opto (LA-2A compressor clone)
- Tascam Model 12 (multitrack recorder / interface)
- Mac (Logic Pro, Loopback, wing-sync)

## Software

- Mac OS
- Logic Pro (DAW — session players, mixing)
- Wing Edit (remote Wing control)
- wing-sync (custom BPM sync app, ~/src/wing-sync)
- Loopback (virtual audio routing between Wing Rack and Model 12)
- Harrison Mixbus 10

## Plugins

- IK Multimedia MixBox (70+ effect modules — channel strip rack plugin)
- IK Multimedia AmpliTube 5 (guitar/bass amp and effects sim)
- IK Multimedia TONEX (AI tone modeling — amp/cab/pedal capture)
- IK Multimedia T-RackS Tape Machine (Tascam 388 tape emulation)

See `EFFECTS-REFERENCE.md` for a complete catalog of every effect across all hardware and software.

---

## Studio I/O — All Devices

### Behringer Wing Rack

The mixer where everything flows. Low-latency effects processing, always-on operation, computer-free recording capable. OSC controllable at 192.168.2.2:2223.

#### Inputs (Back Panel)

| #   | Connector      | Label         | Status     | Connected To          |
| --- | -------------- | ------------- | ---------- | --------------------- |
| 1   | XLR/TRS combo  | Input 1       | **In use** | Vocal Mic (LCL/1 → Ch1) |
| 2   | XLR/TRS combo  | Input 2       | **In use** | Guitar DI (LCL/2 → Ch2) |
| 3   | XLR/TRS combo  | Input 3       | **In use** | Condenser Mic L (LCL/3 → Ch6 L) |
| 4   | XLR/TRS combo  | Input 4       | **In use** | Condenser Mic R (LCL/4 → Ch6 R) |
| 5   | XLR/TRS combo  | Input 5       | Open       |                       |
| 6   | XLR/TRS combo  | Input 6       | Open       |                       |
| 7   | XLR/TRS combo  | Input 7       | Open       |                       |
| 8   | XLR/TRS combo  | Input 8       | Open       |                       |
| 1-8 | 1/4" TRS       | AUX In 1-8    | **Partial** | AUX 1 → LCL/17 → Ch17 (Vocal Processed, from Patchbay P4); AUX 2 → LCL/18 → Ch18 (Guitar Processed, from Patchbay P8) |

#### Outputs (Back Panel)

| #   | Connector      | Label          | Status     | Connected To          |
| --- | -------------- | -------------- | ---------- | --------------------- |
| 1   | XLR            | Analog Out 1   | **In use** | Patchbay Point 1 top (Bus 1 → HA73 A, vocal chain) |
| 2   | XLR            | Analog Out 2   | **In use** | Patchbay Point 5 top (Bus 2 → HA73 B, guitar chain) |
| 3   | XLR            | Analog Out 3   | **In use** | Patchbay Point 9 top (Bus 4L → Condenser Mic L send) |
| 4   | XLR            | Analog Out 4   | **In use** | Patchbay Point 10 top (Bus 4R → Condenser Mic R send) |
| 5   | XLR            | Analog Out 5   | Open       |                       |
| 6   | XLR            | Analog Out 6   | Open       |                       |
| 7   | XLR            | Analog Out 7   | **In use** | Speakers (L) — sourced from MX1 (monitor phones output) |
| 8   | XLR            | Analog Out 8   | **In use** | Speakers (R) — sourced from MX1 (monitor phones output) |
| L   | XLR            | Main 1 L       | Open       | (not connected to speakers — see Out 7/8) |
| R   | XLR            | Main 1 R       | Open       | (not connected to speakers — see Out 7/8) |
| 1-8 | 1/4" TRS       | AUX Out 1-8    | Open       |                       |

#### Digital / Network (Back Panel)

| Connector      | Label          | Status     | Connected To          |
| -------------- | -------------- | ---------- | --------------------- |
| USB-B          | USB Audio/MIDI | **In use** | Mac (48ch in/out audio + MIDI) |
| USB-A          | USB Playback   | Open       | (USB drive recording/playback) |
| Ethernet       | Network 1      | **In use** | Mac (OSC control, Wing Edit) |
| Ethernet       | Network 2      | Open       | (integrated switch for daisy-chaining) |
| etherCON       | AES50 A        | Open       | (48in/48out per port)  |
| etherCON       | AES50 B        | Open       |                       |
| etherCON       | AES50 C        | Open       |                       |
| 5-pin XLR      | StageConnect   | Open       | (32ch bidirectional)  |
| XLR            | AES/EBU In     | Open       | (stereo digital in)   |
| XLR            | AES/EBU Out    | Open       | (stereo digital out)  |
| 5-pin DIN      | MIDI In        | Open       |                       |
| 5-pin DIN      | MIDI Out       | Open       |                       |
| 1/4" TRS       | GPIO 1         | Open       |                       |
| 1/4" TRS       | GPIO 2         | Open       |                       |
| SD card slot   | SD 1           | Open       | (live recording, up to 64 tracks) |
| SD card slot   | SD 2           | Open       |                       |
| Card slot      | Expansion      | Open       | (ADAT, MADI, Dante, WSG) |

#### Front Panel

| Connector      | Label          | Status     | Connected To          |
| -------------- | -------------- | ---------- | --------------------- |
| 1/4" TRS       | Headphone Out  | **In use** | Headphones            |

---

### HA73-EQX2 (Heritage Audio — Neve 1073 Preamp/EQ Clone)

Dual-channel transformer-balanced preamp and 3-band EQ. Carnhill transformers. Used as the first stage of the outboard chain for both guitar and vocal paths.

| Direction | # | Connector | Label       | Location   | Status     | Connected To          |
| --------- | - | --------- | ----------- | ---------- | ---------- | --------------------- |
| Input     | A | XLR       | Mic In A    | Back       | Open       |                       |
| Input     | A | XLR       | Line In A   | Back       | **In use** | Patchbay Point 1 bottom (from Wing Out 1, Bus 1 — vocal chain) |
| Input     | A | 1/4" TS   | Hi-Z / DI A | Front      | Open       | (instrument DI)       |
| Input     | B | XLR       | Mic In B    | Back       | Open       |                       |
| Input     | B | XLR       | Line In B   | Back       | **In use** | Patchbay Point 5 bottom (from Wing Out 2, Bus 2 — guitar chain) |
| Input     | B | 1/4" TS   | Hi-Z / DI B | Front      | Open       | (instrument DI)       |
| Output    | A | XLR       | Output A    | Back       | **In use** | Patchbay Point 2 top (→ WA76 ch A) |
| Output    | B | XLR       | Output B    | Back       | **In use** | Patchbay Point 6 top (→ WA76 ch B) |

---

### WA76-D2 Black (Warm Audio — 1176 Compressor Clone)

Dual-channel FET compressor with parallel compression (dry/wet knob). CineMag transformers. Three stereo modes: Stereo Linked, Primary/Secondary, Dual-Mono (no external link jack — linking is built-in).

| Direction | # | Connector | Label       | Status     | Connected To          |
| --------- | - | --------- | ----------- | ---------- | --------------------- |
| Input     | A | XLR       | Input A     | **In use** | Patchbay Point 2 bottom (from HA73 A out — vocal chain) |
| Input     | A | 1/4" TRS  | Input A     | Open       |                       |
| Input     | B | XLR       | Input B     | **In use** | Patchbay Point 6 bottom (from HA73 B out — guitar chain) |
| Input     | B | 1/4" TRS  | Input B     | Open       |                       |
| Output    | A | XLR       | Output A    | **In use** | Patchbay Point 3 top (→ Opto in — vocal chain) |
| Output    | A | 1/4" TRS  | Output A    | Open       |                       |
| Output    | B | XLR       | Output B    | **In use** | Patchbay Point 7 top (→ Distressor in — guitar chain) |
| Output    | B | 1/4" TRS  | Output B    | Open       |                       |

---

### Distressor (Empirical Labs — Compressor)

Single-channel compressor. Transformerless balanced I/O. In the default guitar chain (after the WA76 B).

| Direction | # | Connector | Label       | Status     | Connected To          |
| --------- | - | --------- | ----------- | ---------- | --------------------- |
| Input     | 1 | XLR       | Input       | **In use** | Patchbay Point 7 bottom (from WA76 B out — guitar chain) |
| Input     | 1 | 1/4" TRS  | Input       | Open       |                       |
| Output    | 1 | XLR       | Output      | **In use** | Patchbay Point 8 top (→ Wing LCL In 18 → Ch18 Guitar Processed) |
| Output    | 1 | 1/4" TRS  | Output      | Open       |                       |
| Link      |   | 1/4" TRS  | Stereo Link | Open       | (for linking two Distressors) |

---

### Audioscape Opto (LA-2A Compressor Clone)

Single-channel optical compressor. Electronically balanced +4dBu. In the default vocal chain (after the WA76 A).

| Direction | # | Connector | Label       | Status     | Connected To          |
| --------- | - | --------- | ----------- | ---------- | --------------------- |
| Input     | 1 | XLR       | Input       | **In use** | Patchbay Point 3 bottom (from WA76 A out — vocal chain) |
| Output    | 1 | XLR       | Output      | **In use** | Patchbay Point 4 top (→ Wing LCL In 17 → Ch17 Vocal Processed) |
| Link      |   | 1/4" TRS  | Stereo Link | Open       | (for linking two units) |

---

### Samson 48-Point TRS Patchbay

24 normalled pairs (top = output, bottom = input). 1/4" TRS front and back. Signal flows top → bottom when no cable is inserted (normalled). Inserting a cable on the front breaks the normal.

| Point | Back Top (Output From)      | Back Bottom (Input To)          | Status     |
| ----- | --------------------------- | ------------------------------- | ---------- |
| 1     | Wing LCL Out 1 (Bus 1)      | HA73 A Line In                  | **Normalled** — Vocal chain |
| 2     | HA73 A Output               | WA76 A Input                    | **Normalled** — Vocal chain |
| 3     | WA76 A Output               | Audioscape Opto Input           | **Normalled** — Vocal chain |
| 4     | Audioscape Opto Output      | Wing LCL In 17 (→ Ch17)        | **Normalled** — Vocal chain |
| 5     | Wing LCL Out 2 (Bus 2)      | HA73 B Line In                  | **Normalled** — Guitar chain |
| 6     | HA73 B Output               | WA76 B Input                    | **Normalled** — Guitar chain |
| 7     | WA76 B Output               | Distressor Input                | **Normalled** — Guitar chain |
| 8     | Distressor Output           | Wing LCL In 18 (→ Ch18)        | **Normalled** — Guitar chain |
| 9     | Wing LCL Out 3 (Bus 4L)     | Condenser Mic L                 | **Normalled** — Acoustic mic send L |
| 10    | Wing LCL Out 4 (Bus 4R)     | Condenser Mic R                 | **Normalled** — Acoustic mic send R |
| 11-24 |                             |                                 | Open        |

---

### Tascam Model 12 (Multitrack Recorder)

Digital tape machine, mixer, and USB audio interface. 12-in/10-out USB interface. In this studio, audio is routed to/from the Model 12 via Loopback software over USB — no physical audio cables. Physical I/O is available but unused. +48V phantom power available on all mic inputs.

#### Physical Audio I/O (All Unused — Audio Routed via USB/Loopback)

| Direction | #    | Connector      | Label              | Notes | Status |
| --------- | ---- | -------------- | ------------------ | ----- | ------ |
| Input     | 1    | XLR/TRS combo  | Ch 1               | Mic/Line/Hi-Z, insert point | Open |
| Input     | 2    | XLR/TRS combo  | Ch 2               | Mic/Line/Hi-Z, insert point | Open |
| Input     | 3    | XLR/TRS combo  | Ch 3               | Mic/Line/Hi-Z | Open |
| Input     | 4    | XLR/TRS combo  | Ch 4               | Mic/Line/Hi-Z | Open |
| Input     | 5    | XLR/TRS combo  | Ch 5               | Mic/Line/Hi-Z | Open |
| Input     | 6    | XLR/TRS combo  | Ch 6               | Mic/Line/Hi-Z | Open |
| Input     | 7/8  | XLR/TRS combo  | Ch 7/8 (stereo)    | Mic/Line/Hi-Z (7, 9 only) | Open |
| Input     | 9/10 | XLR/TRS combo  | Ch 9/10 (stereo)   | Mic/Line/Hi-Z (7, 9 only) | Open |
| Input     | 9/10 | 3.5mm TRRS     | Smartphone In      | Routes to ch 9/10 | Open |
| Insert    | 1    | 1/4" TRS       | Insert 1           | Send/return on single jack | Open |
| Insert    | 2    | 1/4" TRS       | Insert 2           | Send/return on single jack | Open |
| Output    | L/R  | XLR            | Main Out L/R       | Balanced | Open |
| Output    | L/R  | 1/4" TRS       | Sub Out L/R        | Balanced | Open |
| Output    | 1/2  | 1/4" TRS       | AUX Send 1/2       | Mono, pre/post selectable | Open |
| Output    |      | 1/4" jack      | Click Out          | Metronome feed | Open |
| Output    | A    | 1/4" TRS       | Headphone A        | Front panel | Open |
| Output    | B    | 1/4" TRS       | Headphone B        | Front panel | Open |

#### Digital / Control

| Connector      | Label          | Status     | Connected To          |
| -------------- | -------------- | ---------- | --------------------- |
| USB-C          | USB Audio      | **In use** | Mac (12-in/10-out audio interface) |
| SD card slot   | Multitrack Rec | **In use** | SD card (WAV, 44.1/48kHz, 16/24-bit) |
| 5-pin DIN      | MIDI In        | Open       |                       |
| 5-pin DIN      | MIDI Out       | Open       | (sends MIDI Time Code + Clock) |
| 1/4" TRS       | Footswitch     | Open       | (remote transport control) |
| Bluetooth 5.0  | BT Audio In    | Open       | (playback to ch 9/10) |

#### Track Assignments (per project, via USB/Loopback)

| Track | Source                                              | Format  |
| ----- | --------------------------------------------------- | ------- |
| 1     | Vocal + TAPE (USB Out 1 / USR/1 / Bus 7)            | Mono    |
| 2     | Guitar + TAPE (USB Out 2 / USR/2 / Bus 8)           | Mono    |
| 3-6   | Open for overdubs / alternate takes                 | Mono    |
| 7/8   | Condenser mics + TAPE (USB Out 15/16 / USR/6+7 / Bus 9) | Stereo  |
| 9/10  | Open                                                | Stereo  |
| 11/12 | Rough mix (Wing USB Out 17/18, Main L/R)            | Stereo (always recording) |

---

### Mac (Computer)

| Connector      | Connected To        | Purpose                    |
| -------------- | ------------------- | -------------------------- |
| USB            | Wing Rack           | 48ch audio + control       |
| USB            | Model 12            | Multitrack recording       |
| Ethernet       | Wing Rack           | OSC control, Wing Edit     |

#### Software Audio Routing (Loopback)

| From                                                  | To                                    |
| ----------------------------------------------------- | ------------------------------------- |
| Wing USB Out 1 (USR/1 — Bus 7L, Vocal + TAPE)         | Model 12 Track 1 (vocal w/ tape)      |
| Wing USB Out 2 (USR/2 — Bus 8L, Guitar + TAPE)        | Model 12 Track 2 (guitar w/ tape)     |
| Wing USB Out 15 (USR/6 — Bus 9L, Condenser L + TAPE)  | Model 12 Track 7 (condenser L w/ tape)|
| Wing USB Out 16 (USR/7 — Bus 9R, Condenser R + TAPE)  | Model 12 Track 8 (condenser R w/ tape)|
| Wing USB Out 17 (Main 1 L)                            | Model 12 Track 11 (rough mix L)       |
| Wing USB Out 18 (Main 1 R)                            | Model 12 Track 12 (rough mix R)       |
| Model 12 USB Stereo Out L                             | Wing Rack USB (Monitoring L)          |
| Model 12 USB Stereo Out R                             | Wing Rack USB (Monitoring R)          |

---

## Signal Chains (Default/Normalled)

**Vocal (outboard):** Mic → Wing LCL/1 (ch1 dry, preamp gain) → Bus 1 → Wing Out 1 → P1 → HA73 A → P2 → WA76 A → P3 → Opto → P4 → Wing LCL/17 → Ch17 (Vocal Processed)

**Vocal (recording):** Ch1 → Bus 7 → FX9/TAPE (Bus 7 pre-insert) → USR/1 → USB Out 1 → Model 12 Track 1

**Guitar (Electric, outboard):** DI → Wing LCL/2 (ch2 dry, preamp gain) → Bus 5 → FX1/DELUXE (Bus 5 pre-insert) → Bus 2 → Wing Out 2 → P5 → HA73 B → P6 → WA76 B → P7 → Distressor → P8 → Wing LCL/18 → Ch18 (Guitar Processed)

**Guitar (Acoustic, outboard):** DI → Wing LCL/2 (ch2 dry, preamp gain) → Bus 6 → FX11/RACKAMP (Bus 6 pre-insert) → Bus 2 → Wing Out 2 → P5 → HA73 B → P6 → WA76 B → P7 → Distressor → P8 → Wing LCL/18 → Ch18 (Guitar Processed)

**Guitar (recording):** Ch2 → Bus 8 → FX10/TAPE (Bus 8 pre-insert) → USR/2 → USB Out 2 → Model 12 Track 2

**Acoustic Mics (outboard):** Condensers → Wing LCL/3+4 → Ch6 → Bus 6 → FX11/RACKAMP → Bus 2 → outboard chain (above)

**Acoustic Mics (recording):** Ch6 → Bus 9 → FX3/TAPE (Bus 9 pre-insert) → USR/6+7 → USB Out 15/16 → Model 12 Tracks 7/8

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
Digital tape machine — 12 tracks (1-6 mono, 7/8 and 9/10 stereo, 11/12 main L/R always recording). Connected via USB, audio routed through Loopback software. Records everything DRY.

### Behringer Wing Rack (Creative Uses)
Beyond mixing: snapshots for song recall, built-in FX for sound design, channel strip emulations (Neve, SSL, Vintage), guitar amp sims, OSC automation.

