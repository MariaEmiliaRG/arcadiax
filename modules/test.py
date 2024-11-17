import pygame

pygame.init()

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h

print(WIDTH, HEIGHT)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colores
DARK_PURPLE = (36, 16, 57)
LIGHT_PURPLE = (152, 115, 172)
YELLOW = (255, 222, 89)

BUTTON_WIDTH = int(WIDTH * 0.75) 
BUTTON_HEIGHT = int(HEIGHT * 0.09375)

def getY(y):
    return int(y * HEIGHT / 800)

FONT = pygame.font.Font(None, 50) 
SMALL_FONT = pygame.font.Font(None, 20)

def drawButton(y, width, height, button_color, border_color=None, border_width=0):
    x = (WIDTH - width) // 2

    rect = pygame.Rect(x, y, width, height) 
    if border_color and border_width > 0:
        pygame.draw.rect(screen, border_color, rect)  

    inner_rect = pygame.Rect(
        x + border_width, 
        y + border_width, 
        width - 2 * border_width, 
        height - 2 * border_width
    )
    pygame.draw.rect(screen, button_color, inner_rect)
    
    return inner_rect

def drawTextOnButton(text, button_rect, text_color, font):
    text_surface = font.render(text, True, text_color)  
    text_rect = text_surface.get_rect(center=button_rect.center)  
    screen.blit(text_surface, text_rect)  

running = True
while running:
    screen.fill(DARK_PURPLE) 
    
    button = drawButton(getY(70), BUTTON_WIDTH, BUTTON_HEIGHT, LIGHT_PURPLE)
    drawTextOnButton("CONSOLA", button, DARK_PURPLE, FONT)
    button = drawButton(getY(145), BUTTON_WIDTH, BUTTON_HEIGHT, DARK_PURPLE, LIGHT_PURPLE, 10)
    drawTextOnButton("consola", button, LIGHT_PURPLE, SMALL_FONT)
    button = drawButton(getY(290), BUTTON_WIDTH, BUTTON_HEIGHT, LIGHT_PURPLE)
    drawTextOnButton("VIDEOJUEGO", button, DARK_PURPLE, FONT)
    button = drawButton(getY(365), BUTTON_WIDTH, BUTTON_HEIGHT, DARK_PURPLE, LIGHT_PURPLE, 10)
    drawTextOnButton("videojuego", button, LIGHT_PURPLE, SMALL_FONT)
    button = drawButton(getY(510), BUTTON_WIDTH, BUTTON_HEIGHT, LIGHT_PURPLE)
    drawTextOnButton("JUGAR", button, DARK_PURPLE, FONT)
    button = drawButton(getY(655), BUTTON_WIDTH, BUTTON_HEIGHT, DARK_PURPLE, LIGHT_PURPLE, 10)
    drawTextOnButton("CONTROLES", button, LIGHT_PURPLE, FONT)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
