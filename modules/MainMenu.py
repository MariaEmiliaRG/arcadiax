import pygame
import sys
from ROMSManager import ROMSManager

class MainMenu:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.ancho_pantalla, self.alto_pantalla = pantalla.get_size()
        
        # Cargar fondo
        self.fondo = pygame.image.load("../imgs/arcadiax-boot.png")
        self.fondo = pygame.transform.scale(self.fondo, (self.ancho_pantalla, self.alto_pantalla))

        # Colores y fuentes
        self.COLOR_BOTON = (100, 200, 255)
        self.COLOR_TEXTO = (255, 255, 255)
        self.COLOR_RESALTADO = (255, 100, 100)
        self.fuente = pygame.font.Font(None, 40)

        # Opciones y selección
        self.opciones = ["Jugar", "Controles"]
        self.opcion_seleccionada = 0
        romsManager = ROMSManager()
        self.juegos_disponibles = romsManager.getROMS()
        self.juego_seleccionado = 0  # Índice del juego seleccionado

        # Botones
        self.boton_jugar = pygame.Rect(300, 400, 200, 50)
        self.boton_configuracion = pygame.Rect(300, 500, 200, 50)
        self.botones = [self.boton_jugar, self.boton_configuracion]

        # Inicializar joystick
        pygame.joystick.init()
        if pygame.joystick.get_count() > 0:
            self.gamepad = pygame.joystick.Joystick(0)
            self.gamepad.init()
        else:
            print("No se detectó ningún gamepad conectado.")
            sys.exit()

    def dibujar_texto_centrado(self, texto, rect, color):
        texto_renderizado = self.fuente.render(texto, True, color)
        texto_rect = texto_renderizado.get_rect(center=rect.center)
        self.pantalla.blit(texto_renderizado, texto_rect)

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.JOYBUTTONDOWN:
                if evento.button == 0:  # Botón A para confirmar selección
                    if self.opcion_seleccionada == 0:  # Iniciar el juego seleccionado
                        print(f"Iniciar {self.juegos_disponibles[self.juego_seleccionado]}")
                        return "jugar", self.juegos_disponibles[self.juego_seleccionado]
                    elif self.opcion_seleccionada == 1:  # Abrir configuración
                        print("Abrir Configuración de controles")
                        return "controles", None
            elif evento.type == pygame.JOYHATMOTION:  # D-pad para navegar
                x, y = evento.value
                if y == 1:  # Arriba en el D-pad
                    self.opcion_seleccionada = (self.opcion_seleccionada - 1) % len(self.opciones)
                elif y == -1:  # Abajo en el D-pad
                    self.opcion_seleccionada = (self.opcion_seleccionada + 1) % len(self.opciones)
                elif x == -1 and self.opcion_seleccionada == 0:  # Izquierda en el D-pad
                    # Cambia al juego anterior
                    self.juego_seleccionado = (self.juego_seleccionado - 1) % len(self.juegos_disponibles)
                elif x == 1 and self.opcion_seleccionada == 0:  # Derecha en el D-pad
                    # Cambia al siguiente juego
                    self.juego_seleccionado = (self.juego_seleccionado + 1) % len(self.juegos_disponibles)
        return None, None

    def actualizar_pantalla(self):
        # Dibujar fondo
        self.pantalla.blit(self.fondo, (0, 0))

        # Dibujar el título del juego seleccionado
        texto_juego = f"Juego Seleccionado: {self.juegos_disponibles[self.juego_seleccionado]}"
        texto_renderizado = self.fuente.render(texto_juego, True, self.COLOR_TEXTO)
        self.pantalla.blit(texto_renderizado, (self.ancho_pantalla // 2 - texto_renderizado.get_width() // 2, 200))

        # Dibujar botones de opciones
        for i, boton in enumerate(self.botones):
            color = self.COLOR_RESALTADO if i == self.opcion_seleccionada else self.COLOR_BOTON
            pygame.draw.rect(self.pantalla, color, boton)
            self.dibujar_texto_centrado(self.opciones[i], boton, self.COLOR_TEXTO)

        # Actualizar la pantalla
        pygame.display.flip()

    def mostrar_menu(self):
        # Bucle del menú principal
        while True:
            accion, juego = self.manejar_eventos()
            if accion:  # Salir del menú si se selecciona una opción
                return accion, juego
            self.actualizar_pantalla()

