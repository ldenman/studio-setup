#!/bin/bash
# Sets up Wing ch5 as "Vocal LA2A" — a copy of the vocal dry input
# with the Wing's built-in LA-2A dynamics plugin loaded.
#
# Ch3 = Vocal Dry (mic, no processing)
# Ch4 = Vocal Processed (outboard Opto return)
# Ch5 = Vocal LA2A (fed from ch3 via User Signal routing, Wing LA-2A plugin)
#
# Routing: Vocal Mic → Ch3 (Vocal Dry) → USR/1 (user signal) → Ch5
# User Signal routing lives under /io/in/USR/N/user/ (source config).
# The display name comes from /io/in/USR/N/name.
# PRE tap means ch5 gets signal regardless of ch3's fader/mute/solo state.

WING_IP="${1:-192.168.2.2}"
WING_PORT=2223

echo "Setting up ch5 as Vocal LA2A on Wing at $WING_IP..."

# Configure User Signal 1: source = Ch3, pre-fader tap
oscsend "$WING_IP" "$WING_PORT" /io/in/USR/1/user/grp s "CH"
oscsend "$WING_IP" "$WING_PORT" /io/in/USR/1/user/in i 3
oscsend "$WING_IP" "$WING_PORT" /io/in/USR/1/user/tap s "PRE"
oscsend "$WING_IP" "$WING_PORT" /io/in/USR/1/user/lr s "L+R"

# Name and color User Signal 1 (this is what ch5 displays)
oscsend "$WING_IP" "$WING_PORT" /io/in/USR/1/name s "Vocal LA2A"
oscsend "$WING_IP" "$WING_PORT" /io/in/USR/1/col i 2

# Point ch5 at User Signal input 1
oscsend "$WING_IP" "$WING_PORT" /ch/5/in/conn/grp s "USR"
oscsend "$WING_IP" "$WING_PORT" /ch/5/in/conn/in i 1

# Load LA-2A dynamics model and enable
oscsend "$WING_IP" "$WING_PORT" /ch/5/dyn/mdl s "LA"
oscsend "$WING_IP" "$WING_PORT" /ch/5/dyn/on i 1
oscsend "$WING_IP" "$WING_PORT" /ch/5/dyn/mix f 100.0

# High-pass at 80Hz (standard for vocals)
oscsend "$WING_IP" "$WING_PORT" /ch/5/flt/lc i 1
oscsend "$WING_IP" "$WING_PORT" /ch/5/flt/lcf f 80.0

# Fader to unity, unmute, route to main
oscsend "$WING_IP" "$WING_PORT" /ch/5/fdr f 0.0
oscsend "$WING_IP" "$WING_PORT" /ch/5/mute i 0
oscsend "$WING_IP" "$WING_PORT" /ch/5/main/1/on i 1

echo "Done. Ch5 = Vocal LA2A (fed from ch3 via USR/1, LA-2A dynamics loaded)"
