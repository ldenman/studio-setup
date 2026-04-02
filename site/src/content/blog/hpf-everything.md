---
title: "Wing: HPF Everything — Cleaning Up the Mix Buses"
date: 2026-03-29
description: "Adding high-pass and low-pass filters to every mix matrix instantly recovered headroom we didn't know we were losing."
tags: ["wing", "mixing", "workflow", "model-12"]
hero: "/blog/hpf-everything.svg"
---

We'd been mixing through the matrix buses for a couple days and something felt off. The Model 12 faders were creeping higher than they should have been. The stereo bus wasn't clipping, but it felt crowded — like every instrument was fighting for the same space even when the arrangement was sparse. Turning things down helped, but then the mix lost energy. Classic headroom problem.

## The Invisible Weight

The culprit was low-end rumble. Not the kind you hear — the kind you feel in the meters. Every matrix was passing the full frequency spectrum from its source channels, including the sub-bass content that has no business being in a guitar bus, and the harsh upper frequencies that add presence on a solo'd track but just create fatigue in a full mix.

We added a 60Hz high-pass filter and a 14kHz low-pass filter to every mix matrix from MX2 through MX8. That's all seven stems feeding the Model 12 — vocal, rhythm guitar, lead guitar, bass, drums, piano, and the spare.

The difference was immediate. The low end tightened up, the top end smoothed out, and suddenly there was room on the faders again. We gained back maybe three or four dB of usable headroom just by not asking the Model 12 to reproduce frequencies that weren't contributing to the music.

## The Wing Made This Harder Than It Should Be

Here's where it got interesting. On a channel strip, the Wing gives you dedicated high-pass and low-pass filter controls — nice, obvious, easy to find. On a matrix? No such thing. The matrix EQ section is the same parametric EQ as a channel, but without the filter shortcuts.

To get a high-pass on a matrix, you have to set EQ band 1's type to CUT mode, then dial in the frequency. For a low-pass, same thing with band 8. And the parameters aren't named the way you'd expect — it's all numbered. Band 1's type lives at one numbered parameter, band 8's type at another. Not the end of the world once you know the trick, but it's not something you'd stumble into.

The other gotcha: matrix EQ is off by default. You can set perfect filter curves on all seven matrices, and nothing changes until you explicitly enable the EQ. We did exactly that on the first try — set everything up, played back, heard no difference, and spent a few minutes wondering if we'd lost our minds before realizing the EQ wasn't switched on.

## Why Not Filter at the Channel Level?

Fair question. We do filter individual channels when it makes sense — rolling off the low end on a vocal, taming the top on a particularly bright guitar take. But the matrix filter serves a different purpose. It's a safety net for the sum.

A matrix might receive signal from three or four source channels, each with its own processing. Even if each channel sounds fine on its own, the combined low-end energy adds up. A gentle high-pass on the matrix catches everything the individual channels let through. Same logic for the top end — a little air on each channel becomes harshness when it all stacks.

Think of it like this: channel filters are surgical, matrix filters are structural. One shapes the sound of an instrument. The other shapes the sound of the mix.

## The Rule Now

Every mix matrix gets a 60Hz high-pass and a 14kHz low-pass before anything else happens. It's part of the setup, right alongside setting the matrix sources and confirming the Model 12 channel assignments. Takes thirty seconds, saves hours of fighting headroom problems later.

The boring lesson, as always: the biggest improvements in a mix don't come from the exciting stuff — the compression, the reverb, the amp sim tweaks. They come from removing what shouldn't be there in the first place.
