---
title: "One Button Between Two Worlds"
date: 2026-03-25
description: "The solo button trick that lets you switch between tracking and mixing monitoring without touching a cable."
tags: ["workflow", "mixing", "model-12", "lessons"]
hero: "/blog/solo-button-monitor-switch.svg"
---

There's an annoying moment in every session where the studio changes modes. You've been tracking — headphones plugged into the Wing, hearing yourself live through the outboard chain with playback from Logic underneath. Then it's time to mix. The mix lives on the Model 12 now, summed through real faders, and you need to hear *that* instead.

The obvious answer is to swap your headphones to the Model 12's headphone jack. Or run a cable. Or set up some elaborate routing scheme with a monitor controller. All of these work. None of them are elegant.

## The Setup

The Model 12's stereo main mix already comes back to the Wing. It arrives on Ch7 via USB — the Model 12's output goes through Loopback, which feeds USB inputs 3 and 4 on the Wing. That channel exists for exactly this kind of utility. It sits there quietly, fader down, not contributing to Main 1 during tracking.

The trick is what happens when you solo it.

## Solo as a Monitor Switch

Solo on the Wing does exactly what you'd expect — it isolates a channel so that's all you hear. Hit solo on Ch7, and your headphones switch from the full tracking mix to the Model 12's stereo output. Un-solo, and you're back to hearing everything: live inputs, tape returns, session players, the whole tracking world.

One button. No cable swapping. The Wing stays as the monitoring hub for both modes.

This works for the speakers too, which is the part that surprised us. Matrix 1 drives the speaker feed, and it sources from the monitor phones output. When you engage solo, the monitor section automatically switches to the solo bus. So the speakers follow the same toggle — solo Ch7 and the room fills with the Model 12 mix. Un-solo and you're back to tracking monitoring.

## The Footswitch Option

Here's where it gets fun. The Wing has four GPIO ports on the back — physical connectors for external switches. Plug a momentary footswitch into GPIO 1, assign it to toggle Ch7's solo state, and you've got a hands-free monitor switch on the floor next to your pedalboard.

You're sitting at the Model 12, adjusting faders, and you want to check how the mix sounds through the Wing's monitoring chain and the studio speakers. Tap the footswitch. Listen. Tap again, back to tracking. No reaching for the console, no mouse clicks, no menu diving.

## The Honest Caveat

There's latency on this path. The signal goes from the Model 12 into the computer via USB, through Loopback, and back out to the Wing on another USB stream. That's a round trip through the operating system's audio engine. You'll hear it if you're listening for it — a few milliseconds of delay that adds up to a slightly soft, slightly late feel.

For mixing, this doesn't matter. You're adjusting faders and listening to balances, not playing an instrument in time. The latency doesn't affect your judgment about whether the vocal is too loud or the reverb tail is too long.

For truly zero-latency mixing monitoring — if you're doing critical ear training or A/B comparisons where timing precision matters — use the Model 12's own headphone jack. It's direct analog, no conversion, no round trip. That's the reference path.

But for the constant back-and-forth of a working session, where you're bouncing between tracking a new part and checking the mix so far? The solo button is faster than swapping headphones, and the latency is irrelevant.

## The Bigger Pattern

This is a small example of a bigger idea in the studio: the Wing is always the monitoring hub. Everything passes through it — live instruments, tape returns, session players, and now the Model 12's mix output. That means one pair of headphones, one volume knob, one place to control what you hear.

The alternative is scattered monitoring: one headphone jack for tracking, another for mixing, a third for checking the raw Model 12 output. You'd spend half the session managing cables and remembering which output you're plugged into.

One hub. One solo button. Two worlds.
