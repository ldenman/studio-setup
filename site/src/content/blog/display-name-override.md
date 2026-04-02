---
title: "Wing: The Display Name You Can't Override"
date: 2026-03-28
description: "We wrote to /ch/N/name a dozen times. The scribble strip never changed. The Wing has its own ideas about identity."
tags: ["lessons", "routing", "gear"]
hero: "/blog/display-name-override.svg"
---

We renamed a channel and nothing happened. Not "nothing happened and then it updated a second later." Nothing happened, permanently. We wrote a new name, confirmed it was stored, looked at the Wing's display, and the old name was still sitting there like we hadn't done anything at all.

## The Obvious Fix That Doesn't Work

When you want to change what a channel is called, you change its name. On nearly every digital console, mixer, or DAW in existence, there's a name field on the channel strip, and whatever you type there is what shows up on the scribble strip. It's the most intuitive thing in the world. We set the channel name. The channel ignored us.

We tried it again, thinking maybe we'd made a typo in the path. We read the value back -- the name was stored correctly. The Wing had accepted the new name and filed it away somewhere internally. It just refused to display it. The scribble strip kept showing the old label, completely indifferent to what we'd written.

## The Wing Shows the Source, Not the Strip

Here's what's actually happening. The Wing's display doesn't show the channel strip's name. It shows the name of whatever input source is feeding that channel. If Channel 5 receives signal from local input 3, the display shows whatever local input 3 is named. If Channel 17 receives from a bus, the display shows the bus name. The channel strip's own name field exists -- you can write to it, you can read it back -- but the display doesn't use it.

This is not documented in a way that would save you twenty minutes of confusion. The parameter accepts writes. It stores the value. It just doesn't do anything visible. It's the console equivalent of shouting into a pillow.

The fix is to name the input source instead of the channel. For a local input, that means writing to the input's own name field, not the channel's. For a USR input, you name the USR. For a bus, you name the bus. Whatever is plugged into the channel's input -- that's what you name.

## Colors Too

The same rule applies to colors. We tried to color-code our channels by setting colors on the channel strips. Same result -- the Wing displayed the color of the input source, not the channel. Once we moved the color assignments to the input sources, everything lined up immediately.

This means the identity of a channel on the Wing is entirely determined by what's feeding it. The channel strip is just a processing engine with a fader. It doesn't have its own face. It wears the face of whatever walks in the door.

## Why This Actually Matters

This quirk becomes genuinely useful once you stop fighting it. Because identity follows the input source, you can change what a channel displays just by changing what feeds it. Point a channel at a different USR input and it instantly takes on that USR's name and color. No renaming, no reconfiguring. The display updates because the source changed.

This is how USR routing became our naming system. When we duplicate a signal -- tapping a vocal channel to create an independent recording feed, for instance -- the copy needs its own identity. On a console where the channel strip owns its name, you'd just rename the duplicate. On the Wing, you create a USR input, name it something descriptive, give it a color that matches its role, and point the destination channel at it. The channel immediately displays the USR's identity. Blue for vocals, red for guitar, green for recording taps. You can read the entire signal flow from across the room just by looking at the colors.

## The Lesson

Not every writable parameter does what you'd expect. The Wing accepted our channel names politely and stored them faithfully and displayed them never. The real name lives upstream, on the input source, because the Wing thinks about identity differently than we did. The channel doesn't decide what it's called. The signal does.

Once we understood that, we stopped trying to label the channels and started labeling the signals. It's a better mental model anyway. A channel is temporary -- it's whatever you patch into it today. But a signal has an identity: it's the vocal dry, the guitar DI, the tape return. Name the signal, and the channel figures itself out.
