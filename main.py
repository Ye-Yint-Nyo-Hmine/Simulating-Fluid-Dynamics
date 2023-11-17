# Fluid Dynamic Simulation
import pygame
import sys
import random
from particles import Particle
from objects import Platform

# initialize pygame
pygame.init()

# set screen factor and initialize screen with set width, height
SCREEN_SIZE_FACTOR = 80
WIDTH, HEIGHT = 16*SCREEN_SIZE_FACTOR, 9*SCREEN_SIZE_FACTOR
WIN_CENTER = (WIDTH/2, HEIGHT/2)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# initialize class dependencies

# Created Sprite Group to contain platforms in
non_gravity_objects = pygame.sprite.Group()

# Created Sprite Group to contain particles in
particles = pygame.sprite.Group()

# create standard properties for particles
PARTICLE_MASS = 2
PARTICLE_RADIUS = 10


# Create objects on surface with a boundary of width and height
non_gravity_objects.add(Platform([0, HEIGHT-10], [WIDTH, 10], invincible=True))
non_gravity_objects.add(Platform([0, 0], [WIDTH, 10], invincible=True))
non_gravity_objects.add(Platform([0, 0], [10, HEIGHT], invincible=True))
non_gravity_objects.add(Platform([WIDTH-10, 0], [10, HEIGHT], invincible=True))

particles.add(Particle((WIN_CENTER[0], 50), PARTICLE_RADIUS, PARTICLE_MASS, [0, 0]))
particles.add(Particle((WIN_CENTER[0]-200, 50), PARTICLE_RADIUS, PARTICLE_MASS, [5, 0]))



def gameUpdate(surface):
    """
    :return: Update the game, and display objects onto screen
    """
    # recolor the surface every frame
    surface.fill("black")

    #? This is an attempt to solve the issue with ball falling through the platform (the same problem you had in the first prototype)
    #* This creates dictionary and stores position of objects before update function

    #* We should make this run faster and more efficiently
    # TODO: Make it compute more efficiently
    positions = {}
    for particle in particles:
        positions[particle] = [particle.rect.x, particle.rect.y]
    for ngo in non_gravity_objects:
        positions[ngo] = [ngo.rect.x, ngo.rect.y]

    # Update all the sprites
    particles.update()
    non_gravity_objects.update()

    # constant variable for Collision Damping
    COLLISION_DAMPING_CONSTANT = 0.5

    #* Collision detection between particles and non_gravity_objects
    collisions = pygame.sprite.groupcollide(particles, non_gravity_objects, False, False)
    for particle in collisions.keys():
        v1, v2 = particle.velocity[1], collisions[particle][0].velocity[1]
        m1, m2 = particle.mass, collisions[particle][0].mass

        particle.velocity[1] = ((v1*(m1 - m2) + 2*m2*v2) / (m1 + m2)) * COLLISION_DAMPING_CONSTANT
        collisions[particle][0].velocity = [collisions[particle][0].velocity[0], ((v2*(m2-m1) + 2*m1*v1) / (m1+m2)) * COLLISION_DAMPING_CONSTANT]

        #* This resets position of objects after collision (if you want to know how that works text me)
        particle.rect.x, particle.rect.y = positions[particle]
        collisions[particle][0].rect.x, collisions[particle][0].rect.y = positions[collisions[particle][0]]

    #* Finally drawing objects onto screen
    particles.draw(WIN)
    non_gravity_objects.draw(WIN)

    # Update pygame display
    pygame.display.update()

def getKeyPresses(surface):
    # Get inputs from keyboard and neat up the code
    keys = pygame.key.get_pressed()

    if keys[pygame.K_r]:  # reset and clear the screen when r is pressed
        reset(surface)

    if keys[pygame.K_n]:
        print(len(particles))

    if keys[pygame.K_g]:
        generate_group_particles(surface)

    if not keys[pygame.K_s]:  # * freezes frame when key s is being pressed
        gameUpdate(surface)

def reset(surface):
    """
    :return: reset the program by clearing the screen
    """
    # removing particles from the screen
    for particle in particles:
        particles.remove(particle)


def generate_group_particles(surface, num_x=37, num_y=10, pos=(100, 50)):
    """
    :param surface: Game surface to create particles on
    :param num_x: the number of particles on each row
    :param num_y: the number of rows
    :return:
    """
    # for each particle in set num x and num y, create particles
    for rows in range(num_y):
        for column in range(num_x):
            particles.add(Particle((pos[0] + column*30, pos[1]+rows*40), 10, 2, [random.randrange(-10, 10), random.randrange(-10, 10)]))



def main():
    """
    :return: run the main program
    """
    # game run variable is set
    run = True

    # Set standard FPS to 60 for running the program
    FPS = 60
    clock = pygame.time.Clock()

    generate_group_particles(WIN)

    # main game loop
    while run:
        for event in pygame.event.get():
            # quit pygame
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # get mouse inputs
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                particles.add(Particle(mouse_pos, PARTICLE_RADIUS, PARTICLE_MASS, [random.randrange(-10, 10), random.randrange(-10, 10)]))


        # function for all the key presses to clean up the code
        getKeyPresses(WIN)

        # tick at every FPS
        clock.tick(FPS)

    # quit pygame when the program completes
    pygame.quit()




if __name__ == "__main__":
    # run the main function
    main()