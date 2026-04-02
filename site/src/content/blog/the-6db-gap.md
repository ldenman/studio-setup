---
title: "The 6dB Gap: When Analog and Digital Disagree"
date: 2026-01-26
description: "The same signal read -18 in Logic and -12 on the Model 12. We spent an hour chasing a problem that wasn't a problem."
tags: ["lessons", "gear", "model-12", "recording"]
hero: "/blog/the-6db-gap.svg"
---

We were checking levels before a take — one of those quick sanity checks where you send signal through the chain and make sure the meters are doing what you expect. Logic was showing -18dBFS on its input meter. The Model 12 was showing -12dB on its recording meter. Same signal, same moment, six decibels apart.

That's not a small difference. Six dB is double the voltage. If one of those meters is right, the other one is very wrong, and we needed to figure out which before we committed anything to a recording.

## The Rabbit Hole

We started where you'd expect: the gain staging. Checked the bus fader feeding the Model 12. Checked the send level on the channel. Checked the USB output assignment. Everything was set to the values we'd calibrated to. Nothing had drifted, nothing had been bumped.

So we went deeper. Pulled up the channel on the Wing and walked through every gain stage from input to output. The signal was clean all the way through — no stray processing, no unintended boosts, no dynamics sneaking in extra makeup gain. The bus compressor was off. The EQ was flat. There was no explanation for a six-decibel difference between two outputs carrying the same signal.

We even swapped cables, because at a certain point in any troubleshooting session you start suspecting the physical world. Same result. Logic at -18, Model 12 at -12.

## The Realization

About an hour in, we stopped chasing the problem and started thinking about what the two meters were actually measuring.

Logic sees the signal as a digital stream over USB. Its meter reads in dBFS — decibels relative to full scale, where zero is the absolute maximum the digital system can represent. The Wing's USB output is a direct digital tap of the signal, no conversion involved.

The Model 12 sees the signal as an analog voltage arriving on a quarter-inch cable. The Wing's analog output stage has a digital-to-analog converter, and that converter has its own calibration — its own relationship between the digital level inside the mixer and the voltage it puts out on the wire. That relationship is set so that professional reference level, -18dBFS, corresponds to a healthy operating level on the analog side.

The Model 12's meter is reading the analog voltage and expressing it in its own scale. And on its scale, that voltage reads -12dB. Not because the signal is hotter. Because the ruler is different.

## Two Rulers, Same Signal

This is one of those things that seems obvious once you understand it, but it's genuinely confusing when you're staring at two meters that should agree and don't. The signal isn't wrong. Neither meter is wrong. They're just measuring different things — one is reading the digital sample values, the other is reading the analog voltage those values produce after conversion.

The Wing's D/A converters are calibrated so that -18dBFS — which is the standard professional reference level, the digital equivalent of zero on a VU meter — produces a voltage that reads about -12 on the Model 12. That six-decibel offset is baked into the conversion. It's not a bug, it's not a miscalibration, it's just how the math works out when a digital reference level meets an analog meter with its own calibration.

## The Lesson

We wasted an hour because we assumed two meters looking at the same signal should show the same number. They shouldn't, and they won't, any time you're comparing a digital meter to an analog one. The only thing that matters is whether each meter is showing a healthy level in its own context. -18dBFS is right where you want to be in the digital world — plenty of headroom, standard reference level. -12dB on the Model 12 is a clean, workable recording level with room to spare.

The rule now: don't compare numbers across domains. Check the digital meters against digital references. Check the analog meters against analog references. And when they disagree by six dB, nod and move on — that's just the gap between two ways of describing the same sound.
