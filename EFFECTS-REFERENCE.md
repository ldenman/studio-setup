# Effects & Plugins Reference

Complete catalog of every effect available in the studio — hardware (Wing Rack, outboard) and software (IK Multimedia plugins). Use this when designing signal chains, choosing FX for a session, or looking up parameters.

---

## Behringer Wing Rack — Built-in Effects

### Channel Plugins

These replace the default processing on each channel section. Set via `/ch/N/eq/mdl`, `/ch/N/dyn/mdl`, `/ch/N/gate/mdl`, `/ch/N/flt/mdl`. No FX slot required — they run directly on the channel.

#### Filter Plugins (`/ch/N/flt/mdl`)

| Model | Name           | Based On       | Key Parameters |
| ----- | -------------- | -------------- | -------------- |
| TILT  | Tilt EQ        | —              | tilt [-6..6] |
| MAXER | Sound Maxer    | —              | low contour, high process |
| AP1   | All-Pass 90°   | —              | freq |
| AP2   | All-Pass 180°  | —              | freq, Q |

#### EQ Plugins (`/ch/N/eq/mdl`)

| Model  | Name               | Based On            | Bands | Key Parameters |
| ------ | ------------------ | ------------------- | ----- | -------------- |
| STD    | Wing Standard EQ   | —                   | 4 + shelves | Full parametric, SHV/PEQ select |
| SOUL   | Soul Analogue      | SSL 4000 E          | 4 (LF/LM/HM/HF) | Fixed-point freqs, x3 multiplier |
| E88    | Even 88 Formant    | Neve 1088           | 4 (LF/LM/HM/HF) | Bell/shelf select, Q per band |
| E84    | Even 84            | Neve 1084           | 3 (LF/MF/HF) | Fixed freq selectors (35/60/110/220 etc.) |
| F110   | Fortissimo 110     | Focusrite ISA 110   | 2 para + shelves | PEQ on/off, gain trim |
| PULSAR | Pulsar P1a/M5      | Pultec EQP-1A/MEQ-5 | 2 sections | Boost + atten per section, fixed freqs |
| MACH4  | Mach EQ4           | Manley Massive Passive | 5 fixed | sub, 40, 160, 650, 2k5, air, auto gain |

All EQ plugins have a **mix** control (0-125%) for parallel EQ blending.

#### Gate Plugins (`/ch/N/gate/mdl`)

| Model | Name               | Based On               | Key Parameters |
| ----- | ------------------ | ---------------------- | -------------- |
| GATE  | Standard Gate      | —                      | thr, ratio, att, hld, rel, sidechain filter |
| DUCK  | Standard Ducker    | —                      | thr, range, att, hold, rel |
| E88   | Even 88 Gate       | Neve 1088 Gate         | thr, hysteresis, range, rel, fast |
| 9000G | Soul 9000 Gate     | SSL 9000 Gate          | thr, range, hold, rel, fast, gate/exp mode |
| D241G | DrawMore 241       | Drawmer 241            | thr, slow mode |
| DS902 | BDX 902 DeEsser    | DBX 902               | freq, range, full/HF mode |
| DEQ   | Dynamic EQ         | —                      | thr, ratio, att, rel, filter, freq, Q |
| WAVE  | Wave Designer      | SPL Transient Designer | attack, sustain, gain |
| WARM  | Soul Warmth Pre    | —                      | drive, harmonics, color, trim |
| 76LA  | 76 Limiter Amp     | UREI 1176              | in, out, att, rel, ratio (4/8/12/20/ALL) |
| LA    | Leveling Amp 2A    | Teletronix LA-2A       | gain, peak, comp/lim mode |
| RIDE  | Auto Rider         | —                      | thr, target, speed, ratio, hold, range |

#### Dynamics Plugins (`/ch/N/dyn/mdl`)

| Model | Name               | Based On               | Key Parameters |
| ----- | ------------------ | ---------------------- | -------------- |
| COMP  | Wing Compressor    | —                      | thr, ratio, knee, det, att, hld, rel, env, auto |
| EXP   | Wing Expander      | —                      | thr, ratio, knee, det, att, hld, rel, env, auto |
| B160  | BDX 160            | DBX 160                | thr, ratio |
| B560  | BDX 560 Easy       | DBX 560A               | thr, ratio, auto |
| D241C | DrawMore Comp      | Drawmer 241            | thr, ratio, att, rel, lim thr, lim rel, auto |
| ECL33 | Even Comp/Limiter  | Neve 33609             | Separate comp (thr/ratio/rec/fast) + lim (thr/rec/fast) |
| 9000C | Soul 9000 Channel  | SSL 9000 Channel       | thr, ratio, fast att, rel, peak |
| SBUS  | Soul G Bus Comp    | SSL G Bus Comp         | thr, ratio (1.5-10), att (0.1-30ms), rel (0.1-AUTO) |
| RED3  | Red 3 Compressor   | Focusrite Red 3        | thr, ratio, att, rel, auto |
| 76LA  | 76 Limiter Amp     | UREI 1176              | in, out, att, rel, ratio (4/8/12/20/ALL) |
| LA    | Leveling Amp 2A    | Teletronix LA-2A       | gain, peak, comp/lim mode |
| F670  | Fairkid 670        | Fairchild 670          | in, thr, time (1-6), bias |
| BLISS | Eternal Bliss      | Elysia mPressor        | thr, ratio, att, rel, auto fast, anti-log, GR limit |
| NSTR  | No Stressor        | Empirical Labs Distressor | in, out, att, rel, ratio (1.5:1 to NUKE) |
| WAVE  | Wave Designer      | SPL Transient Designer | att, sustain, gain |
| RIDE  | Auto Rider         | —                      | thr, target, speed, ratio, hold, range |

All dynamics plugins have a **mix** control (0-100%) for parallel compression.

---

### FX Slot Effects

Loaded into FX slots 1-16 via `/fx/N/mdl`. Slots 1-8 are premium (reverbs, delays). Slots 9-16 are standard (utilities, EQ, amps). Premium slots can run standard effects too.

#### Reverbs (Premium Slots)

| Model    | Name              | Character     | Key Parameters |
| -------- | ----------------- | ------------- | -------------- |
| HALL     | Hall Reverb       | Large, lush   | pdel, size, dcy, mult, damp, lc, hc, shp, sprd, diff, mspd |
| ROOM     | Room Reverb       | Natural room  | pdel, size, dcy, mult, damp, lc, hc, shp, sprd, diff, spin, ecl, ecr |
| CHAMBER  | Chamber Reverb    | Tight, focused | pdel, size, dcy, mult, damp, lc, hc, shp, sprd, diff, spin |
| PLATE    | Plate Reverb      | Bright, smooth | pdel, size, dcy, mult, damp, lc, hc, att, sprd, diff, spin |
| CONCERT  | Concert Reverb    | Grand, spacious | pdel, size, dcy, mult, damp, lc, hc, shp, sprd, diff, depth, spin, crs |
| AMBI     | Ambience          | Subtle, short | pdel, size, dcy, tail, damp, diff, mod, lc, hc |
| V-ROOM   | Vintage Room/VSS3 | TC Electronic | pdel, size, dcy, dens, erlvl, lmult, hmult, lc, hc, frz |
| V-REV    | Vintage Reverb    | Lexicon-style | pdel, dcy, lmult, hmult, mod, lc, hc, out (FRONT/REAR), trans |
| V-PLATE  | Vintage Plate     | Classic plate | pdel, dcy, lc, col |
| GATED    | Gated Reverb      | 80s gated     | pdel, att, dcy, dens, diff, sprd, lc, hfs, hsg |
| REVERSE  | Reverse Reverb    | Reversed tail | pdel, rise, dcy, diff, sprd, lc, hfs, hsg |
| SHIMMER  | Shimmer Reverb    | Ethereal      | pdel, size, dcy, lc, hc, damp, shim, shine |
| SPRING   | Spring Reverb     | Surf, vintage | dcy, dens, low, high |
| DEL/REV  | Delay/Reverb      | Combined      | time, feed, dly, d2r, pdel, size, dcy, damp, i2r |

#### Delays (Premium Slots)

| Model    | Name              | Character     | Key Parameters |
| -------- | ----------------- | ------------- | -------------- |
| ST-DL    | Stereo Delay      | Clean, precise | time (1-3000ms), mode (ST/X/M), fact, pat, offset, feed, lc, hc |
| TAP-DL   | Ultratap Delay    | Multi-tap     | time (1-2000ms), rep (1-16), slp, fact, pdel, mode, wid, diff |
| TAPE-DL  | Tape Delay        | Warm, saturated | time (60-650ms), sust, drv, flutter |
| OILCAN   | Oil Can Delay     | Vintage warble | time (seconds), sust, wobble, tone |
| BBD-DL   | BBD Delay         | Analog bucket | dly, feed |

#### Modulation (Premium Slots)

| Model    | Name              | Key Parameters |
| -------- | ----------------- | -------------- |
| DIMCRS   | Dimension CRS     | sw1-sw4 (button matrix), input (MONO/STEREO), dry |
| CHORUS   | Stereo Chorus     | lc, hc, wave, phase, mix, dlyl, dlyr, depl, depr, sprd, spd |
| FLANGER  | Stereo Flanger    | lc, hc, flc, fhc, mix, dlyl, dlyr, depl, depr, phase, spd, feed |

#### Pitch (Premium Slots)

| Model    | Name              | Key Parameters |
| -------- | ----------------- | -------------- |
| PITCH    | Stereo Pitch      | semi (-12..12), cent (-50..50), dly, lc, hc, mix |
| D-PITCH  | Dual Pitch        | semi1/2, cent1/2, dly1/2, pan1/2, lvl1/2, lc, hc |

#### EQ / Utilities (Standard Slots)

| Model    | Name              | Key Parameters |
| -------- | ----------------- | -------------- |
| GEQ      | 31-Band Graphic EQ | type (STD/TRU), 31 bands 20Hz-20kHz |
| PIA      | PIA 560 GEQ       | mix, gain, 10 bands (31Hz-16kHz) |
| C5-CMB   | 5-Band Combinator  | 5-band multiband comp, per-band thr/gain/bypass/crossover |
| LIMITER  | Precision Limiter  | gin, gout, squeeze, knee, att, rel |
| DE-S2    | 2-Band DeEsser     | lo, hi, gender, mode |
| ENHANCE  | Ultra Enhancer     | stereo level, mono level, bass/mid/high gain |
| EXCITER  | Exciter            | tune, peak, zfill, timbre, harmonics, mix |
| P-BASS   | Psycho Bass        | intensity, bass, crossover freq |
| BODY     | Bodyrez            | body |
| SUB      | Sub Octaver        | range (LOW/MID/HIGH), oct1, oct2 |
| PCORR    | Pitch Fix          | speed, amount, A4 tuning, per-note on/off |
| DOUBLE   | Vocal Doubler      | mode (TIGHT/LOOSE/GROUP/DETUNE/THICK), mix, spread |
| TAPE     | Tape Machine       | drive, speed, low bump, high shelf, output |
| MOOD     | Mood Filter        | base freq, type (LP/HP/BP/NOTCH), slope, reso, drive, env, LFO |
| ROTARY   | Rotary Speaker     | switch (STOP/SLOW/FAST), lo/hi speed, balance, mix, dist |
| PHASER   | Phaser             | speed, phase, wave, range, depth, env mod, stages, reso |
| PANNER   | Tremolo/Panner     | speed, phase, wave, depth, envelope mod |

#### Guitar Amps (Standard Slots)

| Model    | Name              | Character     |
| -------- | ----------------- | ------------- |
| RACKAMP  | Rack Amp          | Preamp sim — pre, buzz, punch, crunch, drive, cab sim |
| UKROCK   | UK Rock Amp       | Marshall-style — gain, bass, mid, treb, presence, sag, cab sim |
| ANGEL    | Angel Amp         | Mesa-style — gain, bass, mid, treb, presence, mid boost, bright, cab sim |
| JAZZC    | Jazz Clean Amp    | Fender-style — vol, bass, mid, treb, bright, cab sim |
| DELUXE   | Deluxe Amp        | Fender Deluxe — vol, bass, treb, sag, cab sim |

#### Channel Strip FX (Standard Slots)

Full console emulations with gate + EQ + compressor in one unit. Each instance uses one FX slot. Load via `/fx/N/mdl`.

| Model      | Name               | Based On                |
| ---------- | ------------------ | ----------------------- |
| \*EVEN\*   | Even Channel       | Neve console strip      |
| \*SOUL\*   | Soul Channel       | SSL console strip       |
| \*VINTAGE\*| Vintage Channel    | Vintage console strip   |
| \*BUS\*    | Bus Channel        | Bus compressor channel  |
| \*MASTER\* | Master Channel     | Mastering strip         |

**Usage:** Load into FX slot → insert on channel via `/ch/N/postins/ins s "FXn"` → enable → set wet/dry to 100%. Each channel needs its own FX slot instance.

#### Other (Standard Slots)

| Model    | Name              |
| -------- | ----------------- |
| NONE     | Empty slot        |
| EXT      | External I/O      |
| SOUL     | Soul Analogue (as FX insert) |
| E88      | Even 88 (as FX insert) |
| E84      | Even 84 (as FX insert) |
| F110     | Fortissimo 110 (as FX insert) |
| PULSAR   | Pulsar (as FX insert) |
| MACH4    | Mach EQ4 (as FX insert) |

---

## Outboard Hardware Effects

Physical processors patched via the Samson patchbay.

### HA73-EQX2 (Neve 1073 Clone)

| Section   | Controls                                    |
| --------- | ------------------------------------------- |
| Preamp    | Gain, impedance select, phantom power, polarity, Hi-Z DI (front) |
| EQ Band 1 | Low shelf: 35/60/110/220 Hz, ±16dB          |
| EQ Band 2 | Mid peak: 360/700/1.6k/3.2k/4.8k/7.2k Hz, ±16dB, Q |
| EQ Band 3 | High shelf: 10k/12k/16k Hz, ±16dB           |
| HPF       | 50/80/160/300 Hz, 18dB/oct                   |

**Best for:** First-stage coloration, adding warmth and harmonics. Transformer saturation at higher gain. Pairs naturally with the 1176 after it.

### WA76-D2 (1176 Clone)

| Control    | Range / Notes                               |
| ---------- | ------------------------------------------- |
| Input      | Controls compression amount (higher = more) |
| Output     | Makeup gain                                 |
| Attack     | 20μs to 800μs (fast to slow — reversed knob) |
| Release    | 50ms to 1.1s (fast to slow — reversed knob) |
| Ratio      | 4:1, 8:1, 12:1, 20:1, ALL (all-buttons mode) |
| Dry/Wet    | Parallel compression blend                  |
| Meter      | GR or Output                                |
| Stereo Mode | Stereo Linked, Primary/Secondary, Dual Mono |

**Best for:** Fast transient control, aggressive compression, parallel smash (ALL buttons mode + dry/wet). Guitar and vocals in the default chain.

### Distressor (Empirical Labs EL8)

| Control    | Range / Notes                               |
| ---------- | ------------------------------------------- |
| Input      | Threshold (lower = more compression)        |
| Output     | Makeup gain                                 |
| Attack     | 0.1ms to 20ms                               |
| Release    | 50ms to 2.5s                                |
| Ratio      | 1:1, 2:1, 3:1, 4:1, 6:1, 10:1, 20:1, NUKE |
| Detector   | HP filter for sidechain                     |
| Dist 2     | 2nd harmonic distortion (tape-like warmth)  |
| Dist 3     | 3rd harmonic distortion (tube-like grit)    |

**Best for:** Versatile compression on anything. NUKE mode for extreme parallel compression. Dist 2/3 for analog character.

### Audioscape Opto (LA-2A Clone)

| Control    | Range / Notes                               |
| ---------- | ------------------------------------------- |
| Peak Reduction | Compression amount                      |
| Gain       | Makeup gain                                 |
| Mode       | Compress / Limit                            |

**Best for:** Smooth, transparent vocal compression. Set-and-forget — the optical circuit responds musically. In the default vocal chain after the 1176 for two-stage compression.

---

## IK Multimedia MixBox

Channel strip plugin with up to 8 rack slots. 70+ effect modules drawn from T-RackS, AmpliTube, and SampleTank. Runs as a plugin in Logic Pro.

### EQ (4 modules)

| Module        | Based On          | Notes |
| ------------- | ----------------- | ----- |
| British EQ    | SSL/Neve hybrid   | Classic console EQ |
| EQ PG         | —                 | Parametric/graphic |
| Parametric EQ | —                 | Full parametric |
| Vintage EQ-1A | Neve 1073         | Vintage character EQ |

### Dynamics (8 modules)

| Module          | Based On          | Notes |
| --------------- | ----------------- | ----- |
| Black 76        | UREI 1176         | FET compressor |
| White 2A        | LA-2A             | Optical compressor |
| Model 670       | Fairchild 670     | Variable-mu tube comp |
| Bus Compressor  | SSL G Bus         | Mix bus glue |
| British Dynamics| SSL channel       | Channel strip dynamics |
| Compressor      | —                 | General purpose |
| De-Esser        | —                 | Vocal de-essing |
| Limiter         | —                 | Brickwall limiter |

### Reverb (14 modules)

| Module           | Notes |
| ---------------- | ----- |
| Ambience         | Subtle, short |
| ConvoRoom        | Convolution reverb |
| Digital Reverb   | Clean digital |
| Hall Reverb      | Large hall |
| Inverse Reverb   | Reversed envelope |
| Plate Reverb     | Classic plate |
| Room Reverb      | Natural room |
| Spring Reverb    | Spring tank |
| Stereo Imager    | Width processing |
| Sunset Chamber   | Sunset Sound Studios chamber |
| Sunset Iso Booth | Sunset Sound Studios iso booth |
| Sunset Live Room | Sunset Sound Studios live room |
| Sunset Plates    | Sunset Sound Studios plates |
| Sunset Spring    | Sunset Sound Studios spring |

### Delay (3 modules)

| Module        | Notes |
| ------------- | ----- |
| Digital Delay | Clean, precise |
| Reverb Delay  | Delay + reverb combo |
| Tape Echo     | Warm tape delay |

### Modulation (17 modules)

| Module          | Notes |
| --------------- | ----- |
| AM Modulator    | Amplitude modulation |
| AutoPan         | Auto-panning |
| Chorus          | Classic chorus |
| Chorus C1       | Vintage chorus |
| Electric Flanger | Jet flanger |
| Ensemble        | String ensemble effect |
| Env Flanger     | Envelope-controlled flanger |
| Flanger         | Standard flanger |
| FM Modulator    | Frequency modulation |
| Multi Chorus    | Multi-voice chorus |
| Opto Tremolo    | Optical tremolo |
| Phaser          | Phase shifter |
| Rotary Speaker  | Leslie sim |
| Slicer          | Rhythmic gate |
| Small Phazer    | Compact phaser |
| Tremolo         | Amp-style tremolo |
| Uni-V           | Uni-Vibe |

### Filter (10 modules)

| Module        | Notes |
| ------------- | ----- |
| Env Filter    | Envelope filter / auto-wah |
| Filter Formant | Vowel formant filter |
| Filter Phaser | Filter + phaser combo |
| Filter-C      | Character filter |
| Filter-M      | Character filter |
| Filter-O      | Character filter |
| Filter-R      | Character filter |
| LFO Filter    | LFO-modulated filter |
| Multi Filter  | Multi-mode filter |
| Wah 47        | Wah pedal |

### Distortion (5 modules)

| Module      | Notes |
| ----------- | ----- |
| Crusher     | Bit crusher / sample rate reduction |
| Distortion  | Hard clipping |
| Lo-Fi       | Lo-fi degradation |
| Overdrive   | Soft clipping |
| Overscream  | TS808-style overdrive |

### Saturation (3 modules)

| Module        | Notes |
| ------------- | ----- |
| Phonograph    | Vinyl record character |
| Saturator-X   | Analog tape/tube saturation |
| Tape Cassette | Cassette tape emulation |

### Amp (9 modules)

| Module            | Notes |
| ----------------- | ----- |
| American Vintage T | Fender-style clean |
| British Tube Lead  | Marshall-style |
| Cabinet           | Speaker cab sim |
| Flexi Amp         | Flexible amp model |
| Jazz Amp 120      | Roland JC-120 style |
| Modern Tube Lead  | High-gain modern |
| Preamp            | Generic preamp |
| SVT Classic       | Ampeg SVT bass amp |
| Tone Control      | Simple tone shaping |

### Channel Strip (4 modules)

| Module        | Notes |
| ------------- | ----- |
| Channel Strip | Full channel strip |
| EQ 81         | Neve 1081 style EQ |
| EQ Comp       | EQ + compressor combo |
| EQ-PA         | Parametric EQ |

---

## IK Multimedia AmpliTube 5

Guitar and bass amp/effects simulator. Runs as a plugin in Logic Pro or standalone. Full signal chain: tuner → stomps → amp → cab → mic → rack FX.

### Amp Models (Selection — 111 total in MAX v2)

#### Fender-Style
'53 Bassman, '57 Bandmaster, '57 Custom Champ, '57 Custom Deluxe, '57 Custom Pro-Amp, '57 Deluxe, '59 Bassman LTD, Hot Rod DeVille 410, Pro Junior, Vibro-King, '65 Super Reverb, '65 Twin Reverb

#### Marshall-Style
Brit Valve Pre (JMP-1), Brit 8000 (JCM 800), Brit 9000 (JCM 900), Brit Silver (Silver Jubilee), British Tube Lead 1 & 2, Red Pig (Major), Vintage Metal Lead (JMP 100), JH Gold (JTM 45)

#### Mesa/Boogie
Mark III, Mark IV, Dual Rectifier, Triple Rectifier, TransAtlantic TA-30

#### Orange
OR-120, Tiny Terror, Rockerverb 50, AD 30, Thunderverb 200, Dual Terror, OR 50

#### Signature
Slash AFD 100, Slash JCM (2555SL), Satch VM (JVM410HJS), Dimebag CFH

#### Bass
SVT Classic, SVT 2 PRO, B-15, Portaflex, Aguilar models

### Stomp Pedals (Selection — 111 total in MAX v2)

#### Distortion / Overdrive
Overscream (TS808), Diode Overdrive, Satch Distortion, Metal Distortion, Big Pig, Class Fuzz, Fuzz Age, FuzzOne, XS Fuzz, Crusher, X-DRIVE

#### Delay
Analog Delay, Digital Delay, EchoMan, EP Tape Echo, Fender Tape Echo, Solid State Tape Echo, Tap Delay, T-Rex Replica, X-TIME

#### Modulation
Analog Chorus, Chorus-1, Analog Flanger, Electric Flanger, Fender Phaser, FOX Phaser, Small Phazer, Uni-V, Seek Trem, Fender Tremolo, Rotary, X-Chorus, X-VIBE

#### Reverb
Fender '63 Reverb, Spring Reverb, X-SPACE

#### Compression / EQ
Compressor, Booster, 6-Band EQ, 7-Band Graphic, 10-Band Graphic

#### Wah / Filter
Contour Wah, Bass Wah

### Rack Effects (48 in MAX v2)

#### Dynamics
Black 76 (1176), White 2A (LA-2A), Model 670 (Fairchild), Tube Compressor

#### EQ
EQ 81 (Neve 1081), EQ PA, Vintage EQ-1A (Neve 1073), EQ PG, Graphic EQ, Parametric EQ

#### Reverb
Plate Reverb, Hall Reverb, Inverse Reverb, Room Reverb, Shimmer Reverb

#### Modulation / Effects
Digital Chorus, Digital Delay, Digital Flanger, Auto Pan, Rotary Speaker, AM/FM Modulator, Saturator-X, Tape Cassette

#### Filters
Filter C, Filter M, Filter O, Filter R, Filter Formant, Filter Phaser

### Cabinets & Mics

- **106 cabinet models** with Volumetric Impulse Response (VIR)
- **33 speaker models**
- **18 mic models** with adjustable distance, angle, and height
- **8 room simulations**

---

## IK Multimedia TONEX

AI-powered tone modeling using Machine Modeling™ technology. Captures and recreates the sound of real amps, cabs, and pedals. Runs as a plugin in Logic Pro.

### How It Works
- **Tone Models** capture the complete tonal character of an amp/cab/pedal chain
- Can create custom Tone Models from your own gear (5-minute capture process)
- Access to **ToneNET** community library (56,000+ shared models)
- VIR™ cabinet and mic simulation

### Factory Tone Models (varies by version)
- **TONEX CS (Free):** 20 models
- **TONEX SE:** 240 models
- **TONEX Standard:** 440 models
- **TONEX MAX:** 1,250+ models

### Sample Factory Amps Modeled
Fender '59 Bassman, Marshall JMP 100W, Dumble Overdrive Special, Vox AC30, Diezel VH4, Mesa/Boogie MKIIC+, DrZ Maz 18, Bogner Ecstasy, Two Rock Studio Signature, Marshall Silver Jubilee, Hiwatt DR103, ENGL models

### Available Premium Collections
| Collection             | Models | Content |
| ---------------------- | ------ | ------- |
| MESA/Boogie Reference | 70     | 5 Mesa amps |
| Brown Sound 82/84     | 77     | EVH-era tones |
| Metal Gems            | 100    | Peavey 5150, Diezel, Soldano, Bogner |
| Joe Satriani Amp Vault | 67    | 28 amps |
| ENGL Ampthology Vol 1 | 72     | 6 ENGL amps |
| ODS Legends           | 20     | Dumble, Klon, TS808 |
| Boutique Overdrives   | 40     | 3 classic drive pedals |
| Signature Bass        | 150    | Bass amps and cabs |

### Built-in Effects
- Noise Gate
- EQ
- Compressor
- 2x Delays
- 5x Modulation (Chorus, Flanger, Tremolo, Phaser, Rotary)
- 6x Stereo Reverbs (including Spring)
- Tuner

---

## IK Multimedia T-RackS Tape Machine

Standalone tape emulation plugin from the T-RackS suite. Emulates the Tascam 388 tape recorder.

### Controls
| Control    | Notes |
| ---------- | ----- |
| Input      | Drive into tape (more = more saturation) |
| Speed      | Tape speed (affects frequency response and saturation character) |
| Low Bump   | Low-frequency tape head bump |
| High Shelf | High-frequency rolloff |
| Output     | Output gain |

### Character
- Adds tape compression, harmonic saturation, and subtle frequency shaping
- Frequency response changes with tape speed (slower = warmer/darker)
- Can be used on individual tracks or mix bus
- Subtle at low input levels, increasingly saturated at higher levels

---

## Effect Chain Recipes

### Vocal Recording Chain (Outboard)
1. **HA73 ch2** — preamp gain, light EQ (HPF at 80Hz, slight presence boost)
2. **1176 ch2** — fast attack, medium release, 4:1, catching peaks
3. **Opto** — slow optical compression, 3-4dB GR, smoothing dynamics

### Vocal Mix Chain (Wing + Software)
1. **Wing ch4 EQ** — E84 model: HPF 80Hz, cut 300Hz, boost 3kHz, air at 12kHz
2. **Wing ch4 Dyn** — ECL33 (Neve 33609): gentle comp + limiter
3. **Wing FX slot** — PLATE reverb (1.2s decay, 20ms pre-delay) via send
4. **Wing FX slot** — ST-DL delay (BPM-synced 1/4 note) via send
5. **MixBox** (in DAW) — Black 76 for parallel compression, Tape Cassette for warmth

### Guitar Recording Chain (Outboard)
1. **HA73 ch1** — preamp gain, EQ to taste
2. **1176 ch1** — medium attack, fast release, 8:1, taming pick transients

### Guitar Tone Shaping (Wing + Software)
1. **Wing ch2 EQ** — PULSAR model: Pultec-style low boost at 100Hz, high boost at 5kHz
2. **Wing FX slot** — TAPE-DL (slapback, 80-120ms, 20% mix) via insert or send
3. **AmpliTube** (in DAW) — amp + cab + pedals for full guitar rig
4. **TONEX** (in DAW) — captured amp tone as alternative

### Mix Bus (Wing)
1. **Main 1 EQ** — STD model: gentle high shelf +1dB at 12kHz, low cut at 30Hz
2. **Main 1 Dyn** — SBUS (SSL G Bus): ratio 2:1, slow attack, auto release, 1-2dB GR
3. **Wing FX slot** — \*MASTER\* channel strip on post-insert for final polish

### Parallel Compression (Wing)
1. Set `/ch/N/dyn/mdl s "76LA"` (1176 model)
2. Slam it: ratio ALL, low threshold
3. Blend with `/ch/N/dyn/mix f 20.0` (20% wet) — keeps transients, adds density

### Lo-Fi / Vintage (Software)
1. **MixBox** — Tape Cassette → Lo-Fi → Phonograph
2. **T-RackS Tape Machine** — medium drive, slow speed for warmth
3. **Wing** — TAPE FX slot for tape saturation, roll off highs with HPF/LPF
