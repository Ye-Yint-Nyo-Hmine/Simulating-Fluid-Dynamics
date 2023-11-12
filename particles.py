import pygame


class Particle():
    def __init__(self, surface, color, center_x, center_y, radius):
        self._surface = surface
        self._color = color
        self._position = [center_x, center_y]
        self._radius = radius
        self.gravity = 9.81
        self._mass = 2
        self._force = [0, 0] # magnitude of force with respect to x, y
        self.collided = False

    def draw(self):
        pygame.draw.circle(self._surface, self._color, self._position, self._radius)

    def update(self):
        print(self._force[0], self._force[1])
        self._force[0], self._force[1] = self._mass * 0, self._mass * self.gravity
        # TODO: Fix collision and bouncing
        if self.collided:
            self._force[1] *= -1
            self.collided = False

        self._position[0] += self._force[0]
        self._position[1] += self._force[1]

        if self._position[0] - self._radius > 0 and self._position[0] + self._radius < self._surface.get_width():
            if self._position[1] - self._radius > 0 and self._position[1] + self._radius < self._surface.get_height():
                pass
            else:
                self.collided = True



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
    def force(self):
        return  self._force

    @force.setter
    def force(self, new_force):
        self._force = new_force