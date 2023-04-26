import pygame
import numpy as np
import time


# COLORS:
BG_COLOR = (10, 10, 10)
GRID_COLOR = (40, 40, 40)
DIE_NEXT_COLOR = (170, 170, 170)
ALIVE_NEXT_COLOR = (255, 255, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill(GRID_COLOR)

        if running:
            pygame.display.update()

        time.sleep(.001)

if __name__ == '__main__':
    main()
