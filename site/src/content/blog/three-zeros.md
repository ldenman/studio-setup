---
title: "The Three Zeros"
date: 2025-12-15
description: "Zero latency, zero comb filtering, zero unnecessary noise — the three rules that survived contact with reality."
tags: ["philosophy", "lessons", "workflow", "routing"]
hero: "/blog/three-zeros.svg"
---

Every routing decision in this studio gets run through the same three questions. Does this add latency? Does this create a parallel path? Does this add noise? If the answer to any of them is yes, the decision gets rethought. No exceptions, no "it's probably fine."

These aren't principles we started with. They're principles we arrived at, the hard way, after enough sessions went sideways that patterns emerged. Each one was earned by a specific failure.

## Zero Latency

The musician hears everything in real time. Not "nearly" real time. Not "low enough latency that you won't notice." Zero. The Wing handles all monitoring, and the signal from the microphone or guitar hits the headphones through an analog-to-digital-to-analog path that happens inside the mixer hardware. No round trip through the computer. No plugins in the recording input path. Logic's Software Monitoring is off.

This matters because latency is cumulative and it's invisible. A musician can't point to it and say "that's the problem." They just feel slightly disconnected from their instrument. The vocal comes back a few milliseconds late and their pitch drifts because their ears and their throat disagree about timing. The guitarist's attack feels soft because the transient in the headphones arrives after the pick has already left the string. You can't practice your way around physics.

We learned this one early. Logic's Software Monitoring was on during a tracking session, and the vocalist kept asking to turn up the headphone level. It was already loud. The problem wasn't volume — it was timing. The direct signal from the mic bleed and the monitored signal from Logic were arriving at different times, and the brain was interpreting that conflict as "not loud enough." Turning off Software Monitoring and letting the Wing handle it solved it instantly. The vocalist's pitch tightened up on the very next take without anyone mentioning it.

The rule is simple: the Wing owns monitoring. Logic is a tape machine — it records what it's given, plays back what it has, and never inserts itself into the live signal path.

## Zero Comb Filtering

One signal path per source. No parallel routes where the same signal arrives at the same destination at different times. No send-and-return loops that add round-trip delay. If the same audio shows up twice, one of those paths is wrong and needs to be removed.

Comb filtering is what happens when two copies of the same signal arrive slightly out of phase. Some frequencies reinforce, others cancel. The result sounds thin, hollow, like the audio is coming through a cardboard tube. It's subtle enough that you might not identify it immediately, but obvious enough that you know something is wrong.

We built a tape saturation loop using the Model 12's aux send. The idea was elegant: send any channel's signal out through the aux bus, through the Wing's tape emulation effect, and back to a return fader on the Model 12. Parallel processing — blend to taste. It worked beautifully on guitars, bass, vocals. Sustained sounds loved it.

Then we sent drums through it, and every hit had a flam. The round trip through USB added a few milliseconds of delay, which meant the dry signal and the saturated signal arrived at slightly different times. On a sustained guitar note, a few milliseconds is inaudible. On a snare hit, it's a slapback that makes the drummer sound like they can't keep time.

But the real problem was deeper than drums. Even on sustained material, the parallel path was creating comb filtering. We just couldn't hear it as obviously. Once we measured it, the phase cancellation was there on everything — subtle notches in the frequency response that made the mix sound slightly hollow. We killed the hardware loop and moved tape saturation to software, where it sits directly on each track with zero round-trip delay.

The rule: every source gets one path to every destination. If you need processing, it goes in series — not in parallel with a delayed copy.

## Zero Unnecessary Noise

Every active channel, every unmuted bus, every enabled effect contributes to the noise floor. The noise floor is not a fixed property of the gear — it's a stack of small decisions, and most of them are mistakes left over from previous sessions.

We found the master output trim set to +18dB once. That's not a trim. That's a multiplier. Everything on the main bus — signal and noise alike — was being amplified by a factor of eight before it hit the monitors. The hiss was obvious, but the cause wasn't, because who checks the master trim? It's supposed to be at zero. Someone had cranked it during a troubleshooting session and never put it back. Two seconds to fix, once we found it. But it had been coloring every monitoring decision for days.

That discovery kicked off an afternoon of noise hunting that found three more sources: a bus compressor boosting silence between takes with its makeup gain, phantom power left on a line input from a previous session with the preamp still cranked to +37dB, and a ghost channel from a previous session still assigned to a USB input that was carrying a different signal. Four layers of noise, each one small, together enough to make the monitors sound tired.

Now there's a checklist. At the start of every session: master trim at zero. No stray processing on the main bus. Phantom power off on every input that doesn't need it. Every active channel audited — if it's not doing something right now, it gets muted or its input gets cleared. Outboard returns come off the main bus when they're not tracking. The re-amp output gets disabled when nobody's re-amping, because the outboard noise floor leaks through it even when the return channel is muted. Unused effects get bypassed.

The rule: if it's not contributing signal, it's contributing noise. Turn it off.

## The Filter

These three rules aren't a philosophy we adopted. They're a filter we apply. Every time the studio architecture changes — a new effect gets added, a bus gets rerouted, a channel gets repurposed — the change goes through the same three questions.

Does this add latency to the monitoring path? Then it can't be in the monitoring path.

Does this create a second route for the same signal? Then one of the routes needs to go.

Does this leave something active that doesn't need to be? Then it gets turned off.

It sounds rigid, and it is. But rigidity is the point. A studio that's "flexible" about its noise floor is a studio that hisses. A studio that's "relaxed" about parallel paths is a studio with comb filtering it hasn't noticed yet. A studio that tolerates a little monitoring latency is a studio where the musicians never quite feel locked in, and nobody can explain why.

The three zeros aren't goals. They're constraints. And like all good constraints, they don't limit what the studio can do. They limit what it's allowed to do badly.
