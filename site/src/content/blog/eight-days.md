---
title: "Eight Days to a Studio"
date: 2026-03-29
description: "The studio that exists today was not planned on day one — it was discovered through forty commits, three major pivots, and one very loud feedback loop."
tags: ["workflow", "lessons", "philosophy"]
hero: "/blog/eight-days.svg"
---

Nobody sat down with a blank piece of paper and designed this studio. It was built the way you'd build a song — one part at a time, each new layer changing what the previous ones needed to be. Forty commits. Ten pull requests. Three architecture rewrites. Eight days. And the studio that came out the other end barely resembles the one that went in on day one.

## Day 1: The Skeleton

March 21st. First commit. The Wing Rack goes online, the dual outboard chains get patched in through the Samson patchbay, and the Model 12 takes its place as the multi-track recorder. Two signal paths — vocal and guitar — each running through their own preamp, compressor, and leveling amp. The patchbay normalled so you could just plug in and go. No patching required for the default setup.

The same day, an MCP server goes live so an AI assistant can read and write every parameter on the mixer. Not because it's cool — because there are hundreds of parameters to manage across channels, buses, effects, and routing, and keeping them straight by hand is a full-time job. The machine handles the bookkeeping. The human handles the sound.

One commit. The foundation.

## Day 2: Everything at Once

March 22nd hit like a freight train. Six commits in a single day. Outboard calibration — measuring the actual gain and frequency response of each piece of hardware so the digital side knows what to expect. Tape emulation loaded onto the channel pre-inserts. An A/B testing workflow for comparing processed and dry signals. Guitar modes — electric through one amp sim, acoustic through another, switchable without repatching. Condenser mic routing. Transport sync between the Model 12 and Logic so pressing play on one starts the other. Speaker routing through the patchbay.

It felt like the studio was done. Everything was wired, everything was documented, everything worked. That feeling lasted about eighteen hours.

## Day 3: The White Noise Crisis

March 23rd. The Loopback audio interface was set as both Source and Monitor in its routing software. The Wing was sending audio over USB and then listening to what came back on the same connection. A perfect digital circle. The signal went out, came back, went out again, and within milliseconds every channel was screaming full-bandwidth white noise.

The kind of sound that makes you rip your headphones off before your brain even processes what happened.

One setting. Source only. Never both. The fix took seconds. The lesson took longer to absorb: in a studio this interconnected, every signal path is a potential loop. You don't get to assume a path is safe just because it was safe yesterday.

This was the first real failure, and it set the tone for everything that followed. The studio would get better not by adding features, but by surviving its own mistakes.

## Day 4: The Overhaul

March 24th. Nine commits. The most productive day of the build, and almost all of it was tearing things apart.

The tape emulation moved. It had been sitting on the channel pre-inserts — before the outboard chain — which meant the 1176 and Distressor were compressing a signal that already had tape harmonics baked in. That's backwards. The outboard should hear the raw signal. The tape color should come after. So the TAPE effect moved from the channel pre-inserts to the recording buses, where it could process the signal after the outboard chain had done its work.

User Signal routing got fixed. The Wing's internal virtual patchbay uses a different numbering system than the physical outputs — simple bus numbers instead of stereo indices. We'd gotten it wrong, and signals were landing on the wrong buses. The kind of bug where everything looks right on the screen but nothing comes out the speakers.

The re-amping workflow got documented: how to take a dry recording and process it back through the outboard chain and amp sims after the fact. And CLAUDE.md — the master reference for the entire studio — got refactored from one massive file into modular docs, because it had grown too large to be useful.

Architecture version two. Tape on buses, not channels. It wouldn't be the last rewrite.

## Day 6: Outboard in the Recording Path

March 26th. A philosophical shift. The gate moved onto the vocal input channel. The de-esser landed on the vocal processed return. The recording buses started receiving from the outboard returns instead of the raw inputs.

This was the moment the studio committed to printing outboard processing. Not "we'll fix it in the mix." Not "let's keep it clean and add character later." The recording captures the sound of the outboard chain — the Neve-style preamp's warmth, the 1176's transient control, the optical leveling. That's the sound. It's on the recording. You can't undo it, and that's the point.

Architecture version three.

## Day 7: The Model 12 Revelation

March 27th. The discovery that changed everything.

The Model 12 can send ten tracks of audio to a computer over USB. It can receive ten tracks back. But there's a catch buried in the specs that nobody mentions in the marketing: the individual tracks you've recorded to the Model 12's internal storage don't come back over USB during playback. You get the live inputs and the stereo mix. Not the multi-track recordings.

This matters because the whole architecture depends on getting individual tracks back into the Wing for effects processing — adding reverb to vocals, amp simulation to guitars, separate processing on each instrument. If the Model 12 can only send its stereo mix, you're stuck with whatever balance it gives you. No per-track processing. No individual stem mixing.

Logic Pro became the primary recorder that day. Unlimited tracks, every one independently accessible over USB. The Model 12 still runs as the transport master — press play on the Tascam and Logic follows via timecode — but the actual recordings live in the computer.

The same day, the session lessons document was created. A running log of every mistake, every discovery, every quirk of the gear. Updated at the end of every session. Read at the beginning of every session. The studio's institutional memory.

## Day 8: Final Architecture

March 28th. The last major build day. Everything clicked into place.

Logic as the recorder. The Model 12 as an analog mixing console, receiving processed stems from the Wing through seven matrices — vocals, rhythm guitar, lead guitar, bass, keys, synth, drums — each on its own fader. Physical knobs for every instrument. The Model 12 captures its own stereo mixdown on tracks 11/12, so every mix pass is automatically backed up to the SD card.

Tape returns landed on channels 25 through 32. Eight channels dedicated to playing back previously recorded tracks with independent effects processing. Mix monitoring moved to channel 7, soloed so the Model 12's stereo output could be heard through the Wing's headphone amp without interference from the tracking buses.

Nineteen Mermaid diagrams mapped every signal path in the studio. The Astro website went live with an interactive rack room, virtual routing panel, and the first blog posts.

Zero cables needed for default operation. Plug in the instrument. Press record. Everything is already patched.

## The Architecture That Emerged

Looking back, the studio evolved through four distinct versions:

**V1** put tape emulation on the channel inputs, before the outboard. The outboard was compressing tape harmonics. Wrong order.

**V2** moved tape to the recording buses, after the outboard. Clean signal into the hardware, tape character on the way to the recorder. Better.

**V3** committed the outboard processing to the recording. Gate, EQ, compression, de-essing — all printed. No going back. The recording sounds like the performance sounded.

**V4** moved the recordings to Logic and turned the Model 12 into a mixing console. The piece of gear that was supposed to be the recorder became the mixer, and it's better at that job.

None of this was planned. Each version existed because the previous one broke, or fell short, or revealed something about the gear that wasn't obvious until you pushed it. The white noise crisis taught us about feedback paths. The Model 12's USB limitation taught us to separate recording from mixing. The tape emulation's wandering taught us that signal order matters more than signal quality.

## What the Machine Kept

The AI assistant documented everything in real time. Every routing change, every parameter value, every lesson learned. When the architecture pivoted, the documentation pivoted with it. When a mistake was made at 2 AM, it was in the session lessons by 2:01 AM so it would never happen again.

Forty commits across eight days. Ten pull requests. Three major pivots. And a running document of lessons that gets longer after every session — which means the studio is still getting better. The build didn't end on day eight. It just stopped being obvious.
