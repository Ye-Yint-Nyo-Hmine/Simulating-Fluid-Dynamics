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
particles.add(Particle((WIN_CENTER[0], 0), 20, 2, [0, 0]))

non_gravity_objects = pygame.sprite.Group()
non_gravity_objects.add(Platform([100, WIN_CENTER[1]+100], [WIDTH-200, 10], 30))




def gameUpdate(surface):
    """
    :return: Update the game, and display objects onto screen
    """
    surface.fill("black")
    particles.update()
    non_gravity_objects.update()
    
    #* Checking for collisions
    #? Maybe move to another script
    
    #* Collision detection between particles and non_gravity_objects
    collisions = pygame.sprite.groupcollide(particles, non_gravity_objects, False, False)

    #? Is the platform supposed to stay rigid or move with gravity as it is falling down when run
    for particle in collisions.keys():
        v1, v2 = particle.velocity[1], collisions[particle][0].velocity[1]
        m1, m2 = particle.mass, collisions[particle][0].mass
        particle.velocity[1] = (v1*(m1 - m2) + 2*m2*v2) / (m1 + m2)
        collisions[particle][0].velocity[1] = (v2*(m2-m1) + 2*m1*v1) / (m1+m2)

        particles.update()
        non_gravity_objects.update()
    

    #* Finally drawing objects onto screen
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