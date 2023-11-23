import pygame

def collision(particles, non_gravity_objects):
    positions = {}
    for particle in particles:
        positions[particle] = [particle.rect.x, particle.rect.y]
    for ngo in non_gravity_objects:
        positions[ngo] = [ngo.rect.x, ngo.rect.y]

    # Update all the sprites
    particles.update()
    non_gravity_objects.update()

    # constant variable for Collision Damping
    COLLISION_DAMPING_CONSTANT = 0.65

    #* Collision detection between particles and non_gravity_objects
    collisions = pygame.sprite.groupcollide(particles, non_gravity_objects, False, False)
    for particle in collisions.keys():
        v1, v2 = particle.velocity[1], collisions[particle][0].velocity[1]
        m1, m2 = particle.mass, collisions[particle][0].mass

        if particle.rect.y - particle.radius > collisions[particle][0].rect.y:
            particle.velocity[1] = -((v1*(m1 - m2) + 2*m2*v2) / (m1 + m2)) * COLLISION_DAMPING_CONSTANT
            collisions[particle][0].velocity = [collisions[particle][0].velocity[0], ((v2*(m2-m1) + 2*m1*v1) / (m1+m2)) * COLLISION_DAMPING_CONSTANT]
        else:
            particle.velocity[1] = ((v1 * (m1 - m2) + 2 * m2 * v2) / (m1 + m2)) * COLLISION_DAMPING_CONSTANT
            collisions[particle][0].velocity = [collisions[particle][0].velocity[0], ((v2 * (m2 - m1) + 2 * m1 * v1) / (m1 + m2)) * COLLISION_DAMPING_CONSTANT]
        if particle.rect.x - particle.radius > collisions[particle][0].rect.x:
            v1, v2 = particle.velocity[0], collisions[particle][0].velocity[0]
            particle.velocity[0] = -((v1*(m1 - m2) + 2*m2*v2) / (m1 + m2)) * COLLISION_DAMPING_CONSTANT
            collisions[particle][0].velocity = [((v2*(m2-m1) + 2*m1*v1) / (m1+m2)) * COLLISION_DAMPING_CONSTANT, collisions[particle][0].velocity[1]]
        else:
            v1, v2 = particle.velocity[0], collisions[particle][0].velocity[0]
            particle.velocity[0] = ((v1 * (m1 - m2) + 2 * m2 * v2) / (m1 + m2)) * COLLISION_DAMPING_CONSTANT
            collisions[particle][0].velocity = [((v2 * (m2 - m1) + 2 * m1 * v1) / (m1 + m2)) * COLLISION_DAMPING_CONSTANT,collisions[particle][0].velocity[1]]

        #* This resets position of objects after collision (if you want to know how that works text me)
        particle.rect.x, particle.rect.y = positions[particle]
        collisions[particle][0].rect.x, collisions[particle][0].rect.y = positions[collisions[particle][0]]
    
    return particles, non_gravity_objects