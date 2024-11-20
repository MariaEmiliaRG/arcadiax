import pygame

def main():
    pygame.init()
    pygame.joystick.init()

    # Verificar si hay algún Joy-Con conectado
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("No se detectaron controladores.")
        return

    # Inicializar el primer joystick encontrado (puedes cambiar el índice según sea necesario)
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Controlador conectado: {joystick.get_name()}")

    # Loop principal para capturar eventos
    try:
        print("Mueve el joystick para ver los valores de los ejes...")
        while True:
            pygame.event.pump()  # Procesar eventos
            x_axis = joystick.get_axis(0)  # Eje X del stick izquierdo
            y_axis = joystick.get_axis(1)  # Eje Y del stick izquierdo

            # Imprimir los valores del joystick
            print(f"Joystick Izquierdo - X: {x_axis:.2f}, Y: {y_axis:.2f}")

            pygame.time.wait(100)  # Espera 100ms para evitar saturar el CPU
    except KeyboardInterrupt:
        print("\nSaliendo del programa.")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
