#!/bin/bash
# Reproduce el archivo de audio en el arranque

ffmpeg -i /home/emilia/arcadiax/imgs/twinkle.mp3 -f pulse "default"
