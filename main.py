# Fluid Dynamic Simulation
import pygame
import sys
from particles import Particle
from non_gravity_objects import Platform
import random


# initialize pygame
pygame.init()

# set screen factor and initialize screen with set width, height
SCREEN_SIZE_FACTOR = 80
WIDTH, HEIGHT = 16*SCREEN_SIZE_FACTOR, 9*SCREEN_SIZE_FACTOR
WIN_CENTER = (WIDTH/2, HEIGHT/2)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


# initialize class dependencies
particles = pygame.sprite.Group()
particles.add(Particle((WIN_CENTER[0], 50), 20, 2, [0, 0]))
particles.add(Particle((WIN_CENTER[0]-200, 50), 20, 2, [5, 0]))

non_gravity_objects = pygame.sprite.Group()
non_gravity_objects.add(Platform([100, WIN_CENTER[1]+100], [WIDTH-200, 10], 10000)) #increasing mass to 1000 makes platform static


#! I am describing the changes in the github commit.


def gameUpdate(surface):
    """
    :return: Update the game, and display objects onto screen
    """
    surface.fill("black")

    #? This is an attempt to solve the issue with ball falling through the platform (the same problem you had in the first prototype)
    #* This creates dictionary and stores position of objects before update function
    positions = {}
    for particle in particles:
        positions[particle] = [particle.rect.x, particle.rect.y]
    for ngo in non_gravity_objects:
        positions[ngo] = [ngo.rect.x, ngo.rect.y]


    particles.update()
    non_gravity_objects.update()
    
    #* Checking for collisions
    #? Maybe move to another script
        #* Collision detection between particles
    #TODO: The particles stack on each other, needs to be fixed
    for p1 in particles:
        for p2 in particles:
            if p1 != p2:
                if pygame.sprite.collide_circle(p1, p2):
                    v1, v2 = p1.velocity[0], p2.velocity[0]
                    m1, m2 = p1.mass, p2.mass

                    p1.velocity[0] = ((v1*(m1-m2) + 2*m2*v2) / (m1 + m2)) * 0.9
                    p2.velocity[0] = ((v2*(m2-m1) + 2*m1*v1) / (m1+m2)) * 0.9


                    v1, v2 = p1.velocity[1], p2.velocity[1]
                    m1, m2 = p1.mass, p2.mass

                    p1.velocity[1] = ((v1*(m1-m2) + 2*m2*v2) / (m1 + m2)) * 0.9
                    p2.velocity[1] = ((v2*(m2-m1) + 2*m1*v1) / (m1+m2)) * 0.9

                    p1.rect.x, p1.rect.y = positions[p1]
                    p2.rect.x, p2.rect.y = positions[p2]
    

        #* Collision detection between particles and non_gravity_objects
    collisions = pygame.sprite.groupcollide(particles, non_gravity_objects, False, False)
    for particle in collisions.keys():
        v1, v2 = particle.velocity[1], collisions[particle][0].velocity[1]
        m1, m2 = particle.mass, collisions[particle][0].mass

        particle.velocity[1] = ((v1*(m1 - m2) + 2*m2*v2) / (m1 + m2)) * 0.9 #multiplying by 0.9 simulates the loss of kinetic energy in real world
        collisions[particle][0].velocity[1] = ((v2*(m2-m1) + 2*m1*v1) / (m1+m2)) * 0.9

        #* This resets position of objects after collision (if you want to know how that works text me)
        particle.rect.x, particle.rect.y = positions[particle]
        collisions[particle][0].rect.x, collisions[particle][0].rect.y = positions[collisions[particle][0]]
    



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
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                particles.add(Particle(mousepos, 20, 2, [random.randint(-3, 3), random.randint(-3, 3)]))




        gameUpdate(WIN)
    pygame.quit()




if __name__ == "__main__":
    main()