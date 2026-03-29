---
title: "Four Feedback Loops in One Week"
date: 2026-03-27
description: "Digital white noise, reverb leaks, phantom outboard hiss, and USB crosstalk — each one a different animal."
tags: ["lessons", "routing"]
hero: "/blog/feedback-loops.svg"
---

The studio was barely a week old when I hit four distinct feedback loops. Not the musical kind where you lean a guitar into an amp. The ugly kind, where digital audio eats its own tail and screams at you through the monitors.

## The White Noise Wall

The first one was the worst. Full-bandwidth digital white noise, every channel, all at once. The kind of sound that makes you rip your headphones off before you even think about what happened.

The cause was embarrassingly simple. The audio interface was set as both the source and the monitor in the routing software. It was sending audio out over USB and then listening to what came back on the same USB connection. A perfect digital circle. The signal went out, came back, went out again, and within milliseconds it was just noise at full level. Fix: pick one role. Source only. Never both.

## The Reverb Leak

This one was subtle. The guitar send — the bus that feeds the outboard chain — had a send to the reverb bus. Sounds innocent enough, except that send was bypassing the entire outboard chain. Raw amp sim signal was leaking straight into the reverb, which was mixed into the monitors. So you had this ghostly version of the guitar living in the reverb that had nothing to do with the processed sound. It made the guitar feel wide and unfocused in a way that was hard to diagnose until I traced the signal path back and found the stray send sitting at unity gain.

## The Hiss That Wouldn't Die

Outboard gear has a noise floor. Four boxes chained together have a noticeable one. That's fine when you're tracking — the signal buries it. But I had the return channels live on the main mix even when nobody was playing. All that analog hiss was sitting right there in the monitors. Worse, a bus compressor on the main was boosting quiet signals, which made the hiss even more present.

The fix was discipline: take the outboard returns off the main bus when you're not tracking. The channels stay active so the recording path works, but the noise doesn't reach the monitors. And that bus compressor got disabled permanently.

## The USB Ghost

This one haunted us during re-amping. We'd process a dry recording back through the outboard chain and capture the result on a separate USB output. That worked fine. But after the re-amping pass, nobody turned off that USB output. The outboard's noise floor kept flowing through it — not loud, but present. And because it was feeding back into the recorder, it was technically a loop. Not a howling, runaway loop, but a persistent low-level leak that colored the silence between takes.

The rule now: that USB output gets killed the moment re-amping is done. No exceptions.

## The Common Thread

Every one of these had a different cause and a different fix, but they shared one thing: a signal path that existed when it shouldn't have. The studio's routing is powerful enough to connect almost anything to almost anything else. That's a feature right up until you create a circle. Now we check every path before we print, and we kill every route we're not actively using.
