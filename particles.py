import pygame


class Particle():
    def __init__(self, surface, color, center_x, center_y, radius):
        self._surface = surface
        self._color = color
        self._position = [center_x, center_y]
        self._radius = radius
        self.gravity = 9.81/20
        self._velocity = [0, 0] # magnitude of velocity

    def draw(self):
        pygame.draw.circle(self._surface, self._color, self._position, self._radius)

    def update(self):
        self._velocity[1] += self.gravity # apply gravity to the velocity of the particle
        self._position[0] += self._velocity[0] # enforce velocity on x
        self._position[1] += self._velocity[1] # enforce velocity on y

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_pos: list):
        self._position = new_pos

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, new_vel: list):
        self._velocity = new_vel
