# Engineer Notebook

Notes, discoveries, gotchas, and lessons learned while building and operating the studio.

---

## 2026-03-22

### Wing Mute Kills Pre-Fader Sends
On the Wing, muting a channel kills ALL signal — including pre-fader bus sends. This is different from consoles where pre-fader sends survive a mute. If a channel needs to feed a bus but shouldn't be heard on main, remove it from main (`/ch/N/main/1/on i 0`) instead of muting. Bit us when Ch2 was muted and Bus 2 (outboard send) went silent, and again with Ch6 (condenser mics) feeding Bus 6.

### Bus Output Stereo Indexing
The Wing's `/io/out/LCL/N/in` parameter uses stereo channel indices, not bus numbers. Bus 1L=1, Bus 1R=2, Bus 2L=3, Bus 2R=4, etc. Formula: `in = (bus_number - 1) * 2 + 1` for L. We spent a long time debugging why guitar wasn't reaching the outboard — Out 2 was set to `in=2` (Bus 1R) instead of `in=3` (Bus 2L). Same pattern applies to USR outputs.

### HA73 Channel Variance
The HA73-EQX2's two channels have different gain characteristics. Both set to gain knob 35, but channel A needed output at 1 o'clock and channel B needed 4 o'clock to hit the same level. This is normal for analog gear — don't expect matched behavior across channels.

### Patchbay Can't Carry Phantom Power
The Samson patchbay is TRS. Phantom power (48V) requires XLR pins 2+3. Condenser mics must connect directly to the Wing's XLR inputs, bypassing the patchbay entirely. The mic signal can then be sent to the patchbay via a Wing bus output (Bus 4 → Out 3+4 → P9/P10) for outboard routing.

### Wing Oscillator Control
The Wing's `/cfg/...` paths (oscillator, monitor section, solo config) are NOT accessible via wapi (TCP). Must use oscsend (UDP) for these, which is fire-and-forget — can't confirm values took. The oscillator level couldn't be adjusted reliably via oscsend during calibration.

### Meter API Quirks
- The wext.h header shipped with wrong function signatures for `wSetMetersRequest`, `wGetMeters`, and `wRenewMeters`. Had to match them to the PDF documentation (wapi Reference Guide) instead.
- Requesting a single channel's meters returns stale/noise-floor data. Requesting all 40 channels (`mbits[0-4] = 0xFF`) returns accurate live data. Always use `wingctl meter all`.
- Meter values are signed 16-bit big-endian in 1/256th dB. Noise floor reads around -102dB. -128dB (0x8000) means no signal.

### A/B Testing: Signal Path Independence
When comparing hardware vs plugin (e.g., Opto vs Wing LA-2A), the plugin CANNOT live on the source channel. The Wing's pre-fader tap (`ptap=5`) is after dynamics processing, so any plugin on the source channel colors the signal feeding the hardware path too. Solution: source channel has dynamics off and is not assigned to main. Hardware path via bus send. Plugin on a completely separate channel receiving the same USB input directly.

### FX Slot Ownership
An FX slot can only be inserted on one channel/bus at a time. Assigning it elsewhere silently removes it from the previous location. Each guitar mode (Electric/Acoustic) needs its own FX slot so settings are preserved during switching.

### SMPTE Offset Trap
Logic Pro defaults to bar 1 at SMPTE `01:00:00:00` (1-hour offset — old broadcast convention). The Model 12 sends MTC starting at `00:00:00:00`. Mismatch causes Logic to calculate negative bar numbers (bar -9). Fix: set Logic's "Bar Position 1 1 1 1 plays at SMPTE" to `00:00:00:00.00`. This will silently drift back to the default if you reset project settings or create a new project.

### Logic Pro Cannot Slave to MIDI Clock
Logic Pro can only slave to MTC (MIDI Timecode), not MIDI clock. It can SEND MIDI clock but not receive it. The Model 12 fortunately sends both MTC and MIDI clock. The MMC (MIDI Machine Control) listener handles start/stop transport commands.

### Wing Channel Strips Are Stereo
Each Wing channel strip handles a stereo pair of inputs automatically. When a channel's input source has consecutive paired inputs (USB/9-10, LCL/3+4), both L and R land on that single channel — no need for two channels. The channel's pan and width controls manage the stereo image. Had to set Ch6 to stereo mode on the touchscreen for the condenser pair.

### Monitor Section Routing for Solo
To make solo work through speakers (not just headphones), MX1 must source from the monitor section output, not directly from Main 1. Set MX1's direct input to `MON.PH` (monitor phones output). The Main 1 → MX1 send must be OFF to avoid double-signal. `MON.SPK` (speaker output) didn't work — only `MON.PH` routes solo correctly. This is configured on the Wing touchscreen, not via wapi.

### Model 12 Tracks 11/12 Are Internal Only
Model 12 tracks 11/12 capture the internal main L/R mix and cannot receive external USB input. The rough mix from the Wing must go to tracks 9/10 via USB/Loopback.

### Speakers on Patchbay for Source Switching
Speakers routed through patchbay (P23/P24) instead of direct-wired from Wing outputs. This allows switching between Wing monitoring and Model 12 playback by plugging Model 12 main outs into the patchbay front panel — breaks the Wing normal, sends Model 12 directly to speakers. No feedback risk because Model 12 playback never enters the Wing's signal path. Critical for a studio with open condenser mics.

### Output Stereo Indexing Strikes Again
Wing Out 7 and Out 8 were both set to MTX `in=1` — both carrying MX1 Left. Out 8 needed `in=2` for MX1 Right. Same stereo indexing pattern as buses. Always check both sides of a stereo output pair.
