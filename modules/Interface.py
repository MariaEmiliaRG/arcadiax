import pygame
import json

class Interface:
    def __init__(self):
        pygame.init()
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

        with open("mainMenuButtons.json", "r") as json_file:
            self.mainMenuButtons = json.load(json_file)

        #TODO Agregar la verdadera imagen de fondo
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

    def drawButton(self, button):
        borderColor = [255, 222, 89]  if button["selected"] else button["borderColor"]
        backgroundColor = [255, 222, 89]  if button["selected"] else button["backgroundColor"]
        
        font = self.FONT if button["fontSize"] == "big" else self.SMALL_FONT
        
        rect = self.drawRect(self.getY(button["y"]), self.BUTTON_WIDTH, self.BUTTON_HEIGHT, backgroundColor, borderColor, button["borderWidth"])
        self.drawTextOnRect(button["text"], rect, button["textColor"], font)

        return 
    
    def drawMainMenuButtons(self):

        self.screen.fill(self.DARK_PURPLE) 
        self.screen.blit(self.imgBackground, (0, 0))
        for button in self.mainMenuButtons.values():
            self.drawButton(button)

        pygame.display.flip()
        return
    
    def drawMainMenuTest(self):
        running = True
        while running:
            self.drawMainMenuButtons()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
