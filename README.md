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
| 1   | XLR/TRS combo  | Input 1       | **In use** | Guitar DI             |
| 2   | XLR/TRS combo  | Input 2       | **In use** | Patchbay return (Guitar Processed) |
| 3   | XLR/TRS combo  | Input 3       | **In use** | Vocal Mic             |
| 4   | XLR/TRS combo  | Input 4       | **In use** | Patchbay return (Vocal Processed) |
| 5   | XLR/TRS combo  | Input 5       | Open       |                       |
| 6   | XLR/TRS combo  | Input 6       | Open       |                       |
| 7   | XLR/TRS combo  | Input 7       | Open       |                       |
| 8   | XLR/TRS combo  | Input 8       | Open       |                       |
| 1-8 | 1/4" TRS       | AUX In 1-8    | Open       |                       |

#### Outputs (Back Panel)

| #   | Connector      | Label          | Status     | Connected To          |
| --- | -------------- | -------------- | ---------- | --------------------- |
| 1   | XLR            | Analog Out 1   | **In use** | Patchbay Point 1 top (→ HA73 ch1) |
| 2   | XLR            | Analog Out 2   | **In use** | Patchbay Point 4 top (→ HA73 ch2) |
| 3   | XLR            | Analog Out 3   | Open       |                       |
| 4   | XLR            | Analog Out 4   | Open       |                       |
| 5   | XLR            | Analog Out 5   | Open       |                       |
| 6   | XLR            | Analog Out 6   | Open       |                       |
| 7   | XLR            | Analog Out 7   | Open       |                       |
| 8   | XLR            | Analog Out 8   | Open       |                       |
| L   | XLR            | Main 1 L       | **In use** | Speakers (L)          |
| R   | XLR            | Main 1 R       | **In use** | Speakers (R)          |
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
| Input     | 1 | XLR       | Mic In 1    | Back       | Open       |                       |
| Input     | 1 | XLR       | Line In 1   | Back       | **In use** | Patchbay Point 1 bottom (from Wing Out 1) |
| Input     | 1 | 1/4" TS   | Hi-Z / DI 1 | Front      | Open       | (instrument DI)       |
| Input     | 2 | XLR       | Mic In 2    | Back       | Open       |                       |
| Input     | 2 | XLR       | Line In 2   | Back       | **In use** | Patchbay Point 4 bottom (from Wing Out 2) |
| Input     | 2 | 1/4" TS   | Hi-Z / DI 2 | Front      | Open       | (instrument DI)       |
| Output    | 1 | XLR       | Output 1    | Back       | **In use** | Patchbay Point 2 top (→ 1176 ch1) |
| Output    | 2 | XLR       | Output 2    | Back       | **In use** | Patchbay Point 5 top (→ 1176 ch2) |

---

### WA76-D2 Black (Warm Audio — 1176 Compressor Clone)

Dual-channel FET compressor with parallel compression (dry/wet knob). CineMag transformers. Three stereo modes: Stereo Linked, Primary/Secondary, Dual-Mono (no external link jack — linking is built-in).

| Direction | # | Connector | Label       | Status     | Connected To          |
| --------- | - | --------- | ----------- | ---------- | --------------------- |
| Input     | 1 | XLR       | Input 1     | **In use** | Patchbay Point 2 bottom (from HA73 ch1) |
| Input     | 1 | 1/4" TRS  | Input 1     | Open       |                       |
| Input     | 2 | XLR       | Input 2     | **In use** | Patchbay Point 5 bottom (from HA73 ch2) |
| Input     | 2 | 1/4" TRS  | Input 2     | Open       |                       |
| Output    | 1 | XLR       | Output 1    | **In use** | Patchbay Point 3 top (→ Wing ch2) |
| Output    | 1 | 1/4" TRS  | Output 1    | Open       |                       |
| Output    | 2 | XLR       | Output 2    | **In use** | Patchbay Point 6 top (→ Opto) |
| Output    | 2 | 1/4" TRS  | Output 2    | Open       |                       |

---

### Distressor (Empirical Labs — Compressor)

Single-channel compressor. Transformerless balanced I/O. Not in the default normalled chain — patch in via patchbay when needed.

| Direction | # | Connector | Label       | Status     | Connected To          |
| --------- | - | --------- | ----------- | ---------- | --------------------- |
| Input     | 1 | XLR       | Input       | Open       | (patch via patchbay)  |
| Input     | 1 | 1/4" TRS  | Input       | Open       |                       |
| Output    | 1 | XLR       | Output      | Open       | (patch via patchbay)  |
| Output    | 1 | 1/4" TRS  | Output      | Open       |                       |
| Link      |   | 1/4" TRS  | Stereo Link | Open       | (for linking two Distressors) |

---

### Audioscape Opto (LA-2A Compressor Clone)

Single-channel optical compressor. Electronically balanced +4dBu. Part of the default vocal chain (after the 1176).

| Direction | # | Connector | Label       | Status     | Connected To          |
| --------- | - | --------- | ----------- | ---------- | --------------------- |
| Input     | 1 | XLR       | Input       | **In use** | Patchbay Point 6 bottom (from 1176 ch2) |
| Output    | 1 | XLR       | Output      | **In use** | Patchbay Point 7 top (→ Wing ch4 in) |
| Link      |   | 1/4" TRS  | Stereo Link | Open       | (for linking two units) |

---

### Samson 48-Point TRS Patchbay

24 normalled pairs (top = output, bottom = input). 1/4" TRS front and back. Signal flows top → bottom when no cable is inserted (normalled). Inserting a cable on the front breaks the normal.

| Point | Back Top (Output From)      | Back Bottom (Input To)     | Status     |
| ----- | --------------------------- | -------------------------- | ---------- |
| 1     | Wing Rack Analog Out 1      | HA73 Channel 1 Line In     | **Normalled** — Guitar chain |
| 2     | HA73 Channel 1 Output       | 1176 Channel 1 Input       | **Normalled** — Guitar chain |
| 3     | 1176 Channel 1 Output       | Wing Rack Input 2          | **Normalled** — Guitar chain |
| 4     | Wing Rack Analog Out 2      | HA73 Channel 2 Line In     | **Normalled** — Vocal chain |
| 5     | HA73 Channel 2 Output       | 1176 Channel 2 Input       | **Normalled** — Vocal chain |
| 6     | 1176 Channel 2 Output       | Audioscape Opto Input      | **Normalled** — Vocal chain |
| 7     | Audioscape Opto Output      | Wing Rack Input 4          | **Normalled** — Vocal chain |
| 8-24  |                             |                            | Open        |

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

#### Track Assignments (via Loopback Software)

| Track | Source              | Format  |
| ----- | ------------------- | ------- |
| 1     | Guitar Dry (Wing ch1) | Mono  |
| 2     | Vocal Dry (Wing ch3)  | Mono  |
| 3     | Bass (Wing ch9)       | Mono  |
| 4     | Keyboard (Wing ch10)  | Mono  |
| 5     |                       | Mono  |
| 6     |                       | Mono  |
| 7/8   | Synth/Piano (Wing ch11/12) | Stereo |
| 9/10  | Drums (Wing ch13/14)  | Stereo |
| 11/12 | Main L/R              | Stereo (always recording) |

---

### Mac (Computer)

| Connector      | Connected To        | Purpose                    |
| -------------- | ------------------- | -------------------------- |
| USB            | Wing Rack           | 48ch audio + control       |
| USB            | Model 12            | Multitrack recording       |
| Ethernet       | Wing Rack           | OSC control, Wing Edit     |

#### Software Audio Routing (Loopback)

| From                              | To                            |
| --------------------------------- | ----------------------------- |
| Wing Rack USB ch1 (Guitar Dry)    | Model 12 USB Track 1          |
| Wing Rack USB ch3 (Vocal Dry)     | Model 12 USB Track 2          |
| Wing Rack USB ch9 (Bass)          | Model 12 USB Track 3          |
| Wing Rack USB ch10 (Keyboard)     | Model 12 USB Track 4          |
| Wing Rack USB ch11/12 (Synth/Piano) | Model 12 USB Track 7/8      |
| Wing Rack USB ch13/14 (Drums)     | Model 12 USB Track 9/10       |
| Model 12 USB Stereo Out L         | Wing Rack USB (Monitoring L)  |
| Model 12 USB Stereo Out R         | Wing Rack USB (Monitoring R)  |

---

## Signal Chains (Default/Normalled)

**Guitar:** DI → Wing In 1 (ch1 dry) → Bus 1 → Analog Out 1 → Patchbay 1 → HA73 ch1 → Patchbay 2 → 1176 ch1 → Patchbay 3 → Wing In 2 (ch2 processed)

**Vocal:** Mic → Wing In 3 (ch3 dry) → Bus 2 → Analog Out 2 → Patchbay 4 → HA73 ch2 → Patchbay 5 → 1176 ch2 → Patchbay 6 → Opto → Patchbay 7 → Wing In 4 (ch4 processed)

## Gear Notes

### HA73-EQX2
Neve 1073 clone, dual channel. Transistor preamp with 3-band EQ. Guitar and vocals run through this first, then into the compressors. In mixing, can be used standalone as an EQ. In mastering, dual channels for stereo bus EQ.

### WA76-D2
1176 clone, dual channel FET compressor. DRY/WET knob for parallel compression. In recording, tames transient peaks. In mastering, dual channels for stereo bus compression.

### Distressor
Single-channel compressor. Not in the default chain — available via patchbay. General purpose, works on anything.

### Audioscape Opto
LA-2A clone. Optical compressor. Smooth, musical compression. In the default vocal chain after the 1176. Great for vocals and bass guitar.

### Tascam Model 12
Digital tape machine — 12 tracks (1-6 mono, 7/8 and 9/10 stereo, 11/12 main L/R always recording). Connected via USB, audio routed through Loopback software. Records everything DRY.

### Behringer Wing Rack (Creative Uses)
Beyond mixing: snapshots for song recall, built-in FX for sound design, channel strip emulations (Neve, SSL, Vintage), guitar amp sims, OSC automation.

