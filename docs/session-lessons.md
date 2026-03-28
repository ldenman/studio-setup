# Session Lessons

Lessons learned during studio sessions. Updated after each session.

---

## 2026-03-27 — Guitar Tracking (Rhythm + Lead)

### Noise Floor
- Main 1 trim must be 0dB — was found at +18dB, amplifying noise floor
- Bus compressor (SBUS) on main was boosting quiet signals — disabled
- Mute outboard returns (Ch17/Ch18) when not tracking — outboard noise floor leaks to main
- Ch18 must be unmuted for recording path to work (pre-fader sends die on mute), but take it off main when not monitoring
- TAPE (FX10) on Bus 8 amplifies noise floor — bypass when not needed
- Ch7 had a leftover USB/1 assignment leaking signal and causing L/R imbalance

### Signal Routing
- Bus 2 (Guitar Send) had a send to Bus 3 (Reverb) at 0dB — this bypassed the outboard chain entirely, leaking raw amp sim signal to main via the reverb bus. Reverb sends should come from monitoring buses, not outboard send buses.
- Two Wing channels cannot share the same USB input — the second channel gets no signal
- An FX slot can only be on one insert at a time — two buses sharing the same FX slot will fight. One steals it.
- Removing an FX from an insert can reassign it to another channel — always verify after clearing

### Architecture
- Amp sim goes AFTER outboard, not before — if you want outboard-only recordings with amp sim in monitoring, the amp sim must be on the monitoring bus (post-outboard return), not on Bus 5/6 (pre-outboard)
- Recording and monitoring are separate paths: record via Bus 8 (outboard + tape), monitor via Bus 10/11 (amp sim). Independent buses.
- One amp sim per track type, separate buses: rhythm (Bus 10/RACKAMP), lead (Bus 11/ANGEL). Don't switch a shared bus — add a new bus.
- Recording captures outboard + tape. Monitoring adds amp sim on top. Playback adds amp sim on top of recording. No tape on monitoring — it's recording-only.

### Gain Staging
- Wing analog outputs run ~6dB hotter than USB digital — Model 12 records at -12dB, Logic at -18dBFS from the same source. This is normal. Accept it.
- -18dBFS is professional reference level (0dBVU). Not a problem.
- Bus 8 fader at -1dB for Model 12 level. Ch18 send to Bus 8 at -6dB for Logic level.
- USR/2 POST tap means Bus 8 fader affects the Logic recording level

### Model 12 Limitations
- Model 12 USB output is 12-in/10-out: 10 analog inputs to DAW + stereo main mix (11/12). Individual MTR playback tracks do NOT output over USB.
- Logic is the primary multi-track recorder. Model 12 is transport master + backup recorder + DAW controller.
- Logic's "Software Monitoring" must be OFF — Wing handles all monitoring

### Send Levels Keep Getting Reset
- Ch26 send to Bus 10 must be +10dB for playback level matching. It keeps getting reset to 0dB during other routing changes. Always verify send levels after making ANY routing change — the Wing may reset sends when bus assignments or FX inserts change.

### Wing Quirks
- Muting a channel kills ALL signal including pre-fader sends
- Setting a pre-insert to NONE can reassign the FX slot to another channel — always scan after clearing
- Two channels on the same USB input: second channel gets nothing
- USR PRE tap on a bus: not affected by bus fader. USR POST tap: affected by bus fader.
- Assigning an FX slot to a new insert silently removes it from the previous one — the orphaned insert shows `$stat=N/A` with no warning

---

## Pre-2026-03-27 — Lessons from Build History

### Feedback Loops (Multiple Incidents)
- **Loopback feedback:** Wing set as both Source AND Monitor in Loopback creates digital feedback (white noise on all USB inputs). Wing must be Source only.
- **Model 12 USB-mode feedback:** USB-mode tracks re-broadcast their Wing input into the Model 12 stereo mix → Ch13 → Main → USB again. Fix: keep all non-recording tracks in MTR mode.
- **USB 3 (re-amp) feedback:** Outboard noise floor leaks through USB 3 even when Ch18 is muted. Must disable USB 3 after re-amping.
- **Ch13 recording feedback:** Ch13 (Model 12 stereo return) must be muted during recording if Main 1 feeds back to Model 12 via USB.

### USR Routing
- USR `in` values use **simple bus numbering** (Bus 8 = `in=8`), NOT stereo indexing (which would be `in=15`). This is different from `/io/out/LCL/N/in` which DOES use stereo indices. Got this wrong multiple times before documenting it.

### Tape Emulation Architecture (Evolved 3 Times)
1. First: TAPE on channel pre-inserts (Ch1/Ch2) — wrong, colored the outboard send
2. Then: TAPE on recording buses (Bus 7/8/9) — correct, outboard gets clean signal
3. Now: TAPE on Bus 8 for recording, monitoring buses (10/11) are separate. Amp sim is post-outboard.

### Stereo Mode
- Wing channels default to mono. Must explicitly set `/io/in/GRP/N/mode s "ST"` for stereo sources or panning collapses to center. Bit us on Ch6 (condensers) and Ch13 (Model 12 return).

### SMPTE Offset Trap
- Logic defaults bar 1 to SMPTE `01:00:00:00` (1-hour offset). Model 12 sends MTC starting at `00:00:00:00`. This causes Logic to show negative bar numbers. Fix: Logic → Project Settings → Synchronization → set "Bar Position 1 1 1 1 plays at SMPTE" to `00:00:00:00.00`.

### Speaker Routing
- Speakers on P23/P24 normalled from Wing Out 7/8 (MX1). Break normals with Model 12 main outs for feedback-safe playback monitoring — Model 12 signal never enters the Wing.
- Out 7 and Out 8 stereo indexing: Out 7 = `in=1` (MX1 L), Out 8 = `in=2` (MX1 R). Both were initially set to `in=1` giving mono.

### HA73 Channel Variance
- HA73 channels A and B have different output characteristics at the same knob positions. Calibrate each independently.

### Patchbay & Phantom Power
- Patchbay is TRS — cannot carry phantom power. Condenser mics must connect directly via XLR to Wing inputs, bypassing the patchbay.

### Model 12 Limitations (Discovered Late)
- USB output is 12-in/10-out: sends 10 analog inputs to computer + stereo main mix (11/12). Individual MTR playback tracks do NOT output over USB.
- This forced the move to Logic as primary recorder with individual track returns.
