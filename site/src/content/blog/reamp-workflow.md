---
title: "The Re-Amp Workflow: Processing Yesterday's Take"
date: 2026-03-28
description: "You recorded dry. Now you want it through the outboard chain and amp sims. Here's how we send a track back through the studio — and the one thing you absolutely must turn off when you're done."
tags: ["workflow", "outboard", "recording", "gear", "lessons"]
hero: "/blog/reamp-workflow.svg"
---

There's a moment in every session where you listen to yesterday's dry guitar take and think: that needs to go through the real gear. Not a plugin. Not a preset. The actual outboard chain -- the preamp, the compressor, the Distressor -- with an amp sim in front of it, all hitting the iron and the transformers in real time.

That's re-amping. And in a studio where the outboard chain is permanently wired and normalled, it's one of the most satisfying things you can do. You get a second chance at the tone without re-playing the part.

## The Setup

The idea is simple. Play a previously recorded track back out of the recorder, route it through the same signal chain you'd use for a live performance, and capture the processed result on a new track. Same outboard, same amp sims, same analog character -- just applied after the fact instead of during the take.

Here's why that matters. When we're tracking, there's pressure. The musician is in the zone, the arrangement is coming together, and the last thing you want to do is spend twenty minutes dialing in an amp sim tone. So we record dry -- clean signal, full dynamic range, no processing baked in. We can always process it later, and "later" is re-amping.

## The Signal Path

The dry track lives in the recorder. We solo it so it's the only thing playing back, and it arrives at the Wing on a dedicated tape playback channel. From there, we send it to the amp sim bus -- the same bus that handles the live electric guitar signal. The amp sim shapes the tone, and then the signal flows to the outboard send bus, which routes it out of the Wing and through the physical gear.

The outboard chain is where the magic happens. The HA73 preamp/EQ adds harmonic richness and lets us shape the frequency balance. The 1176 compressor grabs the transients and adds that characteristic push. The Distressor does whatever the Distressor does -- which varies from "gentle thickening" to "aggressive character" depending on where the attack knob lands. By the time the signal comes back into the Wing on the processed return channel, it sounds like a completely different recording.

We capture the processed signal through a virtual patch point that taps the return channel and routes it to a USB output, which loops back into the recorder on a fresh track. One pass, and we've got a fully processed version sitting right next to the original dry take.

## Dialing It In

The beauty of re-amping is that you can play the same passage over and over while you adjust the chain. During a live take, you get one shot at the amp sim settings, one shot at the compressor threshold, one shot at the EQ. If the tone isn't right, you need another take. With re-amping, you hit play, listen, tweak a knob on the HA73, hit play again. The performance is locked. Only the processing changes.

We usually start with the amp sim. The difference between a rhythm tone and a lead tone isn't subtle -- it's a completely different amp model, different gain structure, different feel. Once the amp character is right, we move to the outboard. The 1176 ratio and attack time determine how the pick dynamics translate. Fast attack smooths everything out, which works for rhythm parts where you want consistency. Slower attack lets the initial transient through, which gives lead lines more presence and bite.

The Distressor is the wild card. We've had sessions where it barely touches the signal -- just a hint of warmth from the input transformer -- and sessions where it's doing serious work, adding grit and compression that makes a clean recording sound like it was tracked through a cranked tube amp. It depends entirely on the song.

## The Cleanup Nobody Tells You About

Here's the part that bit us. After re-amping, there's a USB output carrying the processed signal from the return channel back to the recorder. That output taps the return channel at a point that's independent of the channel's mute state. So even after you mute the return channel, even after you stop playback, that USB output is still live. And the outboard chain has a noise floor.

It's not loud. It's the kind of low-level hiss that you'd never notice during playback, because the music masks it completely. But between takes, or in quiet passages, or when you're recording something else entirely -- it's there. A subtle, persistent noise floor leaking through an output you forgot about, mixing into whatever you're recording next.

The fix is to disable that USB output entirely after the re-amp pass. Not mute the channel. Not pull down the fader. Actually turn off the output assignment. Because anything short of that leaves the outboard noise floor connected to the recorder, and the next time you wonder why there's a faint hiss on an otherwise clean vocal take, this is probably why.

We learned this the annoying way. Spent time chasing a noise floor issue that turned out to be the re-amp output from two days earlier, still active, still carrying the hiss of three pieces of outboard gear sitting at idle. Now it's part of the workflow: re-amp, capture the take, disable the output, verify silence. Every time.

## Why Not Just Use Plugins?

Fair question. There are excellent amp sim plugins, excellent compressor emulations, excellent everything-emulations. And we use them -- tape saturation, for instance, lives entirely in software. But the outboard chain does something that plugins approximate but don't replicate. It's the interaction between the pieces. The way the HA73's output stage reacts differently depending on what the 1176 is doing downstream. The way the Distressor's harmonics change based on the signal level hitting it, which is affected by every piece of gear upstream.

Plugins model each piece in isolation. Hardware creates a system where everything affects everything else. That's not better in some absolute sense -- it's a different character. And re-amping lets us apply that character deliberately, without the pressure of a live take, with the ability to fine-tune until it's exactly right.

The dry recording is the safety net. The outboard chain is the instrument. Re-amping is how we play it.
