import Interface
import JoyCons
import ROMSManager
import USBManager
import threading
import time
import pygame

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
        pygame.init()
        return 
    
    def start(self):
        self.connectJoyCons()

        while self.play:

            for event in pygame.event.get():
                if event.type == pygame.JOYHATMOTION:
                    value = event.value  
                    self.changeMainMenuOptions(value)
                    self.updateMainMenu()

                elif event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0: # B Button
                        self.selectMainMenuOptions()

            if not self.options["play"]:
                self.interface.drawMainMenu()
                
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
        time.sleep(30)

        self.joycons.initJoyCon1()
        
    def changeMainMenuOptions(self, valueJoystick):
        if valueJoystick == (0, 1): #UP
            self.mainMenuOptions["menu"] -= 1
            if self.mainMenuOptions["menu"] < 0:
                self.mainMenuOptions["menu"] = 3
        
        elif valueJoystick == (0, -1): #DOWN
            self.mainMenuOptions["menu"] += 1
            if self.mainMenuOptions["menu"] > 3:
                self.mainMenuOptions["menu"] = 0

        elif valueJoystick == (-1, 0): #LEFT
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
        
        elif valueJoystick == (1, 0): #RIGHT
            if self.mainMenuOptions["menu"] == 0:
                self.mainMenuOptions["console"] += 1
                if self.mainMenuOptions["console"] > len(self.roms) - 1:
                    self.mainMenuOptions["console"] = 0
                self.mainMenuOptions["game"] = 0
            
            elif self.mainMenuOptions["menu"] == 1:
                self.mainMenuOptions["game"] += 1
                if self.mainMenuOptions["game"] > len(self.roms[console]) - 1:
                    self.mainMenuOptions["game"] = 0
    
    def updateMainMenu(self):
        self.interface.setMenuOption(self.mainMenuOptions["menu"])
        console = list(self.roms.keys())
        console = console[self.mainMenuOptions["console"]]
        self.interface.setConsole(console)
        self.interface.setGame(self.roms[console][self.changeMainMenuOptions["game"]])
        return
    
    def selectMainMenuOptions(self):
        if self.mainMenuOptions["menu"] == 2: #PLAY
            print("ejecutar el emulador")
        elif self.mainMenuOptions["menu"] == 3: #CONTROLS
            print("modificando el ajsute de los controles")
            self.play = False
        return 
     
    def powerOff(self): 
        self.play = False 
        self.joycons.disconnectJoyCons()
        return
