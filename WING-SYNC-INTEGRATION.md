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

These match the Wing Rack channel assignments in RECORDING-CONFIG.md:

| Channel | OSC Path              | Name           |
| ------- | --------------------- | -------------- |
| 1       | /io/in/LCL/1/name     | Guitar Dry     |
| 2       | /io/in/LCL/2/name     | Guitar Proc    |
| 3       | /io/in/LCL/3/name     | Vocal Dry      |
| 4       | /io/in/LCL/4/name     | Vocal Proc     |
| 5       | /io/in/LCL/5/name     |                |
| 6       | /io/in/LCL/6/name     |                |
| 7       | /io/in/LCL/7/name     |                |
| 8       | /io/in/LCL/8/name     |                |
| 9       | /io/in/LCL/9/name     | Bass           |
| 10      | /io/in/LCL/10/name    | Keyboard       |
| 11      | /io/in/LCL/11/name    | Synth/Piano L  |
| 12      | /io/in/LCL/12/name    | Synth/Piano R  |
| 13      | /io/in/LCL/13/name    | Drums L        |
| 14      | /io/in/LCL/14/name    | Drums R        |
| 15      | /io/in/LCL/15/name    |                |
| 16      | /io/in/LCL/16/name    |                |

### Sending Names via CLI

Requires `liblo` (`brew install liblo`):

```sh
oscsend 192.168.2.2 2223 /io/in/LCL/1/name s "Guitar Dry"
oscsend 192.168.2.2 2223 /io/in/LCL/2/name s "Guitar Proc"
oscsend 192.168.2.2 2223 /io/in/LCL/3/name s "Vocal Dry"
oscsend 192.168.2.2 2223 /io/in/LCL/4/name s "Vocal Proc"
oscsend 192.168.2.2 2223 /io/in/LCL/9/name s "Bass"
oscsend 192.168.2.2 2223 /io/in/LCL/10/name s "Keyboard"
oscsend 192.168.2.2 2223 /io/in/LCL/11/name s "Synth/Piano L"
oscsend 192.168.2.2 2223 /io/in/LCL/12/name s "Synth/Piano R"
oscsend 192.168.2.2 2223 /io/in/LCL/13/name s "Drums L"
oscsend 192.168.2.2 2223 /io/in/LCL/14/name s "Drums R"
```
