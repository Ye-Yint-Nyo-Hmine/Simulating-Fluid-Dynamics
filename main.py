# Fluid Dynamic Simulation
import pygame
import sys
from particles import Particle
from non_gravity_objects import Platform


# initialize pygame
pygame.init()

# set screen factor and initialize screen with set width, height
SCREEN_SIZE_FACTOR = 80
WIDTH, HEIGHT = 16*SCREEN_SIZE_FACTOR, 9*SCREEN_SIZE_FACTOR
WIN_CENTER = (WIDTH/2, HEIGHT/2)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


# initialize class dependencies
particles = pygame.sprite.Group()
particles.add(Particle(WIN_CENTER, 20))

non_gravity_objects = pygame.sprite.Group()
non_gravity_objects.add(Platform([100, HEIGHT-40], [WIDTH-200, 10]))




def gameUpdate(surface):
    """
    :return: Update the game, and display objects onto screen
    """
    surface.fill("black")
    particles.update()
    
    #* Checking for collisions
    #? Maybe move to another script
    # TODO: add the collision detection


    particles.draw(WIN)
    non_gravity_objects.draw(WIN)

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