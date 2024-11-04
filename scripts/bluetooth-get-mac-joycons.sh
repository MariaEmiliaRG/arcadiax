#!/bin/bash

bluetoothctl power on > /dev/null &
bluetoothctl scan on > /dev/null &
SCAN_PID=$!


macJoyConL=""
macJoyConR=""

while [ -z "$macJoyConR" ] && [ -z "$macJoyConL" ]; do
    macJoyConR=$(bluetoothctl devices | grep "Joy-Con (R)" | awk '{print $2}')
    macJoyConL=$(bluetoothctl devices | grep "Joy-Con (L)" | awk '{print $2}')
    sleep 1
done

kill $SCAN_PID

echo "{\"macJoyConR\": \"$macJoyConR\", \"macJoyConL\": \"$macJoyConL\"}"

