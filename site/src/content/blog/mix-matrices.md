---
title: "Mix Matrices: The Missing Layer"
date: 2026-03-28
description: "How Wing matrices became the permanent routing bridge between the console and the Model 12 mixing desk."
tags: ["routing", "mixing", "model-12"]
---

The studio had a routing problem. We needed to send processed stems from the Wing to the Model 12 for analog mixing, but we didn't have enough buses. The Wing has 16 buses and most were spoken for — outboard sends, recording, monitoring, reverb.

## The Matrix Solution

The Wing has 8 matrix outputs (MX1-MX8) that nobody talks about. MX1 was already driving the speakers. MX2-MX8 were empty. Every channel and bus already has sends to each matrix. They're designed exactly for this — creating independent mixes for different destinations.

So we wired it: MX2 through MX8, each feeding a dedicated USB output, through Loopback, to a Model 12 channel. The matrices became the permanent bridge. Change the source per project, the Model 12 side never moves.

## The Layout

- **MX2 → M12 Ch 1**: Vocal
- **MX3 → M12 Ch 2**: Rhythm guitar (through RACKAMP)
- **MX4 → M12 Ch 3**: Lead guitar (through ANGEL)
- **MX5 → M12 Ch 4**: Overdub slot
- **MX6 → M12 Ch 5**: Bass (with SUB octaver)
- **MX7 → M12 Ch 7/8**: Drums (stereo)
- **MX8 → M12 Ch 9/10**: Piano/Synth (stereo)

Model 12 Ch 6 is the tape return from the AUX 1 loop. Not a matrix — its own dedicated path.

## Why This Works

The Model 12 never needs to be reconfigured. Fader 1 is always vocal. Fader 2 is always rhythm guitar. The Wing handles which track feeds which matrix. The Model 12 just mixes.

Every pass is captured on tracks 11/12. Move a fader, run it again. Mixing becomes a performance.
