#!/bin/bash
# Author: Maria Emilia Ramirez Gomez
# Year: 2024
# License: MIT License
#
# This code is released under the MIT License. See the LICENSE file for more details.
# Reproduce el archivo de audio en el arranque

ffmpeg -i /home/emilia/arcadiax/imgs/twinkle.mp3 -f pulse "default"
