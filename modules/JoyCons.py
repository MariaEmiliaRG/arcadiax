# Author: Maria Emilia Ramirez Gomez
# Year: 2024
# License: MIT License
#
# This code is released under the MIT License. See the LICENSE file for more details.

import subprocess
import json
import Bluetooth  
import pygame
import threading
import time

class JoyCons:

    def __init__(self):
        self.pathScriptGetMac = "../scripts/bluetooth-get-mac-joycons.sh"
        self.joyconsMac = {}
        self.joystick =  None
        self.joyconsNames = ["Nintendo Switch Combined Joy-Cons","Nintendo Switch Right Joy-Con","Nintendo Switch Left Joy-Con"]
        self.joycon1 = None
        pygame.init()

    def getMacJoyCons(self):
        result = subprocess.run([self.pathScriptGetMac], capture_output=True, text=True, check=True)
        self.joyconsMac = json.loads(result.stdout)

        #print(self.joyconsMac)

        return

    def connectJoyCons(self):
        self.getMacJoyCons()
        bt = Bluetooth.Bluetooth()

        pygame.mixer.init()
        pygame.mixer.music.load('../imgs/twinkle.mp3')

#        rJoyConThread = threading.Thread(target=bt.connectDevice, args=(self.joyconsMac["macJoyConR"],))
#        lJoyConThread = threading.Thread(target=bt.connectDevice, args=(self.joyconsMac["macJoyConL"],))

#        rJoyConThread.start()
#        lJoyConThread.start()

#        rJoyConThread.join()
#        lJoyConThread.join()

        for _, mac in self.joyconsMac.items(): 
            bt.connectDevice(mac)
        
        pygame.mixer.music.play()
        return 

    def disconnectJoyCons(self):
        # we remove the macs since every right and left joycon have the same name
        # it's eassier identifying them by the first time instead of trying connection with every single mac address 
        self.getMacJoyCons()


        bt = Bluetooth.Bluetooth()

        for _ , mac in self.joyconsMac.items(): 
            bt.disconnectDevice(mac)
            bt.removeDevice(mac)
        
        return 
    
    def changeMap(self, numJoyCons):
        #TODO modificar archivos de configuración con el mapeo de los controles
        pass

    def countJoyCons(self):
        total = self.joystick.get_count() 
        self.changeMap(total)
        
        return total   

    def initJoyCon1(self):
        num = 0

        while pygame.joystick.get_count() <= 0 and num < 10:
            self.joystick = pygame.joystick.init()
            print(pygame.joystick.get_count())
            time.sleep(5)
            num += 1
        self.joycon1 = pygame.joystick.Joystick(0)
        self.joycon1.init()

        return

    
