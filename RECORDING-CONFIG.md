# Recording Configuration Reference

All gear is permanently wired into the patchbay. Default guitar and vocal chains are normalled and always active. The only connections made at session time are the instruments themselves (guitar into DI, mic into input). Alternative routing requires only a single front-panel patch cable.

## Behringer Wing Rack -- Channel Assignments

| Channel | Name             | Source          |
| ------- | ---------------- | --------------- |
| 1       | Guitar Dry       | Local           |
| 2       | Guitar Processed | Local           |
| 3       | Vocal Dry        | Local           |
| 4       | Vocal Processed  | Local           |
| 5       |                  | Local           |
| 6       |                  | Local           |
| 7       |                  | Local           |
| 8       |                  | Local           |
| 9       | Bass             | DAW / Session   |
| 10      | Keyboard         | DAW / Session   |
| 11      | Synth/Piano L    | DAW / Session   |
| 12      | Synth/Piano R    | DAW / Session   |
| 13      | Drums L          | DAW / Session   |
| 14      | Drums R          | DAW / Session   |
| 15      |                  | DAW / Session   |
| 16      |                  | DAW / Session   |

## Tascam Model 12 -- Track Assignments

| Track | Source       | Format |
| ----- | ------------ | ------ |
| 1     | Guitar Dry   | Mono   |
| 2     | Vocal Dry    | Mono   |
| 3     | Bass         | Mono   |
| 4     | Keyboard     | Mono   |
| 5     |              | Mono   |
| 6     |              | Mono   |
| 7/8   | Synth/Piano  | Stereo |
| 9/10  | Drums        | Stereo |
| 11/12 | Main L/R     | Stereo |

## Patchbay -- Samson 48-Point TRS

### How Normalled Connections Work

Each patchbay point has a top jack and a bottom jack. In a normalled configuration, the top jack internally routes to the bottom jack without any cable. This means the default signal path is always active.

- **Top jack** = output from a piece of gear
- **Bottom jack** = input to the next piece of gear
- **No cable inserted** = signal flows from top to bottom automatically (normalled)
- **Cable inserted into top** = breaks the normal, signal goes to wherever the cable leads
- **Cable inserted into bottom** = breaks the normal, bottom jack receives from wherever the cable comes from

This allows the default recording chains (guitar, vocal) to work without patching any cables, while still giving full flexibility to reroute through different outboard gear when needed.

### Default Guitar Chain (Points 1-3)

Signal flows through these three normalled points without any cables patched:

1. Wing Rack analog out 1 -> HA73-EQX2 channel 1 input
2. HA73-EQX2 channel 1 output -> 1176 channel 1 input
3. 1176 channel 1 output -> Wing Rack channel 2 input (Guitar Processed)

### Default Vocal Chain (Points 4-7)

Signal flows through these four normalled points without any cables patched:

1. Wing Rack analog out 2 -> HA73-EQX2 channel 2 input
2. HA73-EQX2 channel 2 output -> 1176 channel 2 input
3. 1176 channel 2 output -> Audioscape Opto input
4. Audioscape Opto output -> Wing Rack channel 4 input (Vocal Processed)

### Patch Points

| Point | Top (Output From)           | Bottom (Input To)          |
| ----- | --------------------------- | -------------------------- |
| 1     | Wing Rack analog out 1      | HA73-EQX2 channel 1 input  |
| 2     | HA73-EQX2 channel 1 output  | 1176 channel 1 input       |
| 3     | 1176 channel 1 output       | Wing Rack channel 2 input  |
| 4     | Wing Rack analog out 2      | HA73-EQX2 channel 2 input  |
| 5     | HA73-EQX2 channel 2 output  | 1176 channel 2 input       |
| 6     | 1176 channel 2 output       | Audioscape Opto input      |
| 7     | Audioscape Opto output      | Wing Rack channel 4 input  |
| 7     |                             |                            |
| 8     |                             |                            |
| 9     |                             |                            |
| 10    |                             |                            |
| 11    |                             |                            |
| 12    |                             |                            |
| 13    |                             |                            |
| 14    |                             |                            |
| 15    |                             |                            |
| 16    |                             |                            |
| 17    |                             |                            |
| 18    |                             |                            |
| 19    |                             |                            |
| 20    |                             |                            |
| 21    |                             |                            |
| 22    |                             |                            |
| 23    |                             |                            |
| 24    |                             |                            |

## Loopback Software Routing

| From                        | To                         |
| --------------------------- | -------------------------- |
| Wing Rack channel 1 (Guitar Dry) | Model 12 track 1           |
| Wing Rack channel 3 (Vocal Dry)  | Model 12 track 2           |
| Wing Rack channel 9 (Bass)    | Model 12 track 3           |
| Wing Rack channel 10 (Keyboard)| Model 12 track 4           |
| Wing Rack channel 11 (Synth/Piano L)| Model 12 track 7 (stereo L)|
| Wing Rack channel 12 (Synth/Piano R)| Model 12 track 8 (stereo R)|
| Wing Rack channel 13 (Drums L)| Model 12 track 9 (stereo L)|
| Wing Rack channel 14 (Drums R)| Model 12 track 10 (stereo R)|
| Model 12 stereo out L       | Wing Rack (monitoring L)   |
| Model 12 stereo out R       | Wing Rack (monitoring R)   |
