---
title: "HA73: Two Channels, Two Personalities"
date: 2026-03-27
description: "Same preamp, same knob positions, different output levels. That's not a defect — it's analog."
tags: ["gear", "outboard", "lessons"]
hero: "/blog/ha73-two-personalities.svg"
---

We assumed the two channels would behave identically. Same circuit design, same components, same knob positions — why wouldn't they produce the same output? The Heritage Audio HA73-EQX2 is a dual-channel Neve 1073-style preamp, and on paper, channel A and channel B are mirrors of each other. In practice, they are not.

## The Discovery

We found this during calibration. The process is straightforward: send a known reference tone through each piece of outboard gear one at a time, measure what comes back, and adjust until input equals output. Unity gain. What goes in at a certain level comes back at the same level. You do this so every piece of gear downstream receives exactly what it expects — no surprises, no clipping, no starved signal.

We started with channel A, which lives on the vocal chain. Tone in, patch the preamp output directly back to the mixer, read the meter. Adjusted the output knob until we hit our reference level. Wrote it down: output at roughly one o'clock. Done.

Then we moved to channel B on the guitar chain. Same gain setting, same EQ (flat, bypassed), same reference tone at the same level. Patched it the same way. Read the meter. Too quiet. Not by a huge amount, but clearly not at reference. We kept turning the output knob clockwise. Past two o'clock. Past three. Finally landed at four o'clock before the level matched.

That's a significant difference in knob position for the same result.

## Why It Happens

Discrete analog circuits are built from individual transistors, capacitors, and resistors — not integrated chips where everything is laser-trimmed to identical specs. Each component has a tolerance range. A resistor rated at 1k ohms might actually measure 980 or 1020. A transistor's gain varies from unit to unit. Multiply those small variations across dozens of components in a preamp circuit, and two channels built to the same schematic will have measurably different behavior.

This is not a defect. It is the fundamental nature of discrete analog audio gear. It is, arguably, part of why people reach for this kind of equipment in the first place. The slight unpredictability, the way each unit develops its own character through the specific combination of components it happened to receive — that is the texture people mean when they say analog gear sounds "alive."

Mass-produced digital gear gives you perfect repeatability. A plugin instance is identical to every other instance. That is useful in its own way. But nobody has ever described a plugin as having personality.

## What We Did About It

We calibrated each channel independently and recorded the settings. Channel A on the vocal chain: output at one o'clock. Channel B on the guitar chain: output at four o'clock. Both with the gain knob at the same position, both hitting the same reference level at the mixer's return input.

Those settings live in the studio's configuration file now. If we ever need to recalibrate — after changing the sample rate, swapping a unit in the chain, or if levels start drifting between sessions — we have a known starting point for each channel.

The important thing is that we measured and documented the difference rather than assuming both channels were the same. If we had set both output knobs to the same position and called it done, the guitar chain would have been running slightly low. Every piece of gear downstream — the 1176, the Distressor — would have been receiving less signal than expected. The compressors would have engaged later and lighter than intended. The whole chain would have behaved differently from what we dialed in, and we might not have noticed until something sounded off in a recording and we couldn't figure out why.

## The Lesson

Trust your meters, not your knob positions. Two identical-looking controls on the same piece of gear can produce different results, and that is fine. What matters is that you know the difference exists, you measure it, and you account for it. The calibration process is not about making gear behave perfectly — it is about understanding exactly how your specific units behave and setting them up so the rest of the chain can do its job.

Every piece of analog gear in the rack has its own personality. The HA73 just happens to have two.
