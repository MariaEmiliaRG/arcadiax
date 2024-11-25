import Interface
import JoyCons
import ROMSManager
import USBManager
import threading
import time
import pygame
import subprocess
import os 
import signal
import uinput

class Arcadiax: 
    def __init__(self):
        self.interface = Interface.Interface()
        self.joycons = JoyCons.JoyCons()
        self.play = True
        self.mainMenuOptions = { 
            "menu" : 0,
            "console" : 0,
            "game" : 0,
            "play" : 0, 
        }
        self.roms = ROMSManager.ROMSManager().getROMSGroupByConsole()
        self.mednafen = None

        pygame.init()
        return 
    
    def start(self):
#        self.connectJoyCons()

        self.joycons.initJoyCon1()
        while self.play:

            pygame.event.pump()

            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    print(event.button)

            if self.mainMenuOptions["play"]:
                if self.joycons.joycon1.get_button(11): # A Button
                    os.killpg(os.getpgid(self.mednafen.pid), signal.SIGTERM)
                    self.mainMenuOptions["play"] = 0
                    self.interface.removeDisplay()
                    self.interface.showDisplay()

                if self.joycons.joycon1.get_button(4):
                    print("hola hola")
                    events = [uinput.KEY_LEFTALT, uinput.KEY_LEFTSHIFT, uinput.KEY_1] 
                    with uinput.Device(events) as device:
                        time.sleep(1)
                        device.emit_combo([uinput.KEY_LEFTALT, uinput.KEY_LEFTSHIFT, uinput.KEY_1])

            if not self.mainMenuOptions["play"]:
                joystickX = self.joycons.joycon1.get_axis(0)
                joystickY = self.joycons.joycon1.get_axis(1)
                self.changeMainMenuOptions(joystickX, joystickY)
                self.updateMainMenu()

                self.interface.drawMainMenu()

                if self.joycons.joycon1.get_button(1): # A Button
                    self.selectMainMenuOptions()

            pygame.time.wait(100)
        self.powerOff()
        return 
    
    def connectJoyCons(self):
        self.joycons.disconnectJoyCons()
        
        connectJoyConsThread = threading.Thread(target=self.joycons.connectJoyCons)
        connectJoyConsThread.start()
        
        while connectJoyConsThread.is_alive():
            self.interface.drawBluetoothPairInstructions("pairing")
            time.sleep(10)
            self.interface.drawBluetoothPairInstructions("connect")
            time.sleep(10)

        self.interface.drawBluetoothPairInstructions("connect")
        time.sleep(10)

        self.joycons.initJoyCon1()
        
    def changeMainMenuOptions(self, joystickX, joystickY):
        if joystickY < -0.2: #UP
            self.mainMenuOptions["menu"] -= 1
            if self.mainMenuOptions["menu"] < 0:
                self.mainMenuOptions["menu"] = 3
        
        elif joystickY > 0.2: #DOWN
            self.mainMenuOptions["menu"] += 1
            if self.mainMenuOptions["menu"] > 3:
                self.mainMenuOptions["menu"] = 0

        elif joystickX < -0.2: #LEFT
            if self.mainMenuOptions["menu"] == 0:
                self.mainMenuOptions["console"] -= 1
                if self.mainMenuOptions["console"] < 0:
                    self.mainMenuOptions["console"] = len(self.roms) - 1
                self.mainMenuOptions["game"] = 0
            
            elif self.mainMenuOptions["menu"] == 1:
                self.mainMenuOptions["game"] -= 1
                if self.mainMenuOptions["game"] < 0:
                    console = list(self.roms.keys())
                    console = console[self.mainMenuOptions["console"]]
                    self.mainMenuOptions["game"] = len(self.roms[console]) - 1
        
        elif joystickX > 0.2: #RIGHT
            if self.mainMenuOptions["menu"] == 0:
                self.mainMenuOptions["console"] += 1
                if self.mainMenuOptions["console"] > len(self.roms) - 1:
                    self.mainMenuOptions["console"] = 0
                self.mainMenuOptions["game"] = 0
            
            elif self.mainMenuOptions["menu"] == 1:
                self.mainMenuOptions["game"] += 1
                console = list(self.roms.keys())
                console = console[self.mainMenuOptions["console"]]
                if self.mainMenuOptions["game"] > len(self.roms[console]) - 1:
                    self.mainMenuOptions["game"] = 0
    
    def updateMainMenu(self):
        self.interface.setMenuOption(self.mainMenuOptions["menu"])
        console = list(self.roms.keys())
        console = console[self.mainMenuOptions["console"]]
        self.interface.setConsole(console)
        self.interface.setGame(self.roms[console][self.mainMenuOptions["game"]])
        return
    
    def selectMainMenuOptions(self):
        if self.mainMenuOptions["menu"] == 2: #PLAY
            print("ejecutar el emulador")
            self.interface.removeDisplay()
            self.mainMenuOptions["play"] = 1
            console = list(self.roms.keys())
            console = console[self.mainMenuOptions["console"]]
            game = self.roms[console][self.mainMenuOptions["game"]]
            self.mednafen = subprocess.Popen(["mednafen", "../roms/"+game], preexec_fn=os.setsid)
            print("holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") 
            self.interface.hideDisplay()
        elif self.mainMenuOptions["menu"] == 3: #CONTROLS
            print("modificando el ajsute de los controles")
            self.play = False
        return 
     
    def powerOff(self): 
        self.play = False 
        self.joycons.disconnectJoyCons()
        return
