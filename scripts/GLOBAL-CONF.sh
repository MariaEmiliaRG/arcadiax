#!/bin/bash

sudo apt-get update -y

# -- CONFIGURACIÓN PARA LA REPRODUCCIÓN DE LA IMAGEN ESTÁTICA 

# Creación de un nuevo tema
sudo apt-get install -y  plymouth plymouth-themes
sudo mkdir /usr/share/plymouth/themes/arcadiax
sudo cp ~/arcadiax/plymouth/* /usr/share/plymouth/themes/arcadiax/
sudo plymouth-set-default-theme -R arcadiax
sudo update-initramfs -u

# Quitar los mensajes de arranque
sudo cp ~/arcadiax/conf/cmdline.txt /boot/firmware/

# Quitar pantalla arcoíris 
sudo cp ~/arcadiax/conf/config.txt /boot/firmware/config.txt

# Crear servicio para la reproducción del audio
sudo cp ~/arcadiax/services/play-boot-audio.service
sudo systemctl enable play-boot-audio.service
sudo loginctl enable-linger emilia

# Inicio de sesión automático
sudo cp ~/arcadiax/conf/autologin.conf /etc/systemd/system/getty@tty1.service.d/
sudo systemctl restart getty@tty1
sudo systemctl daemon-reload

# -- CONFIGURACIÓN PARA CONECTAR LOS JOYCONS

sudo apt install -y pi-bluetooth bluetooth bluez dkms cmake libevdev-dev libudev-dev

cd ~
git clone https://github.com/nicman23/dkms-hid-nintendo
cd dkms-hid-nintendo

sudo dkms add .
sudo dkms build nintendo -v 3.2
sudo dkms install nintendo -v 3.2

cd ~
git clone https://github.com/DanielOgorchock/joycond.git
cd joycond
cmake .
sudo make install 
sudo systemctl enable --now joycond

cd ~/arcadiax

# INTALACIÓN DEL EMULADOR 

sudo apt install mednafen

# -- APLICAR TODOS LOS CAMBIOS
sudo reboot