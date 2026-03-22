# Studio Changelog

## 2026-03-22

### Transport Sync (9fecb12)
- Model 12 is the transport master, Logic Pro slaves via MTC
- Fixed Logic jumping to negative bars (-9) when Model 12 starts playback
- Root cause: Logic's default SMPTE offset is `01:00:00:00`, Model 12 sends MTC starting at `00:00:00:00`
- Fix: set Logic's "Bar Position 1 1 1 1 plays at SMPTE" to `00:00:00:00.00`

### Tape Machine / Digital Recording (04f770d)
- Model 12 records vocal dry (track 1), guitar dry (track 2), condenser mics (tracks 7/8), and rough mix (tracks 9/10) simultaneously via USB/Loopback
- All local channels have TAPE emulation baked into dry recordings (FX9 on Ch1, FX10 on Ch2, FX3 on Ch6)
- PRE tap point (ptap=5) captures signal after tape emulation and channel dynamics — compression/gates are baked in when enabled
- USR/6 and USR/7 split Ch6 stereo condensers into L/R for recording to USB 15/16

### Guitar Modes (461357e)
- Replaced single amp sim on Bus 2 with two dedicated amp buses:
  - Bus 5 (Electric): FX1 DELUXE pre-insert, muted by default
  - Bus 6 (Acoustic): FX11 RACKAMP (clean/bright) pre-insert
- Both buses feed Bus 2 which sends to the outboard chain — amp sim goes before outboard compression
- Switch modes by muting/unmuting buses
- Ch5 (Gtr Acoustic DI) added via USR/5 — clean DI path bypassing outboard entirely
- Ch6 (Gtr Ac Mics) receives stereo condensers on LCL/3+4 with phantom power via XLR direct (patchbay is TRS, can't carry phantom)
- Condenser signal available on patchbay via Bus 4 → Out 3+4 → P9 (L) + P10 (R)
- Discovered: Wing mute kills pre-fader sends — use main assign off instead of mute to keep sends flowing

### A/B Testing and Monitor Routing (1d16a26)
- Established A/B testing procedure for hardware vs plugin comparison
  - Key insight: plugin can't live on the source channel because ptap taps after dynamics, coloring the hardware send
  - Solution: source channel (dynamics off, not on main) feeds hardware, separate channel receives same source with plugin
- Built blind A/B test script (random solo switching)
- Fixed monitor routing: MX1 now sources from MON.PH (monitor phones) via direct input instead of Main 1 send — solo now works through speakers
- Switched guitar amp sim from DELUXE to RACKAMP for acoustic guitar
- Wing LA-2A vs hardware Opto comparison on bass: virtually indistinguishable in blind test

### Outboard Calibration and Tape Emulation (a4a1140)
- Calibrated both outboard chains using Wing oscillator (1kHz sine) with per-unit patchbay isolation
- Calibration target: 2 yellow steps on Wing meters (approx -18dBFS)
- **Vocal chain** (HA73 A → WA76 A → Opto):
  - HA73 A: gain 35, output 1 o'clock
  - WA76 A: input 48, output 18, ratio 4:1, 0dB GR
  - Opto: gain 10-15, compress mode, peak reduction off
- **Guitar chain** (HA73 B → WA76 B → Distressor):
  - HA73 B: gain 35, output 4 o'clock (different from channel A — normal analog variance)
  - WA76 B: input 48, output 24, ratio 4:1, 0dB GR
  - Distressor: input 2, output 7, no compression
- Added TAPE FX pre-inserts on Ch1 and Ch2 for analog tape emulation on all recordings
- Fixed Bus 2 output routing: `in` parameter uses stereo channel indices (Bus 2L = 3, not 2) — this was why guitar outboard wasn't getting signal
- Bus 3 (reverb) set up with FX2 PLATE, receiving from Bus 1 and Bus 2, assigned to main
- Added `wingctl meter` command using wapi meter API (fixed wext.h function signatures to match actual ABI)

## 2026-03-21

### Initial Studio Setup (a884886, 6860ccb)
- Full studio configuration committed: Behringer Wing Rack mixer, outboard chains, MCP server
- Wing controlled via MCP tools (wing_get, wing_set, wing_node) over TCP/wapi, with oscsend fallback over UDP
- Channel layout: Ch1 Vocal Dry, Ch2 Guitar Dry, Ch9-12 DAW (Logic session players), Ch17 Vocal Processed, Ch18 Guitar Processed
- Outboard vocal chain: HA73 A → WA76 A → Opto, normalled on patchbay P1-P4
- Outboard guitar chain: HA73 B → WA76 B → Distressor, normalled on patchbay P5-P8
- USB/Loopback routing for dry recording to Tascam Model 12
- Synced all documentation files to current channel layout
