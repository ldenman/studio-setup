# Wing Sync Integration

## Overview

The wing-sync app (~/src/wing-sync) communicates with the Behringer Wing Rack over OSC (Open Sound Control) via UDP.

### Connection Details

| Setting      | Value           |
| ------------ | --------------- |
| Wing IP      | 192.168.2.2   |
| Wing Port    | 2223            |
| Local RX Port| 23456           |
| Protocol     | OSC over UDP    |

Configuration is stored at `~/.wing-sync/config.edn`.

## Current Capabilities

Wing-sync currently syncs FX delay/rate times to MIDI clock BPM. It does not set channel names or any other channel-level configuration.

### OSC Paths Currently Used

| Path          | Direction | Purpose                          |
| ------------- | --------- | -------------------------------- |
| /fx/N/mdl     | Query     | Check which effect model is loaded |
| /fx/N/time    | Send      | Set delay time in ms             |
| /fx/N/speed   | Send      | Set rate/speed in Hz             |

## Channel Naming via OSC

The Behringer Wing supports setting channel names over OSC. This would allow us to push the channel names from our configuration directly to the Wing Rack, eliminating manual entry.

### OSC Paths for Channel Configuration

The Wing display shows the **input source name** (`/ch/N/$name`), not the channel strip name (`/ch/N/name`). To change what appears on the scribble strips, set the name on the input source.

All channels currently use local inputs (`LCL`), so the correct path is `/io/in/LCL/N/name`.

| Path               | Type   | Purpose                                    |
| ------------------ | ------ | ------------------------------------------ |
| /io/in/LCL/N/name  | String | Set input source name (shows on display)   |
| /ch/N/name         | String | Set channel strip name (not shown on display) |
| /ch/N/$name        | String | Read-only, reflects linked source name     |
| /ch/N/icon         | Int    | Set channel icon                           |
| /ch/N/led          | Int    | Set scribble light                         |

### Channel Names

See `studio.edn` :channels for the current channel name assignments. Names are set on input sources via `/io/in/LCL/N/name` (or `/io/in/USR/N/name` for USR-sourced channels). The script `scripts/set-channel-names.sh` pushes all names to the Wing.

### Sending Names via CLI

Requires `liblo` (`brew install liblo`):

```sh
# Example — see scripts/set-channel-names.sh for the full set
oscsend 192.168.2.2 2223 /io/in/LCL/1/name s "Vocal Dry"
oscsend 192.168.2.2 2223 /io/in/LCL/1/col i 2
```
