# Behringer Wing Rack -- OSC Reference

Source of truth for OSC communication with the Wing Rack. Use this when building automation scripts.

## Connection

| Setting       | Value         |
| ------------- | ------------- |
| IP            | 192.168.2.2   |
| Port          | 2223 (UDP)    |
| Native Port   | 2222 (UDP/TCP)|
| Protocol      | OSC over UDP  |
| Max clients   | 16 (TCP); unlimited (UDP) |
| Subscriptions | 1 at a time, must renew every 10s |

### Console Discovery

Send `/?` to get console info:
```sh
oscsend 192.168.2.2 2223 /?
# Returns: WING,<IP>,<name>,<model>,<serial>,<firmware>
```

## Sending Commands

Tool: `oscsend` from liblo (`brew install liblo`)

```sh
# Set a string value
oscsend 192.168.2.2 2223 /path s "value"

# Set an integer value
oscsend 192.168.2.2 2223 /path i 1

# Set a float value
oscsend 192.168.2.2 2223 /path f 0.75

# Query a value (send with no arguments)
# Response comes back to your source port
oscsend 192.168.2.2 2223 /path
```

The Wing accepts string, int, or float for most parameters and converts internally.

### Batch Set (Node Commands)

Set multiple parameters in a single OSC message using dot notation:

```
# Set ch1 fader to -1dB and mute off, ch2 fader to 0dB and mute on
/  ,s  /ch.1.fdr=-1,mute=0,.2.fdr=0,mute=1

# Set fader and mute on ch1 in one command
/ch/1  ,s  fdr=4,mute=1

# Mix root-level paths
/  ,s  /ch.1.fdr=10,mute=1,/bus.1.fdr=5
```

The console replies with `/* ,s OK` on success, or one of:
- `/* ,s NODE NOT FOUND`
- `/* ,s VALUE ERROR`
- `/* ,s BUFFER OVERFLOW`
- `/* ,s INCOMPLETE DATA`

### Port Redirection

Prefix any command with `/%PORT` to receive the reply on a specific UDP port:
```sh
# Receive reply on port 10027
oscsend 192.168.2.2 2223 /%10027/ch/1/mute
```

## Reading Values

The Wing does not echo writes. To read a value, send the path with no arguments. The Wing responds to the UDP source port of the request.

### Response Format

- Strings/enums: `,s` — e.g. `"STD"`
- Floats: `,sff` — ascii string, raw position [0.0..1.0], actual float value
- Integers: `,sfi` — ascii string, raw position [0.0..1.0], actual int value

### Node Discovery

Query a path to discover its children (sub-nodes). The response lists all child node names:
```
Query:  /fx/1
Reply:  /fx/1 ,ssssss mdl fxmix $esrc $emode $a_chn $a_pos
```

This is how you discover what parameters are available for a loaded effect.

```python
import socket

def osc_string(s):
    s = s.encode('utf-8') + b'\x00'
    s += b'\x00' * ((4 - len(s) % 4) % 4)
    return s

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 23458))
sock.settimeout(2)

# Query
sock.sendto(osc_string('/ch/1/name') + osc_string(','), ('192.168.2.2', 2223))
data, addr = sock.recvfrom(4096)
```

## Path Conventions

- `$` prefix = read-only (e.g. `/ch/1/$name`, `/ch/1/$mute`)
- No `$` prefix = writable (e.g. `/ch/1/name`, `/ch/1/mute`)
- `N` in paths below = 1-based index
- Channel names display from the **input source** (`/io/in/LCL/N/name`), not the channel strip (`/ch/N/name`)

### Root JSON Tree

`/ ,s` returns: `$stat cfg $syscfg io ch aux bus main mtx dca mgrp fx cards play rec $ctl`

## Channels (/ch/N/...)

40 channels available. Replace N with 1-40.

### Identity

| Path            | Type   | Description              |
| --------------- | ------ | ------------------------ |
| /ch/N/name      | String | Channel strip name (16 chars max) |
| /ch/N/$name     | String | Display name [RO] reflects input source |
| /ch/N/icon      | Int    | Channel icon (0-999)     |
| /ch/N/led       | Int    | Scribble light on/off    |
| /ch/N/col       | Int    | Channel color (1-12)     |
| /ch/N/$col      | Int    | Display color [RO]       |
| /ch/N/tags      | String | Channel tags             |

### Level Control

| Path            | Type   | Description              |
| --------------- | ------ | ------------------------ |
| /ch/N/fdr       | Float  | Fader level (dB)         |
| /ch/N/pan       | Float  | Pan position             |
| /ch/N/wid       | Float  | Width (%)                |
| /ch/N/mute      | Int    | Mute (0=unmuted, 1=muted)|
| /ch/N/$solo     | Int    | Solo                     |
| /ch/N/solosafe  | Int    | Solo safe                |
| /ch/N/mon       | String | Monitor output (A, B)    |

### Input Configuration

| Path                    | Type   | Description              |
| ----------------------- | ------ | ------------------------ |
| /ch/N/in/conn/grp       | String | Input source group (LCL, USB, A, B, C, etc.) |
| /ch/N/in/conn/in        | Int    | Input source number within group |
| /ch/N/in/conn/altgrp    | String | Alt input source group   |
| /ch/N/in/conn/altin     | Int    | Alt input source number  |
| /ch/N/in/set/trim       | Float  | Input trim (dB)          |
| /ch/N/in/set/inv        | Int    | Polarity invert          |
| /ch/N/in/set/bal        | Float  | Input balance            |
| /ch/N/in/set/dly        | Float  | Input delay (ms)         |
| /ch/N/in/set/srcauto    | Int    | Auto source switching    |
| /ch/N/in/set/altsrc     | Int    | Alt source active        |

### Processing Order

| Path            | Type   | Description              |
| --------------- | ------ | ------------------------ |
| /ch/N/proc      | String | Process order — combination of G(ate), E(Q), D(ynamics), I(nsert) |
| /ch/N/ptap      | String | Pre-tap point for sends  |

Default order: `GEDI` (Gate → EQ → Dynamics → Insert). Change to `GDEI` to put compressor before EQ.

### Filter

| Path            | Type   | Description              |
| --------------- | ------ | ------------------------ |
| /ch/N/flt/lc    | Int    | Low cut on/off           |
| /ch/N/flt/lcf   | Float  | Low cut frequency (Hz)   |
| /ch/N/flt/hc    | Int    | High cut on/off          |
| /ch/N/flt/hcf   | Float  | High cut frequency (Hz)  |
| /ch/N/flt/tf    | Int    | Tilt filter on/off       |
| /ch/N/flt/mdl   | String | Filter model             |

#### Filter Plugin Models

| Model | Name           | Parameters |
| ----- | -------------- | ---------- |
| TILT  | Tilt EQ        | tilt [-6..6] |
| MAXER | Sound Maxer    | low [0..100]%, proc [0..100]% |
| AP1   | All-Pass 90°   | freq [100..10000] Hz |
| AP2   | All-Pass 180°  | f [100..10000] Hz, q [0.442..10] |

### Pre-EQ (3-band)

| Path            | Type   | Description              |
| --------------- | ------ | ------------------------ |
| /ch/N/peq/on    | Int    | PEQ on/off               |
| /ch/N/peq/1g    | Float  | Band 1 gain (dB)         |
| /ch/N/peq/1f    | Float  | Band 1 frequency (Hz)    |
| /ch/N/peq/1q    | Float  | Band 1 Q                 |
| /ch/N/peq/2g    | Float  | Band 2 gain (dB)         |
| /ch/N/peq/2f    | Float  | Band 2 frequency (Hz)    |
| /ch/N/peq/2q    | Float  | Band 2 Q                 |
| /ch/N/peq/3g    | Float  | Band 3 gain (dB)         |
| /ch/N/peq/3f    | Float  | Band 3 frequency (Hz)    |
| /ch/N/peq/3q    | Float  | Band 3 Q                 |

### EQ (6-band + shelves)

| Path            | Type   | Description              |
| --------------- | ------ | ------------------------ |
| /ch/N/eq/on     | Int    | EQ on/off                |
| /ch/N/eq/mdl    | String | EQ model (see plugin list)|
| /ch/N/eq/mix    | Float  | EQ mix/blend (0-125%)    |
| /ch/N/eq/lg     | Float  | Low shelf gain (dB)      |
| /ch/N/eq/lf     | Float  | Low shelf frequency (Hz) |
| /ch/N/eq/lq     | Float  | Low shelf Q              |
| /ch/N/eq/leq    | String | Low shelf type (SHV, PEQ)|
| /ch/N/eq/1g-4g  | Float  | Band 1-4 gain (dB)       |
| /ch/N/eq/1f-4f  | Float  | Band 1-4 frequency (Hz)  |
| /ch/N/eq/1q-4q  | Float  | Band 1-4 Q               |
| /ch/N/eq/hg     | Float  | High shelf gain (dB)     |
| /ch/N/eq/hf     | Float  | High shelf frequency (Hz)|
| /ch/N/eq/hq     | Float  | High shelf Q             |
| /ch/N/eq/heq    | String | High shelf type (SHV, PEQ)|

#### EQ Plugin Models

| Model  | Full Name              | Real Hardware       | Key Parameters |
| ------ | ---------------------- | ------------------- | -------------- |
| STD    | Wing Standard EQ       | —                   | 4-band para + shelves |
| SOUL   | Soul Analogue          | SSL 4000            | lf, lg, lmf, lmg, lmq, hmf, hmg, hmq, hf, hg |
| E88    | Even 88 Formant        | Neve 1088           | 4-band with bell/shelf select, Q per band |
| E84    | Even 84                | Neve 1084           | 3-band with fixed freq selectors |
| F110   | Fortissimo 110         | Focusrite ISA 110   | Parametric + shelves, gain |
| PULSAR | Pulsar P1a/M5          | Pultec EQP-1A/MEQ-5 | Boost/attenuate, fixed freq selectors |
| MACH4  | Mach EQ4               | Massive Passive     | sub, 40, 160, 650, 2k5, air |

Note: Buses, mains, and matrices have **8-band** parametric EQ (bands 1-6 + shelves + tilt).

### Gate

| Path              | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| /ch/N/gate/on     | Int    | Gate on/off              |
| /ch/N/gate/mdl    | String | Gate model               |
| /ch/N/gate/thr    | Float  | Threshold (dB)           |
| /ch/N/gate/range  | Float  | Range (dB)               |
| /ch/N/gate/att    | Float  | Attack (ms)              |
| /ch/N/gate/hld    | Float  | Hold (ms)                |
| /ch/N/gate/rel    | Float  | Release (ms)             |

#### Gate Sidechain

| Path              | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| /ch/N/gatesc/type | String | Filter type (OFF, BP, LP6, LP12, HP6, HP12) |
| /ch/N/gatesc/f    | Float  | Sidechain frequency (Hz) |
| /ch/N/gatesc/q    | Float  | Sidechain Q              |
| /ch/N/gatesc/src  | String | Sidechain source (SELF or external) |
| /ch/N/gatesc/tap  | String | Sidechain tap point (IN) |

#### Gate Plugin Models

| Model | Full Name              | Real Hardware       |
| ----- | ---------------------- | ------------------- |
| GATE  | Standard Gate/Expander | —                   |
| DUCK  | Standard Ducker        | —                   |
| E88   | Even 88 Gate           | Neve 1088 Gate      |
| 9000G | Soul 9000 Gate         | SSL 9000 Gate       |
| D241G | DrawMore 241           | Drawmer 241         |
| DS902 | BDX 902 DeEsser        | DBX 902             |
| DEQ   | Dynamic EQ             | —                   |
| WAVE  | Wave Designer          | SPL Transient Designer |
| WARM  | Soul Warmth Preamp     | — (drive, harmonics, color, trim) |
| 76LA  | 76 Limiter Amp         | UREI 1176 (in/out/att/rel/ratio) |
| LA    | Leveling Amp 2A        | LA-2A (gain, peak, comp/lim) |
| RIDE  | Auto Rider             | — (threshold, target, speed, ratio) |

### Dynamics (Compressor)

| Path              | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| /ch/N/dyn/on      | Int    | Dynamics on/off          |
| /ch/N/dyn/mdl     | String | Dynamics model           |
| /ch/N/dyn/mix     | Float  | Dry/wet mix (0-100%) — **use for parallel compression** |
| /ch/N/dyn/gain    | Float  | Makeup gain (dB)         |
| /ch/N/dyn/thr     | Float  | Threshold (dB)           |
| /ch/N/dyn/knee    | Float  | Knee (0-5)               |
| /ch/N/dyn/ratio   | Float  | Ratio                    |
| /ch/N/dyn/det     | String | Detection (PEAK, RMS)    |
| /ch/N/dyn/att     | Float  | Attack (ms)              |
| /ch/N/dyn/hld     | Float  | Hold (ms)                |
| /ch/N/dyn/rel     | Float  | Release (ms)             |
| /ch/N/dyn/env     | String | Envelope (LIN, LOG)      |
| /ch/N/dyn/auto    | Int    | Auto makeup gain         |

#### Dynamics Sidechain

| Path              | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| /ch/N/dynsc/type  | String | Filter type (OFF, BP, LP6, LP12, HP6, HP12) |
| /ch/N/dynsc/f     | Float  | Sidechain frequency (Hz) |
| /ch/N/dynsc/q     | Float  | Sidechain Q              |
| /ch/N/dynsc/src   | String | Sidechain source (SELF or external) |
| /ch/N/dynsc/tap   | String | Sidechain tap point      |
| /ch/N/dynxo/depth | Float  | Crossover depth (dB)     |
| /ch/N/dynxo/type  | String | Crossover type (OFF, etc.)|
| /ch/N/dynxo/f     | Float  | Crossover frequency (Hz) |

#### Dynamics Plugin Models

| Model | Full Name              | Real Hardware              |
| ----- | ---------------------- | -------------------------- |
| COMP  | Wing Standard Comp     | — (full controls)          |
| EXP   | Wing Standard Expander | —                          |
| B160  | BDX 160                | DBX 160 (thr, ratio)       |
| B560  | BDX 560 Easy           | DBX 560A (thr, ratio, auto)|
| D241C | DrawMore Comp          | Drawmer 241 (full + limiter)|
| ECL33 | Even Comp/Limiter      | Neve 33609 (comp + lim sections) |
| 9000C | Soul 9000 Channel      | SSL 9000 Channel Comp      |
| SBUS  | Soul G Bus Comp        | SSL G Bus Comp (thr, ratio, att, rel) |
| RED3  | Red 3 Compressor       | Focusrite Red 3            |
| 76LA  | 76 Limiter Amp         | UREI 1176                  |
| LA    | Leveling Amp 2A        | LA-2A (gain, peak, comp/lim)|
| F670  | Fairkid 670            | Fairchild 670 (in, thr, time, bias) |
| BLISS | Eternal Bliss          | Elysia mPressor            |
| NSTR  | No Stressor            | Empirical Labs Distressor  |
| WAVE  | Wave Designer          | SPL Transient Designer     |
| RIDE  | Auto Rider             | —                          |

### Sends

| Path                   | Type   | Description              |
| ---------------------- | ------ | ------------------------ |
| /ch/N/main/M/on        | Int    | Main bus M assign on/off (M=1-4) |
| /ch/N/main/M/lvl       | Float  | Main bus M send level (dB) |
| /ch/N/send/B/on        | Int    | Bus B send on/off (B=1-16) |
| /ch/N/send/B/lvl       | Float  | Bus B send level (dB)    |
| /ch/N/send/B/mode      | String | Bus B send mode (PRE, POST) |
| /ch/N/send/B/pan       | Float  | Bus B send pan           |
| /ch/N/send/B/wid       | Float  | Bus B send width         |
| /ch/N/send/B/pon       | Int    | Bus B pan on             |
| /ch/N/send/B/ind       | Int    | Bus B independent        |
| /ch/N/send/B/plink     | Int    | Bus B pan link           |

### Insert

| Path                   | Type   | Description              |
| ---------------------- | ------ | ------------------------ |
| /ch/N/preins/on        | Int    | Pre-insert on/off        |
| /ch/N/preins/ins       | String | Pre-insert FX slot (e.g. "FX9", "NONE") |
| /ch/N/postins/on       | Int    | Post-insert on/off       |
| /ch/N/postins/ins      | String | Post-insert FX slot (e.g. "FX12", "NONE") |
| /ch/N/postins/mode     | String | Post-insert mode (FX)    |
| /ch/N/postins/w        | Float  | Post-insert wet/dry (0.0-1.0) |

An FX slot can only be inserted on one channel at a time. Assigning an effect to a new channel removes it from the previous one.

## Auxiliary Channels (/aux/N/...)

8 aux channels available. Same structure as channels but with 2-band EQ (no gate, no filter plugins).

| Path              | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| /aux/N/name       | String | Aux name                 |
| /aux/N/fdr        | Float  | Fader level (dB)         |
| /aux/N/mute       | Int    | Mute                     |
| /aux/N/pan        | Float  | Pan                      |
| /aux/N/eq/...     |        | 2-band EQ                |
| /aux/N/preins/... |        | Pre-insert               |
| /aux/N/main/...   |        | Main bus assigns (1-4)   |
| /aux/N/send/...   |        | Bus sends (1-16)         |

## Input Sources (/io/in/...)

### Source Groups

| Group | Description                  | Count |
| ----- | ---------------------------- | ----- |
| LCL   | Local analog inputs          | 1-8 (Wing Rack) |
| AUX   | Auxiliary inputs             | 1-8   |
| A     | AES50 A inputs               | 1-48  |
| B     | AES50 B inputs               | 1-48  |
| C     | AES50 C inputs               | 1-48  |
| SC    | StageConnect inputs          | 1-32  |
| USB   | USB inputs                   | 1-48  |
| CRD   | Card inputs                  | 1-64  |
| MOD   | Module inputs                | 1-64  |
| PLAY  | USB player inputs            | 1-4   |
| AES   | AES digital inputs           | 1-2 (stereo pair) |
| USR   | User signal inputs           | 1-24  |
| OSC   | Oscillator inputs            | 1-2   |

### Per-Input Parameters

| Path                   | Type   | Description              |
| ---------------------- | ------ | ------------------------ |
| /io/in/GRP/N/name      | String | Input name (16 chars max) -- **this is what shows on the channel display** |
| /io/in/GRP/N/icon      | Int    | Input icon (0-999)       |
| /io/in/GRP/N/col       | Int    | Input color (1-12)       |
| /io/in/GRP/N/mode      | String | Mode (M=mono, ST=stereo, M/S=mid-side) |
| /io/in/GRP/N/mute      | Int    | Input mute               |
| /io/in/GRP/N/g         | Float  | Gain (dB) -- LCL, A, B, C, SC only |
| /io/in/GRP/N/vph       | Int    | Virtual phantom -- LCL, A, B, C, SC only |
| /io/in/GRP/N/tags      | String | Tags                     |

## Output Routing (/io/out/...)

### Output Groups

| Group | Description                  |
| ----- | ---------------------------- |
| LCL   | Local analog outputs (1-8)   |
| AUX   | Auxiliary outputs (1-8)      |
| A     | AES50 A outputs (1-48)       |
| B     | AES50 B outputs (1-48)       |
| C     | AES50 C outputs (1-48)       |
| SC    | StageConnect outputs (1-32)  |
| USB   | USB outputs (1-48)           |
| CRD   | Card outputs (1-64)          |
| MOD   | Module outputs               |
| REC   | Recorder outputs (1-4)       |
| AES   | AES digital outputs (1-2)    |

### Per-Output Parameters

| Path                   | Type   | Description              |
| ---------------------- | ------ | ------------------------ |
| /io/out/GRP/N/grp      | String | Source group (OFF, CH, AUX, BUS, MAIN, MTX, etc.) |
| /io/out/GRP/N/in       | Int    | Source number             |

### User Signal Routing

User signal source routing lives under the input source at `/io/in/USR/N/user/...`, NOT under `/io/out/` or `/io/user/`.

| Path                        | Type   | Description              |
| --------------------------- | ------ | ------------------------ |
| /io/in/USR/N/user/grp       | String | Source group (OFF, CH, AUX, BUS, MAIN, MTX, etc.) |
| /io/in/USR/N/user/in        | Int    | Source number             |
| /io/in/USR/N/user/tap       | String | Tap point (PRE, POST)    |
| /io/in/USR/N/user/lr        | String | Channel select (L+R, L, R) |

## Buses (/bus/N/...)

16 buses available. Buses have 8-band parametric EQ, dynamics, pre/post inserts, and matrix sends.

| Path              | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| /bus/N/name       | String | Bus name (16 chars max)  |
| /bus/N/fdr        | Float  | Fader level (dB)         |
| /bus/N/mute       | Int    | Mute                     |
| /bus/N/pan        | Float  | Pan                      |
| /bus/N/wid        | Float  | Width                    |
| /bus/N/busmono    | Int    | Mono switch              |
| /bus/N/busmode    | String | Bus mode (PRE, POST)     |
| /bus/N/eq/...     |        | 8-band EQ (bands 1-6 + shelves + tilt) |
| /bus/N/dyn/...    |        | Same dynamics structure as channels |
| /bus/N/dynsc/...  |        | Dynamics sidechain       |
| /bus/N/preins/... |        | Pre-insert               |
| /bus/N/postins/...|        | Post-insert              |
| /bus/N/main/M/on  | Int    | Main bus M assign        |
| /bus/N/main/M/lvl | Float  | Main bus M send level    |
| /bus/N/send/M/on  | Int    | Matrix M send on/off     |
| /bus/N/send/M/lvl | Float  | Matrix M send level      |
| /bus/N/dly/on     | Int    | Delay on/off             |
| /bus/N/dly/dly    | Float  | Delay time               |

## Mains (/main/N/...)

4 main buses. Same structure as buses (8-band EQ, dynamics, inserts).

| Path              | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| /main/N/name      | String | Main name (16 chars max) |
| /main/N/fdr       | Float  | Fader level (dB)         |
| /main/N/mute      | Int    | Mute                     |
| /main/N/pan       | Float  | Pan                      |
| /main/N/eq/...    |        | 8-band EQ                |
| /main/N/dyn/...   |        | Dynamics                 |
| /main/N/preins/...|        | Pre-insert               |
| /main/N/postins/..|        | Post-insert              |
| /main/N/send/M/on | Int    | Matrix M send on/off     |
| /main/N/send/M/lvl| Float  | Matrix M send level      |

## Matrix Buses (/mtx/N/...)

8 matrix buses. Same structure as mains (8-band EQ, dynamics, inserts, delay).

| Path              | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| /mtx/N/name       | String | Matrix name              |
| /mtx/N/fdr        | Float  | Fader level (dB)         |
| /mtx/N/mute       | Int    | Mute                     |
| /mtx/N/pan        | Float  | Pan                      |
| /mtx/N/dir/D/on   | Int    | Direct input D on/off    |
| /mtx/N/dir/D/lvl  | Float  | Direct input D level     |
| /mtx/N/dir/D/in   | String | Direct input D source    |
| /mtx/N/dir/D/tap  | String | Direct input D tap point |
| /mtx/N/eq/...     |        | 8-band EQ                |
| /mtx/N/dyn/...    |        | Dynamics                 |
| /mtx/N/dly/on     | Int    | Delay on/off             |
| /mtx/N/dly/m      | Float  | Delay (meters)           |

## DCAs (/dca/N/...)

8 DCAs available.

| Path              | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| /dca/N/name       | String | DCA name                 |
| /dca/N/fdr        | Float  | Fader level (dB)         |
| /dca/N/mute       | Int    | Mute                     |
| /dca/N/icon       | Int    | Icon                     |
| /dca/N/col        | Int    | Color (1-12)             |
| /dca/N/led        | Int    | Scribble light           |
| /dca/N/mon        | String | Monitor output (A, B)    |

## Mute Groups (/mgrp/N/...)

8 mute groups available.

| Path              | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| /mgrp/N/name      | String | Mute group name          |
| /mgrp/N/mute      | Int    | Mute group on/off        |

## Effects (/fx/N/...)

16 FX slots: 1-8 premium, 9-16 standard. Premium slots can run standard effects too.

| Path              | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| /fx/N/mdl         | String | Effect model name        |
| /fx/N/fxmix       | Float  | FX mix/blend (0-100)     |
| /fx/N/$esrc       | Int    | External source [RO]     |
| /fx/N/$emode      | String | External mode (M, ST, M/S) [RO] |
| /fx/N/$a_chn      | Int    | Assigned channel [RO]    |
| /fx/N/$a_pos      | Int    | Assigned position [RO]   |

Parameters beyond these depend on the loaded model. Query the FX node to discover available parameters.

### Premium Effects

| Model    | Name              | Key Parameters |
| -------- | ----------------- | -------------- |
| NONE     | No effect         | — |
| EXT      | External          | egrp, ein, emode, lat, trim |
| HALL     | Hall Reverb       | pdel, size, dcy, mult, damp, lc, hc, shp, sprd, diff, mspd |
| ROOM     | Room Reverb       | pdel, size, dcy, mult, damp, lc, hc, shp, sprd, diff, spin, ecl, ecr, efl, efr |
| CHAMBER  | Chamber Reverb    | pdel, size, dcy, mult, damp, lc, hc, shp, sprd, diff, spin, ecl, ecr |
| PLATE    | Plate Reverb      | pdel, size, dcy, mult, damp, lc, hc, att, sprd, diff, spin, ecl, ecr, efl, efr |
| CONCERT  | Concert Reverb    | pdel, size, dcy, mult, damp, lc, hc, shp, sprd, diff, depth, rfl, rfr, spin, crs |
| AMBI     | Ambience          | pdel, size, dcy, tail, damp, diff, mod, lc, hc |
| V-ROOM   | Vintage Room / VSS3 | pdel, size, dcy, dens, erlvl, lmult, hmult, lc, hc, frz |
| V-REV    | Vintage Reverb    | pdel, dcy, lmult, hmult, mod, lc, hc, out, trans |
| V-PLATE  | Vintage Plate     | pdel, dcy, lc, col |
| GATED    | Gated Reverb      | pdel, att, dcy, dens, diff, sprd, lc, hfs, hsg |
| REVERSE  | Reverse Reverb    | pdel, rise, dcy, diff, sprd, lc, hfs, hsg |
| DEL/REV  | Delay/Reverb      | time, feed, fhc, dly, d2r, pdel, size, dcy, damp, rlc, i2r |
| SHIMMER  | Shimmer Reverb    | pdel, size, dcy, lc, hc, damp, shim, shine |
| SPRING   | Spring Reverb     | dcy, dens, low, high |
| DIMCRS   | Dimension CRS     | sw1-sw4, in, drysw |
| CHORUS   | Stereo Chorus     | lc, hc, wave, phase, mix, dlyl, dlyr, depl, depr, sprd, spd |
| FLANGER  | Stereo Flanger    | lc, hc, flc, fhc, mix, dlyl, dlyr, depl, depr, phase, spd, feed |
| ST-DL    | Stereo Delay      | time, mode, fact, pat, offset, feed, flc, fhc, lc, hc |
| TAP-DL   | Ultratap Delay    | time, rep, slp, fact, pdel, mode, wid, diff, lc, hc |
| TAPE-DL  | Tape Delay        | time, sust, drv, wf |
| OILCAN   | Oil Can Delay     | time (seconds), sust, wb, tone |
| BBD-DL   | BBD Delay         | dly, feed |
| PITCH    | Stereo Pitch      | semi, cent, dly, lc, hc, mix |
| D-PITCH  | Dual Pitch        | semi1, cent1, dly1, pan1, lvl1, semi2, cent2, dly2, pan2, lvl2, lc, hc |

### Standard Effects

| Model    | Name              | Key Parameters |
| -------- | ----------------- | -------------- |
| NONE     | No effect         | — |
| EXT      | External          | egrp, ein, emode, lat, trim |
| GEQ      | Graphic EQ        | 31-band (20Hz-20kHz), type (STD/TRU) |
| PIA      | PIA 560 GEQ       | mix, gain, 10-band (31-16k) |
| C5-CMB   | Combinator        | 5-band multiband comp with per-band thr/gain/bypass/crossover |
| DOUBLE   | Double Vocal      | mode (TIGHT/LOOSE/GROUP/DETUNE/THICK), mix, sprd |
| PCORR    | Pitch Fix         | spd, amnt, a4, per-note on/off |
| LIMITER  | Precision Limiter | gin, gout, sqz, knee, att, rel |
| DE-S2    | 2-Band DeEsser    | lo, hi, los, his, gdr, mode |
| ENHANCE  | Ultra Enhancer    | stlvl, bass, mid, high, solo |
| EXCITER  | Exciter           | tune, peak, zfill, timbre, harm, mix |
| P-BASS   | Psycho Bass       | int, bass, xf, solo |
| ROTARY   | Rotary Speaker    | sw (STOP/SLOW/FAST), lo, hi, bal, mix, dist |
| PHASER   | Phaser            | spd, phase, wave, range, depth, emod, att, hld, rel, mix, stg, reso |
| PANNER   | Tremolo/Panner    | att, hld, rel, espd, edep, spd, phase, wave, depth |
| TAPE     | Tape Machine      | drv, spd, low, hi, out |
| MOOD     | Mood Filter       | fbase, filt (LP/HP/BP/NOTCH), slope, reso, drv, env, att, hld, rel, mix, lfo, spd, phase, wave |
| BODY     | Bodyrez           | body |
| SUB      | Sub Octaver       | rng (LOW/MID/HIGH), oct1, oct2 |
| RACKAMP  | Rack Amp          | pre, buzz, punch, crunch, drive, out, leq, heq, cab |
| UKROCK   | UK Rock Amp       | gain, bass, mid, treb, pres, mstr, out, sag, cab |
| ANGEL    | Angel Amp         | gain, bass, mid, treb, pres, mstr, out, sag, cab, midb, bri, bt |
| JAZZC    | Jazz Clean Amp    | vol, bass, mid, treb, out, bri, cab |
| DELUXE   | Deluxe Amp        | vol, bass, treb, out, sag, cab |
| SOUL     | Soul Analogue (as FX) | mix, lf, lg, lmf, lmg, lmq, hmf, hmg, hmq, hf, hg |
| E88      | Even 88 (as FX)   | mix, lf, lg, lq, lt, lmf, lmg, lmq, hmf, hmg, hmq, hf, hg, hq, ht |
| E84      | Even 84 (as FX)   | mix, g, lf, lg, mf, mg, mq, hf, hg |
| F110     | Fortissimo 110 (as FX) | mix, peq, lmf, lmg, lmq, hmf, hmg, hmq, shv, lf, lg, hf, hg, g |
| PULSAR   | Pulsar (as FX)    | mix, eq1, eq5, boost/atten/freq per section |
| MACH4    | Mach EQ4 (as FX)  | mix, sub, 40, 160, 650, 2k5, air, airm, again |

### Channel Strip FX (Full Channel Emulations)

These are **complete channel strip emulations** loaded as FX slot effects. They include gate, EQ, and compressor sections in one unit. Each instance uses one FX slot. Load via `/fx/N/mdl`.

| Model      | Name               | Real Hardware       |
| ---------- | ------------------ | ------------------- |
| \*EVEN\*   | Even Channel       | Neve console channel strip |
| \*SOUL\*   | Soul Channel       | SSL console channel strip |
| \*VINTAGE\*| Vintage Channel    | Vintage console channel strip |
| \*BUS\*    | Bus Channel        | Bus compressor channel |
| \*MASTER\* | Master Channel     | Mastering channel strip |

To use a channel strip on a channel:
1. Load into an available FX slot: `/fx/12/mdl s "*EVEN*"`
2. Assign as channel insert: `/ch/2/postins/ins s "FX12"`
3. Enable the insert: `/ch/2/postins/on i 1`
4. Set wet/dry to 100%: `/ch/2/postins/w f 1.0`

**Note:** Each FX slot is a single instance. To use the same channel strip on two channels, load it into two separate FX slots.

### Common FX Parameters

| Path           | Type   | Description              |
| -------------- | ------ | ------------------------ |
| /fx/N/time     | Float  | Delay time (ms)          |
| /fx/N/speed    | Float  | Rate/speed (Hz)          |
| /fx/N/pdel     | Float  | Pre-delay (ms)           |
| /fx/N/dcy      | Float  | Decay (seconds)          |
| /fx/N/mix      | Float  | Effect mix (%)           |
| /fx/N/feed     | Float  | Feedback (%)             |
| /fx/N/lc       | Float  | Low cut (Hz)             |
| /fx/N/hc       | Float  | High cut (Hz)            |
| /fx/N/size     | Float  | Room/reverb size         |
| /fx/N/diff     | Float  | Diffusion                |
| /fx/N/spin     | Float  | Spin/modulation          |
| /fx/N/sprd     | Float  | Spread                   |

## Configuration (/cfg/...)

### Monitor Section

| Path              | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| /cfg/mon/N/src    | String | Monitor source (e.g. "MAIN.1") |
| /cfg/mon/N/dim    | Float  | Dim level (dB)           |
| /cfg/mon/N/dly/on | Int   | Monitor delay on/off     |
| /cfg/mon/N/dly/m  | Float  | Monitor delay (meters)   |
| /cfg/mon/N/inv    | Int    | Phase invert             |
| /cfg/mon/N/pan    | Float  | Monitor pan              |

### Solo

| Path              | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| /cfg/solo/mode    | String | Solo mode (LIVE, etc.)   |
| /cfg/solo/mon     | String | Solo monitor output (A, B) |
| /cfg/solo/mute    | Int    | Solo mute                |
| /cfg/solo/chtap   | String | Channel solo tap (PFL, AFL) |
| /cfg/solo/bustap  | String | Bus solo tap (PFL, AFL)  |

### Talkback

| Path              | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| /cfg/talk/assign  | String | Talkback source (OFF or input) |
| /cfg/talk/A/mode  | String | Talkback A mode (AUTO, etc.) |
| /cfg/talk/A/mondim| Int    | Dim monitors during talkback |
| /cfg/talk/A/B1-B16| Int    | Talkback A to bus 1-16   |
| /cfg/talk/A/M1-M4 | Int    | Talkback A to main 1-4   |

### Oscillator

| Path              | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| /cfg/osc/N/lvl    | Float  | Oscillator level (dB)    |
| /cfg/osc/N/mode   | String | Waveform (SINE, etc.)    |
| /cfg/osc/N/f      | Float  | Frequency (Hz)           |

### Clock

| Path              | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| /cfg/clkrate      | Int    | Sample rate (44100, 48000) |
| /cfg/clksrc       | String | Clock source (INT, etc.) |

## DAW Control (/$ctl/daw/...)

| Path              | Type   | Description              |
| ----------------- | ------ | ------------------------ |
| /$ctl/daw/on      | Int    | DAW mode on/off          |
| /$ctl/daw/conn    | String | Connection type (USB, etc.) |
| /$ctl/daw/emul    | String | DAW emulation (MCU, HUI) |
| /$ctl/daw/config  | String | DAW config (CC, MSTR, MSTR1EXT, MSTR2EXT, MCU+EXTENDER) |
| /$ctl/daw/$on     | Int    | DAW mode active [RO]     |

## Subscriptions

One subscription active at a time. Must renew every 10 seconds.

| Command     | Description                              |
| ----------- | ---------------------------------------- |
| /*b         | Subscribe to binary event messages       |
| /*s         | Subscribe to OSC events (multi-tag)      |
| /*S         | Subscribe to OSC events (single-tag)     |
| /%PORT/*s   | Subscribe, send events to specific port  |

## Shows and Scenes

Shows are collections of up to 1000 scenes. Scenes can contain snapshots, snippets, presets, or audio clips.

### MIDI Scene Control

| MIDI Command  | Action              |
| ------------- | ------------------- |
| Ch7 CC32+PC   | Recall scene by bank/program (up to 16384) |
| Ch8 PC 1-128  | Recall scene by tag #1-#128 |
| Ch9 PC 1      | Scene GO            |
| Ch9 PC 2      | Scene PREV          |
| Ch9 PC 3      | Scene NEXT          |
| Ch9 PC 4      | Scene GO PREV       |
| Ch9 PC 5      | Scene GO NEXT       |

### Snapshot Scope

Snapshots save the full console state (~460KB, ~28800 lines of JSON). Scopes limit which sections are recalled: ch (1-40), aux (1-8), bus (1-16), main (1-4), mtx (1-8), fx (1-16), routin, routout, cfg, area (L/C/R surface sections), data.

## Icon Ranges

| Range   | Category           |
| ------- | ------------------ |
| 0-14    | General            |
| 100-114 | Vocals and Mics    |
| 200-224 | Drums and Percussion |
| 300-319 | Strings and Winds  |
| 400-409 | Keys               |
| 500-524 | Speakers           |
| 600-614 | Specials           |

## Color Map

| Value | Color            |
| ----- | ---------------- |
| 1     | Gray Blue        |
| 2     | Medium Blue      |
| 3     | Dark Blue        |
| 4     | Turquoise        |
| 5     | Green            |
| 6     | Olive Green      |
| 7     | Yellow           |
| 8     | Orange           |
| 9     | Red              |
| 10    | Coral            |
| 11    | Pink             |
| 12    | Mauve            |

## Useful Patterns

### Set all channel names from config

```sh
# scripts/set-channel-names.sh
oscsend 192.168.2.2 2223 /io/in/LCL/1/name s "Guitar Dry"
```

### Query a channel's input source

```sh
# Returns the source group (LCL, USB, etc.)
oscsend 192.168.2.2 2223 /ch/1/in/conn/grp
```

### Mute/unmute a channel

```sh
oscsend 192.168.2.2 2223 /ch/1/mute i 1   # mute
oscsend 192.168.2.2 2223 /ch/1/mute i 0   # unmute
```

### Set fader level

```sh
oscsend 192.168.2.2 2223 /ch/1/fdr f -10.0  # -10 dB
```

### Load an FX model

```sh
oscsend 192.168.2.2 2223 /fx/1/mdl s "ST-DL"
```

### Set FX delay time

```sh
oscsend 192.168.2.2 2223 /fx/1/time f 500.0  # 500ms
```

### Batch set multiple parameters

```sh
# Set ch1 and ch2 faders and mutes in one command (Python required for raw OSC)
# /  ,s  /ch.1.fdr=-10,mute=0,.2.fdr=-6,mute=0
```

### Load a channel strip insert

```sh
# Load Even (Neve) channel strip into FX slot 12
oscsend 192.168.2.2 2223 /fx/12/mdl s "*EVEN*"
# Insert on channel 2
oscsend 192.168.2.2 2223 /ch/2/postins/ins s "FX12"
oscsend 192.168.2.2 2223 /ch/2/postins/on i 1
oscsend 192.168.2.2 2223 /ch/2/postins/w f 1.0
```

### Change processing order

```sh
# Put compressor before EQ on channel 3
oscsend 192.168.2.2 2223 /ch/3/proc s "GDEI"
```

### Set channel EQ plugin model

```sh
# Load Neve 1084 EQ on channel 2
oscsend 192.168.2.2 2223 /ch/2/eq/mdl s "E84"
```

## Protocol Source

Patrick-Gilles Maillot, "WING Remote Protocols v3.0.5", authorized by Behringer.
Full PDF: https://wing-docs.com/pdf/OSC_Documentation.pdf
See also: https://github.com/pmaillot/wapi (native binary API)
