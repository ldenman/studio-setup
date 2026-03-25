# Outboard Calibration

Calibrate the outboard chains so each piece of gear receives and returns signal at the correct level. This ensures unity gain through the chain, predictable behavior from the compressors, and clean headroom.

## What Claude Can Do
- Generate a reference tone from the Wing's oscillator and route it through Bus 1 or Bus 2 to the outboard chain
- Set and verify Wing output levels, bus send levels, and return channel trim
- Read back the return level on Ch17/Ch18 to confirm the signal is coming back at the expected level
- Walk through each piece of gear step by step

## What Lake Must Do
- Adjust the physical knobs on each piece of outboard gear (HA73 gain/EQ, WA76 input/output, Distressor input/output, Opto gain/peak)
- Read VU meters on units that have them (WA76, Distressor, Opto)
- Patch cables on the patchbay front panel to isolate individual units for calibration

## Metering Note
The HA73-EQX2 has no onboard VU meter. Use Ch17 (vocal) or Ch18 (guitar) on the Wing as the metering point for every unit. Calibrate one unit at a time by patching its output directly back to the Wing return input (bypassing downstream gear).

## Calibration Procedure (per chain)

### 1. Send Reference Tone
Route the Wing's oscillator (1kHz sine, -18dBFS) through the bus send to the outboard chain:
- `/cfg/osc/1/mode s "SINE"`, `/cfg/osc/1/f f 1000.0`, `/cfg/osc/1/lvl f -18.0`
- Route oscillator to the appropriate bus (Bus 1 for vocal, Bus 2 for guitar)
- Verify tone is leaving on the correct Wing output

### 2. Calibrate Each Unit Individually
Patch one unit at a time back to the Wing return so Ch17/Ch18 meters show the result. Claude reads the Wing meters, Lake adjusts the knobs.

**Vocal chain (Bus 1 → Out 1):**

a. **HA73 A** — Patch: Out 1 (P1 top, normalled) → HA73 A → patch HA73 A out (P2 top) directly to Wing LCL 17 (P4 bottom) via front-panel cable, bypassing WA76/Opto. EQ flat/bypassed. Lake adjusts gain until Claude confirms -18dBFS on Ch17.

b. **WA76 A** — Patch: restore P2 normal (HA73 A → WA76 A), patch WA76 A out (P3 top) directly to Wing LCL 17 (P4 bottom) via front-panel cable, bypassing Opto. Set ratio 4:1, threshold fully CW (no compression). Lake adjusts input/output until Claude confirms -18dBFS on Ch17 with no gain reduction on the VU.

c. **Opto** — Restore all normals (full chain). Signal now flows through all three units. Lake adjusts Opto gain/peak until Claude confirms -18dBFS on Ch17. Check Opto VU shows no gain reduction.

**Guitar chain (Bus 2 → Out 2):**

a. **HA73 B** — Patch: Out 2 (P5 top, normalled) → HA73 B → patch HA73 B out (P6 top) directly to Wing LCL 18 (P8 bottom) via front-panel cable. Lake adjusts gain until Claude confirms -18dBFS on Ch18.

b. **WA76 B** — Patch: restore P6 normal, patch WA76 B out (P7 top) directly to Wing LCL 18 (P8 bottom). Lake adjusts input/output until Claude confirms -18dBFS on Ch18.

c. **Distressor** — Restore all normals (full chain). Lake adjusts input/output until Claude confirms -18dBFS on Ch18.

### 3. Kill the Tone
Turn off the oscillator: `/cfg/osc/1/mode s "OFF"`

### 4. Test with Live Signal
Play/sing at normal performance level and verify the chain behaves as expected. Compressors should show modest gain reduction (3-6dB) at performance level with default settings.

## Calibration Targets
- Wing bus send to outboard: 0dB (unity)
- Each unit in isolation: signal returns at approximately -18dBFS on Ch17/Ch18 with -18dBFS reference tone (unity passthrough)
- Full chain end-to-end: -18dBFS in, -18dBFS out on Ch17/Ch18
- Compressors (WA76/Distressor/Opto): 0dBVU on their own meters, no gain reduction during calibration

## Chain Orders
- **Vocal:** Wing Out 1 → P1 → HA73 A → P2 → WA76 A → P3 → Opto → P4 → Wing Ch17
- **Guitar:** Wing Out 2 → P5 → HA73 B → P6 → WA76 B → P7 → Distressor → P8 → Wing Ch18

## Calibrated Settings

**Vocal chain (1kHz sine @ -18dBFS):**
- HA73 A: Red gain knob 35, output 1 o'clock → 2 yellow steps on Ch17
- WA76 A: Input 48, output 18, ratio 4:1, 0dB gain reduction → 2 yellow steps on Ch17
- Opto: Gain between 10 and 15, compress mode, peak reduction off → 2 yellow steps on Ch17

**Guitar chain (same reference tone):**
- HA73 B: Red gain knob 35, output 4 o'clock → 2 yellow steps on Ch18
- WA76 B: Input 48, output 24, ratio 4:1, 0dB gain reduction → 2 yellow steps on Ch18
- Distressor: Input 2, output 7, no compression → 2 yellow steps on Ch18

## Re-calibrate When
- Swapping outboard units in the chain (e.g., Distressor for Opto)
- After changing the Wing's sample rate or clock source
- If return levels drift noticeably from session to session
