---
title: "The Stereo Collapse"
date: 2026-03-28
description: "Our stereo sources had been quietly folding to mono for weeks. We didn't notice because mono still sounds normal — you just lose everything that makes stereo worth having."
tags: ["lessons", "routing", "recording"]
hero: "/blog/stereo-collapse.svg"
---

There's a special category of studio mistake where the problem isn't that something sounds bad. It's that something sounds fine. Just fine. Perfectly acceptable. And because it sounds acceptable, you never think to question it. You move on and build an entire workflow on top of a signal that's been silently ruined.

That's what happened with our stereo sources. For weeks, every stereo signal in the studio had been collapsed to mono, and we had no idea.

## The Setup

We have two stereo sources that matter. The first is a pair of condenser microphones — small diaphragms in a spaced pair, meant to capture room sound and acoustic instruments with a sense of physical space. The second is the Model 12's stereo return, which carries the mixdown from our analog mixing console back into the Wing for monitoring.

Both of these sources were wired correctly. The condensers were patched to the right inputs. The Model 12's stereo output was arriving on the right channels. Levels were good. Signal was present. Everything checked out.

Except the stereo image was completely gone. Both sources were coming through dead center, with no width at all. The condenser pair — two microphones specifically positioned to capture a stereo field — was producing a mono signal. The Model 12's carefully panned mix was arriving as a mono sum. Every bit of spatial information, every subtle difference between left and right, was being thrown away before it even hit the channel strip.

## Why We Didn't Notice

This is the insidious part. Mono doesn't sound broken. If you solo a mono signal, it sounds like a perfectly good audio signal. It has full frequency range, good dynamics, correct levels. There's nothing wrong with it in isolation. You could record an entire album in mono and it would sound like music.

What mono doesn't have is width. The sense that the acoustic guitar is wider than the vocal. The feeling that the room has actual dimensions. The subtle left-right differences that make a stereo mix feel three-dimensional instead of flat. Those things are easy to miss if you're focused on other problems — and in the early days of this studio, we were always focused on other problems. Gain staging, feedback loops, noise floors, phantom power disasters. Stereo imaging was pretty far down the list of things we were actively worrying about.

So the condensers sounded like condensers. The Model 12 return sounded like a mix. Nothing was obviously wrong. We just never had that moment of putting on headphones and thinking, "Wait, where's the width?"

## The Cause

The Wing defaults every channel to mono mode. This is a reasonable default — most channels in a typical setup are mono sources. A vocal mic, a guitar DI, a kick drum. You don't want those accidentally spread across the stereo field because the console decided they were stereo.

But it means that when you do have a stereo source, you have to explicitly tell the Wing. And "explicitly" means setting the input mode on the input group, not on the channel strip itself. We were looking at the channels, seeing signal, hearing sound, and assuming everything was configured correctly. The input group's mode setting — the one that actually determines whether the Wing treats a pair of physical inputs as a linked stereo signal or two independent mono signals — was sitting at its factory default.

In mono mode, the Wing takes whatever arrives on the input pair and sums it. Left plus right becomes a single mono signal routed to the channel. All the spatial information encoded in the difference between the two sides gets folded into a single stream. You still get audio. You just don't get stereo.

## The Fix

One command per input group. That's it. Set the mode to stereo, and suddenly the condensers have width. The Model 12 return has a left side and a right side again. Panning works. The room sounds like a room instead of a point source.

The fix took thirty seconds. Finding the problem took weeks — or more accurately, we lived with the problem for weeks without realizing there was one.

## What We Actually Lost

Here's what bothers us. During those weeks, we tracked acoustic guitar with the condenser pair. We monitored mixes through the Model 12 return. We made decisions about panning and reverb and spatial placement while listening to a monitoring path that had no stereo information in it. Every mix decision we made through that return was based on a lie. We were hearing a mono fold-down and treating it as the truth.

Did any of those recordings come out wrong? Probably not — the individual tracks were recorded correctly through their own paths. But the monitoring was compromised. If we'd been checking our mixes on the Model 12 return and thinking "this sounds nicely centered, good balance," what we were actually hearing was "everything is forced to center because the return is mono." That's not a mix decision. That's a routing error pretending to be a mix decision.

## The Rule Now

Every stereo source gets its mode set on the day it's patched in. Not later. Not when we get around to it. Not when something sounds weird. The moment a stereo cable gets plugged in, the input group mode gets set to stereo. We added it to the setup checklist alongside phantom power and gain staging.

The broader lesson is about defaults. Every piece of gear ships with defaults, and most of the time those defaults are sensible. But "sensible default" and "correct for your setup" are different things. A mono default is sensible. It's also wrong for half the inputs in our studio. The gap between "works fine" and "works correctly" is where the subtle problems live — the ones you don't catch until you've been living with them long enough to forget what the right version sounds like.
