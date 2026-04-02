---
title: "Wing: Bus Sends That Reset Themselves"
date: 2026-03-29
description: "A send level that should be +10dB keeps reverting to zero. The Wing is silently undoing our work, and it's not in the manual."
tags: ["lessons", "routing", "workflow"]
hero: "/blog/bus-sends-that-reset.svg"
---

We have a channel that needs its bus send at +10dB. Not zero. Not unity. Plus ten. The gain staging through our outboard chain demands it -- without that boost, the playback level drops noticeably compared to the live signal, and the musician hears a volume dip every time they switch between playing and listening back. It's distracting. It breaks the illusion that the recorded sound is "the sound."

So we set it to +10dB. And it works. Until it doesn't.

## The Vanishing Boost

The first time it happened, we assumed we'd made a mistake. We were adjusting some FX inserts on a different channel entirely, and when we played back a take, the level was wrong. Quieter than before. We checked the fader -- fine. Checked the bus output -- fine. Finally checked the send level on the channel feeding the bus, and there it was: 0dB. Right back where it started.

We set it to +10 again. Made a mental note. Moved on.

The second time, we were reassigning a bus routing -- nothing to do with that channel or its sends. Played something back, and the level was wrong again. Same send, same channel, same 0dB where +10 should have been.

The third time, we caught it in the act. We'd just loaded a different effect model into an FX slot -- not even on the same bus -- and checked the send level immediately afterward. Zero. The Wing had silently reset it.

## What Triggers It

We still don't have a complete list, and that's part of what makes this maddening. Here's what we know triggers a send level reset:

Changing a bus assignment on any channel. Loading or swapping an FX model in any slot. Modifying insert routing. Possibly other things we haven't isolated yet.

What these have in common is that they all touch the Wing's internal routing graph. Our best theory is that when the Wing recalculates its signal routing -- which it apparently does whenever you touch anything bus-related -- certain send parameters get pushed back to their defaults as part of that recalculation. Not all of them. Not every time. Just often enough that you can't trust them to stay put.

This isn't documented anywhere that we've found. The Wing's OSC reference describes how to set send levels. It doesn't mention that setting them might be temporary.

## Why +10dB in the First Place

The reason we need a non-unity send level is that the signal path isn't a simple point-to-point connection. The channel in question is a tape return carrying playback from the recorder. That signal has been through a recording chain that includes outboard compression, and it comes back at a level that's lower than the live monitoring path. The bus it feeds has its own processing and output gain structure. After calibrating everything, the math works out to needing +10dB on that particular send to maintain consistent loudness between "playing live" and "listening to what was just recorded."

We could restructure the gain staging to avoid needing the boost, but the current calibration is correct everywhere else. Moving one number would mean moving six others. The +10dB send is the right fix for the right reason. The problem is the console deciding, unprompted, that zero is a better number.

## The Workaround

There isn't an elegant one. We verify. Every time we make a routing change -- any routing change, on any channel or bus -- we check the send levels on every channel that has a non-default send. In practice, that means we keep a short list of "sends that aren't at zero" and audit them after touching anything.

We've also added this to our post-routing-change checklist, right next to "confirm mute states" and "check that the recording bus is still live." It's the kind of thing that feels excessive until the alternative is a take at the wrong level that you don't notice until mixdown.

For now, we query the send level before every recording pass. If it's wrong, we set it again. It takes five seconds. It's not the kind of thing a console should make you do, but it's faster than re-recording a vocal.

## The Lesson

Digital consoles have internal state machines, and those state machines have opinions. When you change one parameter, the console may silently change others as a side effect of recalculating its routing. Analog boards don't have this problem -- a knob stays where you put it because it's a physical resistor, not a number in a database that might get overwritten during a rebuild.

The broader rule we've adopted: never assume a parameter is still what you set it to. Verify before you commit. Especially on the Wing, where the mute button already taught us that words don't always mean what we think they mean, send levels have now taught us that numbers don't always stay what we set them to.

Trust, but verify. Actually, skip the trust part.
