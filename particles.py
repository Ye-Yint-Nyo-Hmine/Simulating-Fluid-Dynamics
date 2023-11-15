import pygame

GRAVITY = 9.81

class Particle(pygame.sprite.Sprite):
    def __init__(self, position, radius, mass=1
                 , velocity=[0, 0], color="blue"):
        super().__init__()

        
        self.radius = radius
        self.mass = mass
        self._color = color

        self._velocity = velocity

        self.image = pygame.Surface([radius*2, radius*2])
        pygame.draw.circle(self.image, self._color, (radius, radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def update(self):
    
        self.velocity[1] += GRAVITY//8

        self.rect.x += self._velocity[0]
        self.rect.y += self._velocity[1]

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
    def velocity(self, new_velocity):
        self._velocity = new_velocity
