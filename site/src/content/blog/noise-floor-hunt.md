---
title: "The Noise Floor Hunt"
date: 2026-01-12
description: "Four noise sources found in one afternoon — a master trim cranked to +18, a compressor boosting silence, phantom power on a line input, and a ghost channel."
tags: ["lessons", "routing"]
hero: "/blog/noise-floor-hunt.svg"
---

The monitors were hissing. Not loudly — more of a presence, like the room itself was breathing. The kind of noise you can almost ignore until you listen for it, and then it's all you can hear. We spent an afternoon tracking down four separate sources, each one contributing its own layer to the problem.

## The Master Trim

This was the dumbest one. The main output trim — the very last gain stage before the monitors — was set to +18dB. That's not a subtle boost. That's taking everything on the main bus, including the noise floor of every channel, and amplifying it by a factor of eight.

How did it get there? Probably from a previous troubleshooting session where someone was trying to get more level out of the monitors and grabbed the wrong knob. The fix took two seconds: back to zero. The hiss dropped noticeably, but it didn't disappear.

## The Compressor Boosting Silence

There was a bus compressor on the main output — the kind of gentle glue compression that's supposed to make the mix feel cohesive. The problem is that compressors have makeup gain, and makeup gain doesn't care whether it's boosting music or silence. Between takes, when nobody was playing, the compressor was reaching down into the noise floor and pulling it up to audible levels.

This is one of those things that sounds fine when music is playing and terrible when it stops. Disabled the compressor. Another layer of hiss gone.

## Phantom Power on a Line Input

This one was left over from a previous session. The condenser microphones need phantom power — 48 volts sent up the cable to power the mic's electronics. When the mics were disconnected and the input was repurposed for a line-level source, nobody turned off the phantom power. And the preamp gain was still set to +37dB, which is appropriate for a quiet condenser mic but absurdly hot for a line-level signal.

Phantom power into a line input doesn't usually damage anything, but it does add noise. Combined with the cranked gain, that input was contributing a healthy dose of hiss to any bus it fed. Killed the phantom power, dropped the gain to zero. Another layer gone.

## The Ghost Channel

The last one was the sneakiest. A channel from a previous session was still assigned to a USB input that was now carrying a different signal. It wasn't doing anything useful — just sitting there, fader down, contributing its input noise to the main bus. Nobody noticed it because the channel name still showed the old label, and it looked like it belonged.

Found it by going through every channel on the mixer and checking what was actually assigned where. The channel had no business being active, and its input was creating a slight left-right imbalance in the noise floor because it was panned to one side.

## The Takeaway

None of these were dramatic. No pops, no howling feedback, no emergency mute. Just four small things, each adding its own thin layer of noise. Together they were enough to make the monitors sound tired and the silence between takes feel restless.

The rule now: at the start of every session, check the master trim, verify there's no stray processing on the main bus, confirm phantom power is off on every input that doesn't need it, and audit every active channel. The noise floor is a stack of small mistakes, and you fix it by fixing all of them.
