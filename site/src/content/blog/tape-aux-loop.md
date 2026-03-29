---
title: "Building a Tape Saturation Loop with AUX 1"
date: 2026-03-28
description: "Using the Model 12's AUX 1 send to route through the Wing's TAPE effects and back — parallel tape saturation with per-channel control."
tags: ["tape", "effects", "model-12"]
---

We wanted tape saturation on the mix but didn't want to burn FX slots on every matrix. The solution: use the Model 12's AUX 1 as a tape send, route it through the Wing's TAPE effects, and return it on a spare channel.

## The Signal Path

```
Model 12 AUX 1 Out (pre-fader)
  → TRS-to-XLR cable
  → Wing LCL 3 (gain 10dB, phantom OFF)
  → Ch33 Tape Send
    pre-insert: FX13 TAPE (drive 10, speed 30)
    post-insert: FX6 TAPE-DL (flutter 55, no feedback)
  → USR/3 (POST tap)
  → USB 38
  → Loopback
  → Model 12 Ch 6
```

Each Model 12 channel has an AUX 1 knob. Turn it up to send more of that instrument to the tape. Ch 6 fader controls the return level. It's parallel processing — the dry signal and the tape return coexist.

## The Gotchas

**Phantom power.** LCL 3 was previously used for condenser mics. It had 48V phantom and 37.5dB gain. Plugging a line-level output into that was... noisy. Always check phantom power and gain when repurposing Wing inputs.

**Drums don't work.** The USB round-trip adds a few milliseconds of latency. On sustained sounds like guitar and vocals, it's inaudible. On drums, those few milliseconds create an audible slapback on every transient. Keep AUX 1 down on the drum channel.

**It's mono.** AUX 1 sums to mono before sending. The tape return on Ch 6 is center-panned. At high return levels, it pulls stereo content toward center. Keep the blend modest.

## The USR Tap Lesson

We initially set USR/3 to PRE tap, which captures before the post-insert. The TAPE-DL on the post-insert was completely bypassed. Switching to POST tap captured the full chain — both TAPE and TAPE-DL.

Rule: USR PRE = before post-inserts. USR POST = after everything.
