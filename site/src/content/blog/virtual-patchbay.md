---
title: "Wing: The Virtual Patchbay Nobody Sees"
date: 2026-03-28
description: "When the Wing's output routing hit a dead end, 24 invisible patch points saved the session."
tags: ["routing", "workflow", "lessons"]
hero: "/blog/virtual-patchbay.svg"
---

We hit a wall during the mix-matrix buildout. The plan was straightforward: tap specific channels on the Wing, route them to specific USB outputs, send those to the Model 12 for analog mixing. The Wing has 48 USB outputs and 40-something channels. Should be a matter of pointing output A at channel B and moving on.

It wasn't.

## The Dead End

The Wing's USB output routing has a source selector. You pick a group — channel, bus, matrix, aux — and then pick which one. Simple in theory. But when we tried to assign a high-numbered channel directly to a USB output, the Wing wouldn't cooperate. The CH group just didn't work for certain destinations. No error, no feedback. The output sat there producing silence while the channel was clearly carrying signal.

We tried different channels. Different USB outputs. Different tap points. Same result. The Wing was perfectly happy routing buses and matrices to USB, but direct channel-to-USB routing had blind spots. We were stuck with signals we could see on the meters but couldn't get out of the box.

## Twenty-Four Invisible Patch Points

Buried in the Wing's I/O architecture is something called USR — User Signal inputs. Twenty-four of them. The manual barely mentions them. They're virtual patch points that live entirely inside the Wing's routing engine, and they turned out to be exactly what we needed.

A USR input taps any signal in the Wing — any channel, any bus, any matrix — at whatever point you choose. Pre-fader, post-fader, pre-insert, post-insert. You configure the source, the tap point, and then the USR signal becomes available as a routing source everywhere else in the system. It's a virtual patch cable. You plug it into whatever you're trying to reach, and the signal appears on the other end.

So instead of routing Channel 33 directly to a USB output — which the Wing refused to do — we created a USR input that tapped Channel 33, then pointed the USB output at the USR. The signal flowed immediately. No latency, no level change, no coloration. Just a clean internal redirect around a routing limitation we couldn't explain.

## More Than a Workaround

Once we understood what USR could do, it stopped being a workaround and started being the backbone of the studio's routing. We now use it for everything the Wing's default routing can't handle cleanly.

The vocal dry signal for recording? That's a USR input tapping Bus 7 pre-fader, routed to USB 1 for Logic. Pre-fader matters here — the bus fader controls the monitoring level, but the recording level stays fixed regardless of what we do at the console. We can ride the vocal in the headphones without touching what hits the recorder.

The tape saturation loop? A USR tapping Channel 33 post-insert, catching the signal after the tape and delay effects, routing it back to the Model 12 on a dedicated channel. The "post" tap is critical — pre-insert would miss the effects entirely.

The acoustic guitar DI path? A USR tapping Channel 2 pre-fader, feeding a separate channel that has its own name and processing. The original channel still runs through the amp sim and outboard chain. The USR gives us a clean copy with zero interaction between the two paths.

And the re-amp output — that's a USR tapping the processed return channel, feeding USB 3, which only gets enabled during re-amping passes. The rest of the time it stays off so the outboard noise floor doesn't leak into the recorder.

## The Naming Trick

Here's the thing about USR that elevated it from useful to essential: each USR input gets its own scribble strip. Its own name, its own color, its own identity on the Wing's display.

The Wing always shows the name of a channel's input source, not the channel itself. If Channel 5 receives from a USR input, the display shows whatever you named that USR. This sounds like a minor cosmetic detail until you're staring at a 40-channel console trying to figure out which signal is where. A channel called "Vocal LA2A" is immediately readable. A channel showing "CH 3" when it's actually a post-compressor tap of the vocal chain is not.

So USR became our naming system too. Every derived signal — every tap, every split, every reroute — gets a USR with a descriptive name and a color that matches its role. Vocal paths are blue. Guitar paths are red. Recording taps are green. You can glance at the Wing's display and immediately see what's a source, what's a process, and what's a recording feed.

## The Invisible Infrastructure

Five of our twenty-four USR slots are in use now. That leaves nineteen for whatever comes next — stereo monitoring splits, additional recording taps, parallel processing paths, alternate headphone mixes. The capacity is there without running a single new cable or buying a single new piece of gear.

The thing that strikes us about USR is how invisible it is. There's no physical patchbay, no cables to trip over, no normalling to remember. It just exists inside the routing engine, doing its job silently. When someone listens to a recording from this studio, they'll never know that the signal took a detour through a virtual patch point to get from the channel strip to the recorder. And that's exactly how infrastructure should work — solving problems without announcing itself.

We went looking for a way to get a channel signal to a USB output. We found a virtual patchbay that changed how we think about the entire console.
