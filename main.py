# Fluid Dynamic Simulation
import pygame
import sys
from particles import Particle


# initialize pygame
pygame.init()

# set screen factor and initialize screen with set width, height
SCREEN_SIZE_FACTOR = 80
WIDHT, HEIGHT = 16*SCREEN_SIZE_FACTOR, 9*SCREEN_SIZE_FACTOR
WIN_CENTER = (WIDHT/2, HEIGHT/2)
WIN = pygame.display.set_mode((WIDHT, HEIGHT))


# initialize class dependencies
particles = pygame.sprite.Group()
particles.add(Particle(WIN, (100, 200, 255), [WIN_CENTER[0], WIN_CENTER[1]], 20))


def gameUpdate(surface):
    """
    :return: Update the game, and display objects onto screen
    """
    surface.fill("black")
    particles.update()
    particles.draw(WIN)

    pygame.display.update()


def main():
    """
    :return: run the main program
    """
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



        gameUpdate(WIN)
    pygame.quit()




if __name__ == "__main__":
    main()