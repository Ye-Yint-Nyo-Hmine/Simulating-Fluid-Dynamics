import math

import pygame


def smoothingCurve(radius, distance):
    volume = (math.pi * (radius**8))/4
    value = max(0, (radius**2) - (distance**2))
    return (value**3)/volume

def calculateDensity(WIN, particles, sample_point, smoothing_radius=5):
    density = 0
    # TODO: Make this function run faster
    # TODO: Redo the calculation to make it correct; as it is not currently
    # TODO: make the following density visual semi transparent
    pygame.draw.circle(WIN, (0, 255, 255),
                       (sample_point), smoothing_radius, width=smoothing_radius-8)

    for particle in particles:
        distance = math.sqrt((particle.center[0]-sample_point[0])**2 + (particle.center[1]-sample_point[1])**2)
        influence = smoothingCurve(smoothing_radius, distance)*1000
        density += (particle.mass * influence)

    return round(density, 4)
