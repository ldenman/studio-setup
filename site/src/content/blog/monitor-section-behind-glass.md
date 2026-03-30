---
title: "The Monitor Section Lives Behind Glass"
date: 2026-03-29
description: "We can automate every fader, every mute, every FX slot on the Wing — except the one section we reach for most during a session."
tags: ["lessons", "workflow", "philosophy"]
hero: "/blog/monitor-section-behind-glass.svg"
---

We have spent weeks building automation for this studio. Scripts that name and color every channel on the Wing at startup. A command-line tool that reads any fader, any mute, any EQ band, any dynamics setting — and writes it back. We can dump an entire channel's configuration in one command, diff it against yesterday's state, and restore it if something drifted. The whole point is that the console should be fully knowable from the outside. No surprises. No mystery state.

And then we tried to automate the monitor section.

## The 95% Wall

The Wing exposes almost everything over its native protocol. Channels, buses, matrices, aux sends, FX slots, I/O routing, USB assignments, user signals — all of it responds to our wingctl tool over TCP. We can read a value, change it, read it again to confirm. It's proper bidirectional control. This is what makes the Wing feel like a programmable instrument instead of a black box with knobs.

The monitor section is the exception. It lives at `/cfg/mon` in the Wing's address space, and when you ask wingctl to read it, you get nothing. Not an error. Not a refusal. Just silence. The native protocol that handles everything else simply doesn't reach this part of the console.

You can hit it with UDP messages — fire-and-forget commands that the Wing will accept. And the touchscreen works, obviously. But you can't read the current state back. You can't ask "what source is the monitor section listening to right now?" or "what's the dim level set to?" You can send a command and hope it landed. That's it.

## Why It Matters

The monitor section controls two things we care about deeply: the speaker output and the headphone routing. Our speaker feed comes through Matrix 1, and during tracking with open mics, those speakers need to be muted instantly to prevent acoustic feedback into the vocal mic. We handle that by muting the matrix directly — which works, because matrix mutes are fully accessible over the protocol. That's our workaround, and it's solid.

But the monitor section has its own source selector, its own dim control, its own mono-sum button. These are the kinds of things you reach for constantly during a session. Switching between mix sources to check a balance on different speakers. Dimming to have a conversation without pulling off the headphones. Hitting mono to check for phase problems. These are rapid, tactile decisions — and they're exactly the kind of thing you'd want to automate or at least verify programmatically.

We can't. Not fully. We can fire a UDP command to switch the source, but we can't confirm it took. We can't build a script that reads the current monitor state, does something, and restores it afterward. We can't include monitor settings in a session snapshot that captures the complete console state, because the monitor section will always have a hole in it.

## The Pattern

This is a pattern we keep running into with the Wing. The automation story is genuinely impressive — far more complete than most digital consoles at this price point. We have built an entire studio workflow around the assumption that the console is fully scriptable, and that assumption holds for 95% of what we do.

But the missing 5% is never something obscure. It's never "we can't automate the phase invert on aux send 7." It's always something central. The mute button that kills pre-fader sends. The display names that can only be set on the input source. And now the monitor section that lives behind glass — visible, usable by hand, but unreachable from the outside.

## Living With It

We're not angry about it. The Wing costs a fraction of what a console with a fully documented control protocol would cost, and the amount of automation it does support is remarkable. We've built things with wingctl and the USR routing system that would require expensive third-party controllers on other platforms.

But we've learned to check our assumptions. Every time we plan a new automation workflow, the first question is no longer "what should it do?" It's "can the protocol actually reach what we need to touch?" Because the Wing will let you automate almost everything. And the "almost" is always where it gets interesting.
