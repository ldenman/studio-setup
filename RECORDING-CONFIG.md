# Recording Configuration Reference

All gear is permanently wired into the patchbay. Default guitar and vocal chains are normalled and always active. The only connections made at session time are the instruments themselves (guitar into DI, mic into input). Alternative routing requires only a single front-panel patch cable.

## Behringer Wing Rack -- Channel Assignments

| Channel | Name             | Color | Source                            |
| ------- | ---------------- | ----- | --------------------------------- |
| 1       | Vocal Dry        | Blue  | LCL/1 (mic)                       |
| 2       | Guitar Dry       | Red   | LCL/2 (DI)                        |
| 3-8     | Open             |       | Local                             |
| 9       | Bass             | Green | USB/9-10 (Logic, stereo pair)     |
| 10      | Keyboard         | Green | USB/11-12 (Logic, stereo pair)    |
| 11      | Synth/Piano      | Green | USB/13-14 (Logic, stereo pair)    |
| 12      | Drums            | Green | USB/15-16 (Logic, stereo pair)    |
| 13-16   | Open             |       |                                   |
| 17      | Vocal Processed  | Blue  | LCL/17 (outboard return)          |
| 18      | Guitar Processed | Red   | LCL/18 (outboard return)          |
| 19-40   | Open             |       |                                   |

## USB Output Routing (Wing → Loopback → Model 12)

| USB Out | Source                | Model 12 Track            |
| ------- | --------------------- | ------------------------- |
| 1       | USR/1 (Vocal Dry)     | Track 1 (dry recording)   |
| 2       | USR/2 (Guitar Dry)    | Track 1 (dry recording)   |
| 17      | Main 1 L              | Track 11 (rough mix L)    |
| 18      | Main 1 R              | Track 12 (rough mix R)    |

USB 1 or 2 depending on which instrument is being tracked — only one at a time.

## USR Routing (Virtual Patchbay)

| USR | Name       | Source | Tap | Purpose                             |
| --- | ---------- | ------ | --- | ----------------------------------- |
| 1   | Vocal Dry  | Ch1    | PRE | Clean vocal for dry recording via USB |
| 2   | Guitar Dry | Ch2    | PRE | Clean guitar for dry recording via USB |

## Tascam Model 12 -- Track Assignments (per project)

| Track | Source                                     | Format |
| ----- | ------------------------------------------ | ------ |
| 1     | Current instrument (dry via USB 1 or 2)    | Mono   |
| 2-6   | Open for overdubs / alternate takes        | Mono   |
| 7/8   | Open                                       | Stereo |
| 9/10  | Open                                       | Stereo |
| 11/12 | Rough mix (Main 1 L/R via USB 17/18)       | Stereo |

## Patchbay -- Samson 48-Point TRS

### How Normalled Connections Work

Each patchbay point has a top jack and a bottom jack. In a normalled configuration, the top jack internally routes to the bottom jack without any cable. This means the default signal path is always active.

- **Top jack** = output from a piece of gear
- **Bottom jack** = input to the next piece of gear
- **No cable inserted** = signal flows from top to bottom automatically (normalled)
- **Cable inserted into top** = breaks the normal, signal goes to wherever the cable leads
- **Cable inserted into bottom** = breaks the normal, bottom jack receives from wherever the cable comes from

This allows the default recording chains (guitar, vocal) to work without patching any cables, while still giving full flexibility to reroute through different outboard gear when needed.

### Default Vocal Chain (Points 1-4)

Signal flows through these four normalled points without any cables patched:

1. Wing Rack analog out 1 (Bus 1) -> HA73-EQX2 channel A input
2. HA73-EQX2 channel A output -> WA76 channel A input
3. WA76 channel A output -> Audioscape Opto input
4. Audioscape Opto output -> Wing Rack LCL input 17 (Vocal Processed, ch17)

### Default Guitar Chain (Points 5-8)

Signal flows through these four normalled points without any cables patched:

1. Wing Rack analog out 2 (Bus 2) -> HA73-EQX2 channel B input
2. HA73-EQX2 channel B output -> WA76 channel B input
3. WA76 channel B output -> Distressor input
4. Distressor output -> Wing Rack LCL input 18 (Guitar Processed, ch18)

### Patch Points

| Point | Top (Output From)           | Bottom (Input To)              | Chain  |
| ----- | --------------------------- | ------------------------------ | ------ |
| 1     | Wing LCL Out 1 (Bus 1)      | HA73 A In                      | Vocal  |
| 2     | HA73 A Out                  | WA76 A In                      | Vocal  |
| 3     | WA76 A Out                  | Opto In                        | Vocal  |
| 4     | Opto Out                    | Wing LCL In 17                 | Vocal  |
| 5     | Wing LCL Out 2 (Bus 2)      | HA73 B In                      | Guitar |
| 6     | HA73 B Out                  | WA76 B In                      | Guitar |
| 7     | WA76 B Out                  | Distressor In                  | Guitar |
| 8     | Distressor Out              | Wing LCL In 18                 | Guitar |
| 9-24  |                             |                                | Open   |

## Loopback Software Routing

| From                              | To                              |
| --------------------------------- | ------------------------------- |
| Wing USB Out 1 (USR/1 Vocal Dry)  | Model 12 Track 1 (dry)          |
| Wing USB Out 2 (USR/2 Guitar Dry) | Model 12 Track 1 (dry)          |
| Wing USB Out 17 (Main 1 L)        | Model 12 Track 11 (rough mix L) |
| Wing USB Out 18 (Main 1 R)        | Model 12 Track 12 (rough mix R) |
| Model 12 stereo out L             | Wing Rack (monitoring L)        |
| Model 12 stereo out R             | Wing Rack (monitoring R)        |

Note: USB 1 or 2 is used depending on which instrument is being tracked — only one at a time.
