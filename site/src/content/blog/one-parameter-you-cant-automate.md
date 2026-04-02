---
title: "Wing: The One Parameter You Can't Automate"
date: 2026-03-30
description: "In a studio where everything is scriptable, one critical routing parameter silently refuses to be set remotely."
tags: ["wing", "lessons", "workflow", "philosophy"]
hero: "/blog/one-parameter-you-cant-automate.svg"
---

We can control almost everything on the Wing without touching it. Faders, mutes, EQ curves, dynamics thresholds, FX models, bus routing, matrix assignments, channel names, colors, input sources, tap points -- all of it responds to commands sent over the network. We've built scripts that configure the entire console from scratch. We have an assistant that reads and writes parameters in real time. The whole studio philosophy is built on the idea that if a setting exists, we can script it, verify it, and reproduce it without walking across the room.

So when we found the one parameter that won't cooperate, it felt personal.

## The Setup

We wanted to set up a ducking sidechain. The compressor on one channel would listen to another channel's signal, so that when the vocal comes in, the guitar ducks out of the way. This is bread-and-butter mixing. Every console with a dynamics section supports it. The Wing supports it. The path to configure it is right there in the protocol documentation: set the sidechain source to an external channel instead of SELF, and the compressor starts listening to the other signal.

We sent the command. It accepted it. No error, no rejection. We queried the parameter back to confirm, and it read SELF. We sent it again. SELF. We tried the gate sidechain instead of the dynamics sidechain. Same behavior. We tried the other protocol -- TCP instead of UDP. SELF. We tried every variation of the source format we could think of. It always came back SELF.

## The Diagnostic Spiral

This is the kind of problem that eats an hour before you realize what's happening, because there's no error message. The console acknowledges the command. It doesn't complain. It just doesn't do it. It's like talking to someone who nods along and then does whatever they were going to do anyway.

We checked whether it was a permissions issue, a firmware version thing, a syntax problem. We read through the protocol header file and confirmed the parameter addresses exist. They do. They're enumerated right alongside every other dynamics parameter. The sidechain filter type, frequency, and Q all work fine remotely. You can shape what the sidechain hears. You just can't tell it what to listen to.

## The Answer

The sidechain source -- for both the dynamics processor and the gate -- can only be set from the Wing's touchscreen or through the Wing Edit desktop software. That's it. No OSC. No wapi. The parameter exists in the protocol. The address is valid. The console accepts the write. But the value doesn't stick. It's as if the firmware has a whitelist of parameters that can be modified remotely, and this one didn't make the cut.

We confirmed it by walking to the rack, tapping the screen, setting the sidechain source by hand, and watching it hold. The exact same parameter, set through the physical interface, works perfectly. Set it over the network, and it snaps back.

## Why It Matters

In isolation, this is a minor inconvenience. You set it once on the touchscreen, and it stays. It's not something you change mid-session.

But in a studio built around the principle that every parameter is scriptable, reproducible, and verifiable, one exception breaks the model. Our setup scripts can rebuild the entire console state from a config file -- except for this. Our snapshot verification can confirm every routing decision -- except this one. If we ever need to reset the board and restore from scratch, this is the one thing that requires a human hand on the screen.

It's a crack in the abstraction. And cracks have a way of becoming the thing you forget about at the worst possible moment.

## The Lesson

Every system has seams. Digital consoles present themselves as fully controllable, fully automatable, but somewhere in the firmware there are always decisions about what's exposed and what isn't. The parameter address exists. The protocol accepts the write. But the implementation quietly drops it on the floor. No error. No warning. Just a value that won't change.

We've added it to the list of things we verify by hand. Right next to "check that the send levels haven't reset themselves" and "confirm the mute button is doing what you think it's doing." The Wing keeps teaching us the same lesson: the protocol documentation tells you what you can say to the console. It doesn't always tell you what the console is willing to hear.
