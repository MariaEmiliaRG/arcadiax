#!/bin/bash

# Función para conectar un dispositivo Bluetooth
connectDevice() {
    local macAddress=$1
    bluetoothctl pair $macAddress
    sleep 30
    bluetoothctl connect $macAddress
    sleep 30
}

bluetoothctl power on
bluetoothctl agent on
bluetoothctl default-agent
bluetoothctl scan on > /dev/null &
SCAN_PID=$!


macJoyConL=""
macJoyConR=""

while [ -z "$macJoyConR" ]; do
    macJoyConR=$(bluetoothctl devices | grep "Joy-Con (R)" | awk '{print $2}')
    sleep 1
done

connectDevice $macJoyConR &
JOYCONR_PID=$!

while [ -z "$macJoyConL" ]; do
    macJoyConL=$(bluetoothctl devices | grep "Joy-Con (L)" | awk '{print $2}')
    sleep 1
done

connectDevice $macJoyConL &
JOYCONL_PID=$!

kill $SCAN_PID

