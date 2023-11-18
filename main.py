# Fluid Dynamic Simulation
import pygame
import sys
import random
from objects.particles import Particle
from objects.other_objects import Platform
from objects.updates import updates
# initialize pygame
pygame.init()

# set screen factor and initialize screen with set width, height
SCREEN_SIZE_FACTOR = 80
WIDTH, HEIGHT = 16*SCREEN_SIZE_FACTOR, 9*SCREEN_SIZE_FACTOR
WIN_CENTER = (WIDTH/2, HEIGHT/2)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# initialize class dependencies

# Created Sprite Group to contain platforms in
other_objects = pygame.sprite.Group()

# Created Sprite Group to contain particles in
particles = pygame.sprite.Group()

# create standard properties for particles
PARTICLE_MASS = 2
PARTICLE_RADIUS = 10


# Create objects on surface with a boundary of width and height
other_objects.add(Platform([0, HEIGHT-10], [WIDTH, 10], invincible=True))
other_objects.add(Platform([0, 0], [WIDTH, 10], invincible=True))
other_objects.add(Platform([0, 0], [10, HEIGHT], invincible=True))
other_objects.add(Platform([WIDTH-10, 0], [10, HEIGHT], invincible=True))



def gameUpdate(surface):
    """
    :return: Update the game, and display objects onto screen
    """

    global particles
    global other_objects

    # *Recolor the surface every frame
    surface.fill("black")

    #* Updates the objects
    particles, other_objects, = updates(particles, other_objects)

    #* Finally drawing objects onto screen
    particles.draw(WIN)
    other_objects.draw(WIN)

    # Update pygame display
    pygame.display.update()



def reset(surface):
    """
    :return: reset the program by clearing the screen
    """
    #* removing particles from the screen
    for particle in particles:
        particles.remove(particle)



def generate_group_particles(surface, num_x=37, num_y=10, pos=(100, 50)):
    """
    :param surface: Game surface to create particles on
    :param num_x: the number of particles on each row
    :param num_y: the number of rows
    :return:
    """
    #* for each particle in set num x and num y, create particles
    for rows in range(num_y):
        for column in range(num_x):
            particles.add(Particle((pos[0] + column*30, pos[1]+rows*40), 10, 2, [random.randrange(-10, 10), random.randrange(-10, 10)]))




def getKeyPresses(surface):
    #* Get inputs from keyboard and run some functions
    keys = pygame.key.get_pressed()

    if keys[pygame.K_r]:  #* reset and clear the screen when r is pressed
        reset(surface)

    if keys[pygame.K_n]:
        print(len(particles)) #* displays number of particles on screen

    if keys[pygame.K_g]:
        generate_group_particles(surface) #* generates particles

    if not keys[pygame.K_s]:  # * freezes frame when key s is being pressed
        gameUpdate(surface)



def main():
    """
    :return: run the main program
    """
    # *game run variable is set
    run = True

    # *Set standard FPS to 60 for running the program
    FPS = 60
    clock = pygame.time.Clock()
    highest_fps = 0

    generate_group_particles(WIN)

    #* Main game loop
    while run:
        for event in pygame.event.get():
            # *quit pygame
            if event.type == pygame.QUIT:
                print(highest_fps)
                pygame.quit()
                sys.exit()
            # *get mouse inputs
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                particles.add(Particle(mouse_pos, PARTICLE_RADIUS, PARTICLE_MASS, [random.randrange(-10, 10), random.randrange(-10, 10)]))


        #* function for all the key presses (also updates the screen)
        getKeyPresses(WIN)

        fps = clock.get_fps()
        if fps > highest_fps:
            highest_fps = fps

        # tick at every FPS
        clock.tick(FPS)

    # quit pygame when the program completes
    pygame.quit()




if __name__ == "__main__":
    # run the main function
    main()