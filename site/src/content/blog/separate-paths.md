---
title: "Separate Paths: Why Recording and Monitoring Divorced"
date: 2026-03-27
description: "Recording and monitoring used to share a signal path. Splitting them apart was the biggest architecture decision in the studio's first week."
tags: ["workflow", "recording", "philosophy", "outboard"]
hero: "/blog/separate-paths.svg"
---

For the first few days the studio was running, everything shared a bus. The guitar came in, hit the amp sim, went through the outboard chain, and the same signal fed both the recorder and the headphones. One path, one sound, one bus. Simple.

Too simple, as it turned out.

## The Problem with Sharing

We wanted the recordings to capture what the outboard does to the signal — the Neve-style preamp color, the 1176 compression, the Distressor's harmonic grit — and nothing else. That's the whole point of printing outboard. The character is baked in, committed, part of the performance.

But the amp sim was on the same bus. Which meant the recording also captured the amp sim. And amp sims are the opposite of outboard — they're decisions you want to keep changing. Different songs call for different amp sounds. Different sections of the same song might want a cleaner tone or a dirtier one. If the amp sim is printed to the recording, you're stuck with whatever you picked in the moment.

We were also hearing the amp sim twice during overdubs. The original take had the amp sim baked in. Then during playback, the tape return went through the monitoring path — which had the same amp sim on it. Double processing. The guitar sounded like it was behind two layers of glass.

## The Insight

The fix seems obvious in hindsight: recording and monitoring need to be completely separate signal paths. The recording bus captures what comes out of the outboard and nothing else. The monitoring bus takes that same outboard return and adds whatever the musician needs to hear — amp sims, reverb, whatever makes the performance feel good in the headphones.

Two buses. Two jobs. No overlap.

The recording path captures gate, preamp color, compression, de-esser. That's it. Clean outboard signal, ready for mixing. The monitoring path takes the outboard return and routes it through an amp sim so the guitarist hears an amp tone while playing. But that amp tone never touches the recording.

## What Actually Changed

Before the split, the signal went: guitar in, amp sim bus, outboard chain, single bus that fed both the recorder and the headphones. One path doing two things.

After the split, the guitar still goes through the outboard chain the same way. But the outboard return now feeds two independent destinations. One goes straight to the recording bus — no amp sim, no effects, just the pure outboard signal. The other goes to a monitoring bus where the amp sim lives, and that bus only goes to headphones.

The recording bus captures what the outboard does to the sound. The monitoring bus adds what the musician needs to hear while playing. They never cross.

## The Unexpected Benefits

Once recording and monitoring were separate, a bunch of things got easier.

Switching amp sims mid-session became free. Want to try a different amp tone for the chorus? Change the monitoring bus. The recording doesn't care — it's still capturing the same outboard signal. You can audition ten different amp sounds without recording ten different takes.

We also set up separate monitoring buses for rhythm and lead guitar. Instead of swapping one amp sim back and forth, there's a clean rhythm tone on one bus and a high-gain lead tone on another. Toggle between them instantly. Each has its own character dialed in, and neither affects what gets recorded.

Playback stopped sounding weird, too. When a recorded take plays back during overdubs, it goes through the monitoring amp sim once — which is exactly what the guitarist heard while playing. No double processing. The take sounds the same on playback as it did live.

## The Deeper Lesson

This was the first week of the studio being operational, and the biggest lesson was about separation of concerns. Every signal path should have one job. The moment a bus is trying to serve two masters — the recorder and the headphones — you lose the ability to change one without affecting the other.

It's the same principle as printing outboard. Commit the things that define the sound. Keep the things that are preferences flexible. Outboard compression shapes the performance — commit it. Amp sim flavor is an aesthetic choice — keep it in monitoring where you can change your mind.

The studio architecture now treats recording and monitoring as two completely independent systems that happen to share the same source. The outboard chain is the bridge between them. Everything upstream of the outboard is shared. Everything downstream is separate.

We spent most of a session rewiring buses and testing signal paths to get here. It wasn't glamorous work. But every session since has started with the same clean separation, and the recordings have been better for it. Not because the signal sounds different — the outboard chain hasn't changed — but because we stopped accidentally printing things we didn't mean to keep.
