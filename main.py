# Fluid Dynamic Simulation

import pygame
import sys


pygame.init()

SCREEN_SIZE_FACTOR = 80
WIDHT, HEIGHT = 16*SCREEN_SIZE_FACTOR, 9*SCREEN_SIZE_FACTOR
WIN = pygame.display.set_mode((WIDHT, HEIGHT))



def main():

    run = True
    FPS = 60
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    pygame.quit()




if __name__ == "__main__":
    main()