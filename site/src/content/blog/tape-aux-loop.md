---
title: "The Tape Saturation Experiment"
date: 2026-03-28
description: "We tried building a hardware tape saturation loop using the Model 12's aux send. It worked — until it didn't."
tags: ["tape", "effects", "lessons"]
hero: "/blog/tape-aux-loop.svg"
---

*Updated March 29: This approach was later replaced by software tape emulation in Logic (T-RackS Tape Machine). The hardware loop worked but introduced phase issues on percussive material that we couldn't live with. Kept here as a record of the experiment.*

---

We wanted tape saturation on the mix without burning through effects slots on every channel. The idea: use the Model 12's aux send as a tape bus, route it through the Wing's tape emulation effects, and return it on a spare channel. Each instrument gets its own send knob — turn it up for more tape character.

## How It Worked

The aux send on the Model 12 is pre-fader and per-channel. The signal leaves the Model 12, enters the Wing on a dedicated channel with tape saturation and tape delay effects, then returns to the Model 12 on a spare fader. It's parallel processing — the dry signal and the tape-colored signal coexist. Blend with the return fader.

## Where It Fell Apart

**Drums exposed the latency.** The digital round-trip through USB adds a few milliseconds of delay. On sustained sounds — guitar, vocals, bass — it's inaudible. On drums, those few milliseconds create a slapback on every transient. The kick gets a flam. The snare doubles. You can't fix it; you can only avoid sending drums to the tape bus.

**The aux is mono.** Everything sums to a single channel before it leaves the Model 12. The tape return sits dead center. At higher blend levels, it pulls the stereo image inward. You have to keep the blend modest or accept the narrowing.

**Phase is phase.** Even on sustained sounds, a parallel path with latency is a parallel path with latency. The comb filtering is subtle, but it's there. Once we heard it, we couldn't unhear it.

## What We Learned

The experiment proved the concept — per-instrument tape saturation with a single send knob is a great workflow. But the implementation needed to move to software, where the tape effect sits directly on each track with no round-trip delay and no phase issues. Same creative result, cleaner execution.

Sometimes the best hardware solution is knowing when to use software instead.
