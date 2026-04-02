---
title: "Wing: Solo Doesn't Mean Alone"
date: 2026-03-31
description: "We solo'd a channel expecting silence from everything else. The buses had other plans."
tags: ["wing", "lessons", "mixing", "routing", "model-12"]
hero: "/blog/solo-doesnt-mean-alone.svg"
---

We were deep into a mix, comparing the Model 12's stereo output against the individual stems feeding it. Simple diagnostic move: solo Ch7, the channel carrying the Model 12's mix back into the Wing, and listen to just that. Except when we hit solo, we didn't hear just that. We heard everything.

Not everything on every channel -- the solo did its job on the other channels. But the buses kept right on playing. Every bus assigned to Main was still dumping signal into our headphones, layered on top of the supposedly solo'd channel. The whole point of soloing was to isolate, and we were hearing a mess of overlapping signals with no way to tell what was coming from where.

## The Assumption

Solo, on any console we've ever used, means "let me hear this one thing." It's the most basic troubleshooting move in mixing. Something sounds off, you solo channels until you find it. The implicit promise is that everything else goes quiet.

On the Wing, channels honor that promise. Solo a channel and every other channel drops out. But buses don't participate in the solo system at all. If a bus is assigned to Main, it stays on Main regardless of what you've solo'd. It doesn't matter that you only want to hear one channel. The buses aren't listening.

## Why It Matters During Mixing

During tracking, this quirk is mostly invisible. The buses carrying amp sims, outboard sends, and effects all need to be on Main because they're part of the monitoring path. You're hearing everything together anyway. Solo isn't really part of the tracking workflow.

But mixing is different. During mixing, the Wing is sending processed stems out through matrices to the Model 12, and the Model 12 sends its stereo mix back on Ch7. The only thing that needs to be on Main is Ch7 -- that's what we're monitoring. If the amp sim buses, the effects buses, and the outboard return buses are all still assigned to Main from the tracking session, they're all still audible. Solo doesn't help because solo can't touch them.

We spent longer than we'd like to admit trying to figure out why the solo'd channel sounded so thick and layered. It wasn't a processing issue. It wasn't bleed. It was half a dozen buses happily summing into Main, completely ignoring the fact that we'd asked to hear one channel in isolation.

## The Fix

Once we understood what was happening, the fix was straightforward: take every bus off Main when mixing. During mixing, the buses are feeding matrices that route to the Model 12 -- they have no business being on Main. Only Ch7, the Model 12's stereo return, belongs on Main during a mix session.

We'd been leaving the buses on Main out of laziness, really. The tracking setup had them there, and when we transitioned to mixing, we just started mixing without cleaning up the monitoring path. The buses weren't hurting anything obvious -- until we tried to solo.

Now the transition from tracking to mixing includes a step: pull all buses off Main. It takes a few seconds, and it means solo actually works the way you'd expect. More importantly, it means the only thing on Main during mixing is the actual mix -- no stale bus signals sneaking in and coloring what we hear.

## The Pattern

This is the third time the Wing has taught us that a familiar control doesn't work quite the way we assumed. Mute kills pre-fader sends. Pre-fader sends aren't really pre-mute. And now: solo doesn't affect buses. Each one is a small thing, and each one is completely logical once you know the rule. The problem is that nobody tells you the rule. You find out when something sounds wrong and you don't know why.

We're building a mental model of this console one surprise at a time. And every surprise gets written down, because the worst version of these lessons is learning them twice.
