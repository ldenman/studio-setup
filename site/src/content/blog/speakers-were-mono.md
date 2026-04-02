---
title: "Wing: The Speakers Were Mono and Nobody Noticed"
date: 2026-03-31
description: "Both studio monitors were playing the left channel for weeks. We didn't catch it because mono sounds perfectly fine — which is exactly the problem."
tags: ["wing", "lessons", "routing", "mixing"]
hero: "/blog/speakers-were-mono.svg"
---

We'd like to tell you we caught this one quickly. We didn't. For an embarrassingly long stretch of time, both of our studio monitors were playing the exact same channel — the left side of the monitor matrix — and we had no idea. Everything sounded normal. That's the whole problem.

## Two Speakers, One Signal

The monitor path in our studio runs through MX1, the monitor matrix on the Wing. MX1 produces a stereo pair — left on output 1, right on output 2 — which feeds Out 7 and Out 8, the physical outputs wired to our left and right speakers. Simple enough. Except both Out 7 and Out 8 were set to `in=1`. Both outputs were pulling from MX1's left channel. The right speaker was faithfully reproducing the left side of the mix, and the left speaker was doing the same, and together they were giving us a perfectly listenable, perfectly centered, perfectly wrong picture of whatever we were working on.

## Why We Didn't Notice

This is the part that stings. Most of what we work with is mono. A single vocal mic. A guitar DI. A bass line from a session player. When your sources are mono, they sit dead center in the stereo field regardless of whether your monitoring is actually stereo. A mono source panned center sounds identical on a true stereo pair and on two speakers playing the same channel. There's literally no difference to hear.

Even our stereo sources didn't tip us off immediately. Reverb tails, stereo delays, the occasional keyboard pad — these things add width, but if you're not actively listening for width, you don't miss it. The mix sounds complete. It sounds balanced. It has the right amount of everything. You just can't tell that the delay you panned hard right is also coming out of the left speaker, because your brain fills in the expectation of stereo when the phantom center is strong enough.

We were making mix decisions — panning decisions, stereo effect decisions, spatial balance decisions — while listening to a monitoring rig that threw away every bit of left-right distinction. Not because the mix was wrong, but because the speakers were lying about what the mix contained.

## The Indexing Error

The cause was a stereo indexing mistake. MX1 has two outputs: index 1 is left, index 2 is right. When we configured Out 7 and Out 8, we set both to `in=1`. That's it. A single wrong number on a single output assignment, and the entire monitoring path collapses to mono.

This is the same category of mistake we've hit with USR routing, where the difference between `in=1` and `in=2` is the difference between tapping the left side and the right side of a stereo signal. Digital consoles are full of these numbered assignments where a one-digit error doesn't produce silence or distortion or any obvious symptom. It just quietly gives you the wrong signal, and the wrong signal sounds close enough to right that you keep working.

The fix took about five seconds. Out 7 stays at `in=1` for MX1 Left. Out 8 gets changed to `in=2` for MX1 Right. Suddenly the speakers are actually stereo. Panning works. The reverb has width. The delay you put on the right side is actually on the right side.

## The Hard-Left Test

We now have a rule for any stereo pair in the studio, whether it's speakers, headphones, or a stereo bus feeding an output. After configuring it, we pan a source hard left and walk over to the speakers. The left speaker should be making sound. The right speaker should be silent. Then pan hard right and check the opposite.

It takes ten seconds and it catches exactly this kind of mistake. If both speakers make sound when the source is panned hard left, something in the chain is summing or miswired or — as in our case — both outputs are pulling from the same index.

The broader pattern here is that the most dangerous mistakes aren't the ones that sound broken. A feedback loop screams at you. A dead channel is obviously dead. A missing phantom power supply gives you nothing and you know it immediately. But a stereo pair that's been silently collapsed to mono? That sounds like music. It sounds fine. It sounds like everything is working. And you can go weeks without questioning it, making decisions based on a signal that's missing half its information, never suspecting a thing.

We suspect a lot of home studios are running mono right now and don't know it. Pan something hard left. Check which speaker moves. You might be surprised.
