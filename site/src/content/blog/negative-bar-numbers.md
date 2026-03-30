---
title: "Negative Bar Numbers"
date: 2026-03-29
description: "Press play on the Model 12 and Logic jumps to bar negative nine. An old broadcast convention almost derailed our first synced session."
tags: ["lessons", "workflow", "model-12"]
hero: "/blog/negative-bar-numbers.svg"
---

We pressed play on the Model 12 and Logic Pro jumped to bar negative nine. Not bar one. Not even bar zero. Bar negative nine. The transport was rolling, the timecode was flowing, and Logic was convinced we were somewhere before the beginning of time.

## The Setup

The Tascam Model 12 is our transport master. It sends MTC — MIDI Timecode — over USB to Logic Pro. The idea is simple: press play on the hardware, the software follows. One transport to rule them all. The Model 12 owns the timeline, Logic just rides along and provides session players for the backing track.

We'd spent an afternoon getting the sync settings dialed in. Logic was receiving MTC, the sync indicator was locked, everything looked right. Then we hit play and watched Logic's transport display a bar number that shouldn't exist.

## An Hour Early

Here's what was happening. The Model 12 starts its timecode at `00:00:00:00` — midnight, zero hours, zero minutes, zero seconds, zero frames. That's where you'd expect a timeline to begin. Sensible.

But Logic had a different opinion about where bar one lives. Deep in its project settings, under Synchronization, there's a field called "Bar Position 1 1 1 1 plays at SMPTE." Logic's default for that field is `01:00:00:00`. One hour. Not zero. One.

So when the Model 12 said "we're at zero," Logic did the math: if bar one doesn't start until the one-hour mark, and we're currently at zero hours, then we must be... an hour before bar one. Which works out to roughly bar negative nine, depending on tempo. Logic wasn't broken. It was faithfully calculating its position based on a disagreement about where the timeline starts.

## Why One Hour?

This is where it gets interesting. The one-hour offset isn't a bug and it isn't arbitrary. It comes from the film and broadcast world, where SMPTE timecode has been the standard since the 1960s.

In a film post-production environment, the day's work might span multiple reels of tape. Engineers needed a way to distinguish between them. The convention was to start each reel at a different hour: reel one at `01:00:00:00`, reel two at `02:00:00:00`, and so on. The zero hour — `00:00:00:00` — was reserved for pre-roll, slate information, tone, and other technical material that comes before the actual program content. Starting your show at zero was considered bad practice because it left no room for that preamble.

This convention got baked into every piece of professional audio software. Pro Tools does it, Logic does it, Nuendo does it. If you've ever opened a new session in any major DAW and noticed the timeline doesn't start where you expected, this is why. The software assumes you might be syncing to a film reel, and it's being polite about leaving room at the top.

The problem is that nobody in a home studio is syncing to a film reel. We're syncing a mixer to a laptop. The Model 12 has no concept of reel numbers or pre-roll conventions. It starts at zero because zero is where things start.

## The Fix

File, Project Settings, Synchronization, General tab. "Bar Position 1 1 1 1 plays at SMPTE." Change `01:00:00:00` to `00:00:00:00.00`. That's it. Logic now agrees with the Model 12 about where the timeline begins, and pressing play puts us at bar one instead of bar negative nine.

It took us longer to find the setting than to change it. The synchronization preferences in Logic are spread across multiple tabs — General, MIDI, Audio — and the field names are dense. "Bar Position 1 1 1 1 plays at SMPTE" is not a phrase that screams "this is why your transport is broken." You have to already know what it means to know you need to change it.

## The Broader Problem

This is the thing about sync between hardware and software: every device carries assumptions from a different era. The Model 12 thinks like a modern multitrack recorder — zero is zero, play means play. Logic thinks like a post-production workstation that might be locked to a Studer tape machine running SMPTE striped an hour in. Both are correct within their own context. Neither knows about the other's assumptions.

We've run into this pattern before with other settings — the sync button needing "Auto Sync In" enabled, the clock start position needing to match, MMC input needing to be on. Each one is a small assumption buried in a preferences panel, and each one can silently break the connection between two devices that are otherwise talking to each other just fine.

The lesson isn't really about timecode offsets. It's that hardware-software sync is a negotiation between decades of accumulated defaults, and most of them were set for workflows that don't exist anymore. When something breaks in a way that doesn't make sense, start by asking: what does each device think "zero" means?
