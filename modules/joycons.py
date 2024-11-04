import time
import subprocess
import json
import bluetooth  

class joycons:

    def __init__(self):
        self.pathScriptGetMac = "../scripts/bluetooth-get-mac-joycons.sh"
        self.joyconsMac = {}

    def getMacJoyCons(self):
        result = subprocess.run([self.pathScriptGetMac], capture_output=True, text=True, check=True)
        self.joyconsMac = json.loads(result.stdout)
        
        return

    def connectJoyCons(self):

        self.getMacJoyCons()
        bt = bluetooth.bluetooth()

        for joycon, mac in self.joyconsMac.items(): 
            bt.connectDevice(mac)
        
        bt.close()
        return 

    def disconnectJoyCons(self):
        bt = bluetooth.bluetooth()

        for joycon, mac in self.joyconsMac.items(): 
            bt.disconnectDevice(mac)
            bt.removeDevice(mac)
        
        bt.close()
        return 
