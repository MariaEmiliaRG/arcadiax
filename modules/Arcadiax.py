import Interface
import JoyCons
import ROMSManager
import USBManager
import threading
import time

class Arcadiax: 
    def __init__(self):
        self.interface = Interface.Interface()
        self.joycons = JoyCons.JoyCons()
        self.play = True
        return 
    
    def start(self):
        self.connectJoyCons()

        time.sleep(180)
        self.powerOff()
        return 
    
    def connectJoyCons(self):
        self.joycons.disconnectJoyCons()
        print("hola1")
        connectJoyConsThread = threading.Thread(target=self.joycons.connectJoyCons)
        connectJoyConsThread.start()
        print("hola2")
        while connectJoyConsThread.is_alive():
            self.interface.drawBluetoothPairInstructions("pairing")
            #print("hola3")
        return

    
    def powerOff(self): 
        self.play = False 
        self.joycons.disconnectJoyCons()
        return
