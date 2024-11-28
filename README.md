# ✨ Arcadiax 
## Autora: María Emilia Ramírez Gómez
Proyecto Final Sistemas Embebidos

Arcadiax es un proyecto diseñado para transformar una Raspberry Pi 4 en una consola de videojuegos retro, emulando juegos de NES, SNES y Game Boy Advance. El sistema incluye una interfaz gráfica (GUI) desarrollada en Python, diseñada para ser controlada mediante los controles Joy-Con de Nintendo.

## 🌙 Características
- **Videojuegos Retro**: Emula juegos de NES, SNES y Game Boy Advance en tu Raspberry Pi 4.
- **Soporte para Joy-Con de Nintendo**: Usa los controles Joy-Con de Nintendo para navegar y jugar.
- **Interfaz Gráfica en Python**: Una interfaz gráfica simple pero efectiva para gestionar tus juegos.
- **Arquitectura Modular**: El sistema está dividido en módulos para facilitar el mantenimiento y desarrollo.

## 🌙 Requisitos 
- Una Raspberry Pi 4 con 4 GB de RAM
- Un par de controles Joy-Con (es posible utilizar otro gamepad, pero será necesario realizar ajustes en el código)
- El módulo de kernel [dkms-hid-nintendo](https://github.com/nicman23/dkms-hid-nintendo)
- El servicio [joycond](https://github.com/DanielOgorchock/joycond)
- El emulador [mednafen](https://mednafen.github.io/)

## 🌙 Instalación 
```
git clone https://github.com/MariaEmiliaRG/arcadiax.git
sudo apt install python3-pygame python3-pexpect python3-uinput python3-pyudev
cd arcadiax/modules
python3 main.py
```

  
