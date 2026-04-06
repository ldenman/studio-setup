# Podcast Outline: Building a Hybrid Studio in 8 Days — The Complete Changelog

## Intro (2 min)
- Hook: "We built a professional hybrid recording studio from scratch in 8 days. An AI assistant engineered it. Here's every decision, every mistake, and every pivot — in order."
- This isn't theory — every change came from real sessions, real failures, and real recordings
- The studio evolved three major times in one week. The final architecture looks nothing like day one.

---

## Day 1 — March 21: Foundation (5 min)

### What was built
- Wing Rack as the central mixer/hub — 40 channels, OSC controllable over the network
- Dual outboard chains permanently wired through a 48-point patchbay
  - A side (vocals): HA73 A (Neve EQ) → WA76 A (1176 compression) → Opto (LA-2A leveling)
  - B side (guitar): HA73 B (Neve EQ) → WA76 B (1176 compression) → Distressor
- Patchbay normalled — zero cables needed for default operation. Plug in the instrument and record.
- Model 12 as the multitrack recorder, connected via Loopback software over USB
- Logic Pro providing virtual session players (bass, keyboard, synth, drums) synced via MTC
- An AI assistant (Claude) controlling the Wing via MCP tools — wing_get, wing_set, wing_node

### The design philosophy
- Zero friction — the studio is always ready
- Everything through the patchbay (analog) or Loopback (digital) — single points of flexibility
- Automate everything — scripts for channel names, colors, routing

---

## Day 2 — March 22: The Feature Blitz (8 min)

### Six commits in one day — the studio gets its full feature set

**Outboard calibration**
- Both chains calibrated end-to-end with documented settings
- WA76 A: Attack 3, Release 7, Ratio 4:1 — catching vocal peaks with 3-4dB gain reduction
- Opto: Peak Reduction ~40%, Compress mode — smooth 2-3dB leveling
- WA76 B: Attack 5, Release 6 — medium attack to let guitar pick transients through
- Distressor: 4:1, Dist 2 (tape mode) — leveling plus warm harmonic color

**Tape emulation added**
- Wing's built-in TAPE FX loaded on channel pre-inserts (Ch1 and Ch2)
- First attempt at tape — this would be wrong and get moved twice later

**A/B testing framework**
- Method for comparing hardware outboard against Wing plugin emulations
- Key rule: source channel has dynamics OFF, not assigned to main
- Plugin goes on a separate channel — the pre-fader send tap is post-dynamics
- Use wingctl meter all for level matching within 0.5dB

**Guitar modes**
- Bus 5 Electric: ANGEL (Mesa-style lead) or DELUXE (Fender rhythm) amp sim
- Bus 6 Acoustic: RACKAMP (clean/bright) amp sim
- Mute/unmute buses to switch modes — no repatching

**Condenser mics and transport sync**
- Ch6 receives stereo condensers on LCL/3+4 via XLR direct — patchbay is TRS and can't carry phantom power
- Model 12 sends MTC to Logic — press play on the Model 12, Logic follows
- Critical discovery: Logic's SMPTE offset defaults to 1 hour. Model 12 sends from 00:00:00:00. Mismatch shows negative bar numbers. Fix: set Logic to 00:00:00:00.00.

**Speaker routing**
- Speakers wired through patchbay P23/P24 from Wing MX1 (matrix output)
- MX1 sources from monitor phones output — this makes solo work through speakers

---

## Day 3 — March 23: The White Noise Incident (3 min)

### First major crisis
- White noise on ALL USB inputs. Everything screaming.
- Root cause: Loopback had the Wing set as both Source AND Monitor — creating a digital feedback loop
- Also found: Ch7 had a leftover USB/1 assignment leaking Mac system audio, causing L/R imbalance
- Speaker L/R routing was swapped on the patchbay

### What was learned
- Wing must be Source only in Loopback — never Monitor
- Always check for stale channel assignments after any routing change
- Documented as the first entry in what would become the session lessons file

---

## Day 4 — March 24: The Architecture Overhaul (10 min)

### Nine commits in one day — the biggest single day of changes

**Tape emulation moves to recording buses (V2)**
- The first major architecture pivot
- TAPE on Ch1/Ch2 was wrong — it colored the signal going to outboard. The HA73 and WA76 were receiving tape-saturated signal instead of clean signal.
- Solution: Move TAPE to dedicated recording buses (Bus 7 Vocal Rec, Bus 8 Guitar Rec, Bus 9 Mic Rec) as pre-inserts
- Outboard now gets clean signal. Only the recording path picks up tape color.
- This is correct tape machine behavior — tape is on the recording heads, not the monitoring path.

**Overdub monitoring**
- Model 12 playback return added on Ch13 (Tape Playback) via USB/3-4
- Previous takes play back from Model 12 while new ones record
- Overdub workflow simplified — no more USB 17/18 workaround

**USR routing fix — the indexing trap**
- USR `in` values use simple bus numbering: Bus 8 = `in=8`
- This is different from `/io/out/LCL/N/in` which uses stereo indexing: Bus 8L = `in=15`
- Got this wrong multiple times before documenting it. One of the most confusing Wing quirks.

**Re-amping workflow**
- Full signal path documented: Logic playback → amp sim bus → outboard → Ch18 → USR/8 → USB 3 → Logic
- Critical: USB 3 must be disabled after re-amping — outboard noise floor leaks through even when Ch18 is muted

**Documentation refactor**
- CLAUDE.md split into modular docs: commands.md, advanced.md, calibration.md, workflows.md, session-guide.md
- Reduced context window pressure — the AI reads only what it needs per task

---

## Day 6 — March 26: Outboard in the Recording Path (4 min)

### The recording captures the full processed chain now (V3)

**What changed**
- Bus 7 and Bus 8 now receive from the outboard RETURNS (Ch17/Ch18) instead of raw channels (Ch1/Ch2)
- Added GATE dynamics on Ch1 — noise/bleed control before outboard
- Added DE-ES dynamics on Ch17 — catches sibilance the compressors emphasize

**What gets recorded**
- Gate → HA73 EQ/color → WA76 compression → Opto/Distressor leveling → de-esser → tape emulation
- No reverb, no amp sims, no monitoring FX — just the processed outboard chain

**Guitar recording modes**
- With amp sim: Ch2 → Bus 5/6 → Bus 2 → outboard → recording
- Clean DI: Ch2 → Bus 2 direct → outboard → recording (amp sim bypassed)
- Toggle with one bus mute

---

## Day 7 — March 27: The Model 12 Revelation (8 min)

### The day the architecture had to change

**Tape returns — the original plan**
- All 10 Model 12 tracks wired back to Wing individually (Ch25-32)
- Permanent Loopback routing — bus sends configured per project
- Vocal tracks get reverb, guitar tracks get amp sim + reverb

**The critical discovery**
- Model 12 individual MTR playback tracks do NOT output over USB
- USB only carries: 10 analog channel inputs + stereo main mix (11/12)
- The USB send point in the signal path is before the MTR return — a hardware limitation
- This meant: you can record TO the Model 12, but you can't get individual tracks BACK from it over USB

**The pivot**
- Logic was already recording the same signal as a backup
- Logic has no track count limit — it just became the primary recorder
- The Model 12's role had to change completely

**Session lessons document created**
- Mandatory post-session updates — what broke, what was learned, what to never repeat
- Covers: noise floor (Main 1 trim at +18dB!), signal routing leaks (Bus 2 sending to Bus 3 bypassing outboard), gain staging (analog 6dB hotter than USB), Wing quirks (mute kills pre-fader sends, FX slot silent stealing)
- The AI reads this at the start of every session

**Architecture lesson from real tracking**
- Amp sim must go AFTER outboard, not before
- If amp sim is pre-outboard, it gets baked into the recording — can't change tone later
- New monitoring buses: Bus 10 Rhythm (RACKAMP), Bus 11 Lead (ANGEL) — post-outboard, monitoring only
- Recording captures outboard + tape. Monitoring adds amp sim on top. Independent paths.

---

## Day 8 — March 28: The Final Architecture (10 min)

### Logic Pro takes over as primary recorder
- Unlimited tracks, non-destructive editing, take comping, full undo
- Records the same signal: gate → outboard → de-esser → tape → Logic via USB
- Tape returns come from Logic (USB 17-26 → Wing Ch25-32), not Model 12
- Logic's "Software Monitoring" stays OFF — the Wing handles all monitoring

### 19 Mermaid signal flow diagrams
- Every signal path visualized: studio overview, vocal/guitar chains, recording vs monitoring, tape returns, patchbay, bus architecture, USB routing, re-amping, amp sim modes
- Troubleshooting flowcharts based on real incidents: noise floor, feedback loops, FX slot collisions
- Session setup checklist, architecture evolution timeline, gain staging reference
- Rendered PNG of the complete signal chain

### Model 12 becomes an analog mixing console
- Logic plays back all tracks through the Wing with FX
- Wing sends processed stems to Model 12 channels via USB
- Model 12 faders, EQ, and compression build the mix — hands on, like an SSL room
- Tracks 11/12 capture every mix pass automatically
- Takes stay in Logic — swap anytime, run the mix again
- This is exactly how professional studios work: DAW plays back, console mixes

### Mix monitoring solved
- Model 12 stereo main mix returns to Wing Ch7 via USB
- Solo Ch7 = hear only the Model 12 mix through headphones and speakers
- Un-solo = back to full tracking monitoring
- One button. No cable swapping. Wing is always the monitoring hub.
- GPIO port available for a physical button shortcut

---

## The Architecture Evolution — Recap (3 min)

| Version | Recorder | Model 12 Role | Tape | Amp Sim |
|---|---|---|---|---|
| V1 (Day 1) | Model 12 | Tape machine | Channel pre-inserts | Pre-outboard (Bus 5/6) |
| V2 (Day 4) | Model 12 | Tape machine | Recording buses | Pre-outboard (Bus 5/6) |
| V3 (Day 6) | Model 12 | Tape machine + backup | Recording buses, outboard in path | Post-outboard (Bus 10/11) |
| V4 (Day 8) | Logic Pro | Analog mixing console | Recording buses, outboard in path | Post-outboard (Bus 10/11) |

---

## By the Numbers (1 min)

- 10 pull requests merged
- ~40 commits across 8 days
- 3 major architecture pivots
- 19 signal flow diagrams
- 4 outboard compressors wired through 10 patchbay points
- 8 tape return channels from Logic
- 2 simultaneous outboard chains (vocal A side + guitar B side)
- 1 white noise incident
- 1 hardware limitation that changed everything
- 0 cables needed for default operation

---

## Closing (2 min)
- The studio that exists today was not planned on day one — it was discovered through real sessions and real failures
- Every mistake became a documented lesson. Every limitation became an architecture change.
- The AI assistant didn't just execute commands — it documented every decision, tracked every routing change, and proposed architectural solutions
- The gear is modest. The workflow is professional. The documentation is better than studios costing 100x more.
- Next up: first full song tracked, mixed on the Model 12, and mastered through the outboard chain
