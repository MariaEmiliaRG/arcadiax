import pygame
import json
import time
import os

class Interface:
    def __init__(self):
        os.environ["SDL_VIDEODRIVER"] = "kmsdrm"
        pygame.init()
        pygame.display.init()
        info = pygame.display.Info()
        self.WIDTH, self.HEIGHT = info.current_w, info.current_h

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.DARK_PURPLE = (53, 40, 79)
        self.LIGHT_PURPLE = (216, 187, 255)
        self.YELLOW = (255, 222, 89)

        self.BUTTON_WIDTH = int(self.WIDTH * 0.75) 
        self.BUTTON_HEIGHT = int(self.HEIGHT * 0.09375)

        self.FONT = pygame.font.Font(None, 50) 
        self.SMALL_FONT = pygame.font.Font(None, 30)

        with open("mainMenuButtons.json", "r", encoding='utf-8') as jsonFile:
            self.mainMenuButtons = json.load(jsonFile)

        with open("controlsMenuButtons.json", "r", encoding='utf-8') as jsonFile:
            self.controlsMenuButtons = json.load(jsonFile)

        self.imgBackground = pygame.image.load("../imgs/arcadiax-background.png")  

        self.imgBackground = pygame.transform.scale(self.imgBackground, (self.WIDTH, self.HEIGHT))

        return

    def getY(self, y):
        return int(y * self.HEIGHT / 800)
    
    def drawRect(self, y, width, height, buttonColor, borderColor=None, borderWidth=0):
        x = (self.WIDTH - width) // 2

        rect = pygame.Rect(x, y, width, height) 
        if borderColor and borderWidth > 0:
            pygame.draw.rect(self.screen, borderColor, rect)  

        innerRect = pygame.Rect(
            x + borderWidth, 
            y + borderWidth, 
            width - 2 * borderWidth, 
            height - 2 * borderWidth
        )
        pygame.draw.rect(self.screen, buttonColor, innerRect)
        
        return innerRect

    def drawTextOnRect(self, text, buttonRect, textColor, font):
        textSurface = font.render(text, True, textColor)  
        textRect = textSurface.get_rect(center=buttonRect.center)  
        self.screen.blit(textSurface, textRect) 

        return 
    
    def drawText(self, text, point, font, color, lineSpacing=5):
        lines = text.splitlines()
        x, y = point
        for line in lines:
            textSurface = font.render(line, True, color)
            self.screen.blit(textSurface, (x, y))
            y += textSurface.get_height() + lineSpacing

        return

    def drawButton(self, button):

        borderColor = [255, 222, 89]  if button["selected"] else button["borderColor"]
        backgroundColor = [255, 222, 89]  if button["selected"] else button["backgroundColor"]
        
        font = self.FONT if button["fontSize"] == "big" else self.SMALL_FONT
        
        rect = self.drawRect(self.getY(button["y"]), self.BUTTON_WIDTH, self.BUTTON_HEIGHT, backgroundColor, borderColor, button["borderWidth"])
        self.drawTextOnRect(button["text"], rect, button["textColor"], font)

        return 
    
    def drawMainMenu(self):

        self.screen.fill(self.DARK_PURPLE) 
        self.screen.blit(self.imgBackground, (0, 0))
        for button in self.mainMenuButtons.values():
            self.drawButton(button)

        pygame.display.flip()
        return
    
    def drawControlsMenuMenu(self):

        self.screen.fill(self.DARK_PURPLE) 
        self.screen.blit(self.imgBackground, (0, 0))
        for button in self.controlsMenuButtons.values():
            self.drawButton(button)

        joyconImg = pygame.image.load("../imgs/joy-con.png") 
        joyconImg = pygame.transform.scale(joyconImg, (self.WIDTH*0.7, self.HEIGHT*0.7))

        imgWidth, imgHeight = joyconImg.get_size()
        x = (self.WIDTH - imgWidth) // 2
        y = (self.HEIGHT - imgHeight) // 2

        self.screen.blit(joyconImg, (x, y+100))

        pygame.display.flip()
        return
    
    def drawBluetoothPairInstructions(self, option):
        self.screen.fill(self.DARK_PURPLE) 
        self.screen.blit(self.imgBackground, (0, 0))
        header = {
            "y": 70,
            "backgroundColor": self.LIGHT_PURPLE,
            "borderColor": self.LIGHT_PURPLE,
            "borderWidth": 10,
            "text": "INSTRUCCIONES DE EMPAREJAMIENTO DE LOS JOY-CON",
            "fontSize": "big",
            "textColor": self.DARK_PURPLE,
            "selected": 1
        }

        #TODO: Mejorar las instrucciones
        instructions = """
        Manten presionado el pequeño botón negro de emparejamiento ubicado al costado del riel de cada Joy-Con
        hasta que las luces comiencen a destellar.

        En cuanto escuches los destellos: 

        - PRESIONA ZL y ZR al mismo tiempo para usarlo como un único control.
        - PRESIONA SL y SR en cada joycon para asignarlos como controles individuales.
        """
        self.drawButton(header)
        self.drawText(instructions, (150,150), self.SMALL_FONT, self.LIGHT_PURPLE)

        imgPath = "../imgs/"
        imgPath += "pair-joycons.png" if option == "pairing" else "joy-con.png"
        joyconImg = pygame.image.load(imgPath) 
        joyconImg= pygame.transform.scale(joyconImg, (self.WIDTH*0.6, self.HEIGHT*0.7))

        imgWidth, imgHeight = joyconImg.get_size()
        x = (self.WIDTH - imgWidth) // 2
        y = (self.HEIGHT - imgHeight) // 2

        self.screen.blit(joyconImg, (x, y+100))


        pygame.display.flip()
        return

    def drawNewGames(self, games): 
        self.screen.fill(self.DARK_PURPLE) 
        self.screen.blit(self.imgBackground, (0, 0))
        header = {
            "y": 70,
            "backgroundColor": self.LIGHT_PURPLE,
            "borderColor": self.LIGHT_PURPLE,
            "borderWidth": 10,
            "text": "NUEVOS JUEGOS",
            "fontSize": "big",
            "textColor": self.DARK_PURPLE,
            "selected": 1
        }

        text = ""

        if len(games) == 0: 
            text = "No se agregaron nuevos juegos :c"
        else: 
            for game in games: 
                text += game + "\n"

        self.drawButton(header)
        self.drawText(text, (150,150), self.SMALL_FONT, self.LIGHT_PURPLE)

        pygame.display.flip()
        return 

    def setConsole(self, console):
        self.mainMenuButtons["consoleOptions"]["text"] = console
        return
    
    def setGame(self, game):
        self.mainMenuButtons["gameOptions"]["text"] = game
        return
    
    def setMenuOption(self, option): 
        for menuOption in self.mainMenuButtons.keys():
            self.mainMenuButtons[menuOption]["selected"] = 0

        menuOptions = list(self.mainMenuButtons.keys())[:4]
        self.mainMenuButtons[menuOptions[option]]["selected"] = 1
        return

    def removeDisplay(self):
        pygame.display.quit()

    def hideDisplay(self):
        os.environ["SDL_VIDEODRIVER"] = "dummy"
        pygame.display.init()

    def showDisplay(self):
#        pygame.quit()
#        os.environ["SDL_VIDEODRIVER"] = "kmsdrm"
#        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
