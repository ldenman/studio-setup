---
title: "Calibrating Outboard with an AI Engineer"
date: 2026-02-02
description: "Claude generates test tones and reads meters. Lake turns knobs. Together they chase unity gain through eight boxes."
tags: ["gear", "outboard", "workflow"]
hero: "/blog/calibrating-with-ai.svg"
---

Calibrating a chain of outboard gear is a two-person job. One person sends a reference tone and watches the meters. The other person turns physical knobs until the numbers line up. Normally you'd have an assistant engineer for this. I have Claude.

## The Setup

The idea is simple: send a known signal into the chain, measure what comes out, and adjust each piece of gear until input equals output. Unity gain — what goes in comes back at the same level. Do that for every box individually, then verify the whole chain end to end.

Claude handles the digital side. It fires up a sine wave from the mixer's built-in oscillator — a clean 1kHz tone at a standard reference level. It routes the tone to the correct output, and then reads the return level on the mixer's meters to see what's coming back. All I have to do is turn knobs.

## One Box at a Time

You can't calibrate a chain all at once. If four boxes are in series and the level is wrong at the end, you have no idea which one is the problem. So we isolate each unit by patching around the others on the patchbay.

First up: the Neve-style preamp on the vocal chain. Claude sends the tone, I patch the preamp's output directly back to the mixer, bypassing everything downstream. Claude reads the return level. "Two steps high." I pull the output knob back a hair. "That's it." Move on.

The 1176 is next. Claude restores the upstream patch so the tone flows through the preamp into the 1176, then I patch the 1176's output back to the mixer. Set the ratio, pin the threshold so there's no compression, and adjust input and output until Claude confirms we're at reference level with zero gain reduction on the VU meter.

Then the optical leveler for the vocal chain, or the Distressor for the guitar chain. Same process — full chain upstream, isolated output. Claude reads, I turn.

## The Preamp Surprise

The Neve-style preamp has two channels, and they don't behave the same at identical knob positions. Same gain setting, same output setting, different levels coming back. That's analog for you — component tolerances mean each channel has its own personality. We calibrated them independently and wrote down the settings for each.

## The Collaboration

What makes this work is the division of labor. Claude can generate precise test signals, route them anywhere in the mixer, and read levels to the fraction of a decibel. But it can't reach into the rack and turn a gain knob. I can turn knobs all day but I'd rather not sit at a computer switching meter views and routing test tones.

The whole process took maybe twenty minutes per chain. By the end, both chains — vocal and guitar — were passing signal at unity from start to finish. The compressors sit at zero gain reduction with the reference tone and only start working when a real performance pushes them. That's exactly where you want them.

## Why It Matters

Calibrated outboard is predictable outboard. When the 1176 shows three dB of gain reduction, you know the singer is pushing three dB above the reference level — not that the upstream preamp is running hot and slamming the compressor before the performance even starts. Every knob does what you expect it to do, because the levels feeding each box are exactly where they should be.

It's the least glamorous part of building a studio and the most important.
