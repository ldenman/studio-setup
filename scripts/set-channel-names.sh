#!/bin/bash
# Sets Wing Rack channel names and colors from the recording config.
# Usage: ./set-channel-names.sh [wing-ip]
#
# Color map:
#   1=Dark Purple  2=Blue    3=Purple  4=Greenish Blue
#   5=Green        6=Highlighter Green  7=Yellow  8=Brown
#   9=Red         10=Peach  11=Pink   12=Purple

WING_IP="${1:-192.168.2.2}"
WING_PORT=2223

# Guitar (Red)
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/1/name s "Guitar Dry"
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/1/col i 9
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/2/name s "Guitar Proc"
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/2/col i 9

# Vocal (Blue)
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/3/name s "Vocal Dry"
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/3/col i 2
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/4/name s "Vocal Proc"
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/4/col i 2

# Vocal LA2A (Blue)
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/5/name s "Vocal LA2A"
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/5/col i 2

# Open Local (Brown)
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/6/col i 8
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/7/col i 8
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/8/col i 8

# DAW / Session (Green)
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/9/name s "Bass"
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/9/col i 5
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/10/name s "Keyboard"
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/10/col i 5
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/11/name s "Synth/Piano L"
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/11/col i 5
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/12/name s "Synth/Piano R"
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/12/col i 5
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/13/name s "Drums L"
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/13/col i 5
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/14/name s "Drums R"
oscsend "$WING_IP" "$WING_PORT" /io/in/LCL/14/col i 5

echo "Channel names and colors set on Wing Rack at $WING_IP"
