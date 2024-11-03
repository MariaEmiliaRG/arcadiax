#!/bin/bash

macJoyConL=""
macJoyConR=""


macJoyConR=$(bluetoothctl devices | grep "Joy-Con (R)" | awk '{print $2}')
bluetoothctl remove $macJoyConR

macJoyConL=$(bluetoothctl devices | grep "Joy-Con (L)" | awk '{print $2}')
bluetoothctl remove $macJoyConL
