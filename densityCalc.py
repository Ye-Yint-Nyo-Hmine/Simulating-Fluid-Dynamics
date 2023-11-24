import math

import pygame


def smoothingCurve(radius, distance):
    volume = (math.pi * (radius**8))/4
    value = max(0, (radius**2) - (distance**2))
    return value**3

def calculateDensity(WIN, particles, sample_point, smoothing_radius=5):
    density = 0
    pygame.draw.circle(WIN, (0, 255, 255),
                       (sample_point), smoothing_radius, width=5)

    for particle in particles:
        distance = math.sqrt((particle.center[0]-sample_point[0])**2 + (particle.center[1]-sample_point[1])**2)
        influence = smoothingCurve(smoothing_radius, distance)/10**9
        density += (particle.mass * influence)

    return round(density, 4)
