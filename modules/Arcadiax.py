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
        
        connectJoyConsThread = threading.Thread(target=self.joycons.connectJoyCons())
        connectJoyConsThread.start()
        
        while connectJoyConsThread.is_alive():
            self.interface.drawBluetoothPairInstructions(option = "pairing")

        return

    
    def powerOff(self): 
        self.play = False 
        self.joycons.disconnectJoyCons()
        return
