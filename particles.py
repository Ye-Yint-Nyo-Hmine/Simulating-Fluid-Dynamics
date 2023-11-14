import pygame

GRAVITY = 9.81

class Particle(pygame.sprite.Sprite):
    def __init__(self, position, radius, mass=2, velocity=[0, 0], color="blue"):
        super().__init__()

        
        self._radius = radius
        self._mass = mass
        self._color = color

        self._velocity = velocity
        self.collided = False #? Do we need it?

        self.image = pygame.Surface([radius*2, radius*2])
        pygame.draw.circle(self.image, self._color, (radius, radius), self._radius)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def update(self):

        self._velocity[1] += GRAVITY//4

        self.rect.x += self._velocity[0]
        self.rect.y += self._velocity[1]








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