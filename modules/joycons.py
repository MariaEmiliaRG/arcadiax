import subprocess
import json
import bluetooth  
import pygame

class joycons:

    def __init__(self):
        self.pathScriptGetMac = "../scripts/bluetooth-get-mac-joycons.sh"
        self.joyconsMac = {}
        self.joystick = pygame.joystick.init()
        self.joycon0 = None

    def getMacJoyCons(self):
        result = subprocess.run([self.pathScriptGetMac], capture_output=True, text=True, check=True)
        self.joyconsMac = json.loads(result.stdout)
        return

    def connectJoyCons(self):
        self.getMacJoyCons()
        bt = bluetooth.bluetooth()

        pygame.mixer.init()
        pygame.mixer.music.load('twinkle.mp3')

        for _, mac in self.joyconsMac.items(): 
            bt.connectDevice(mac)
        
        bt.close()
        pygame.mixer.music.play()
        return 

    def disconnectJoyCons(self):
        # we remove the macs since every right and left joycon have the same name
        # it's eassier identifying them by the first time instead of trying connection with every single mac address 
        bt = bluetooth.bluetooth()

        for _ , mac in self.joyconsMac.items(): 
            bt.disconnectDevice(mac)
            bt.removeDevice(mac)
        
        bt.close()
        return 
    
    def changeMap(self, numJoyCons):
        #TODO modificar archivos de configuración con el mapeo de los controles
        pass

    def countJoyCons(self):
        total = self.joystick.get_count() 
        self.changeMap(total)
        return        

    