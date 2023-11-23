import pygame

#* On these objects, gravity is not applied

class Platform(pygame.sprite.Sprite):
    def __init__(self, position, size, invincible=False, mass=1000, velocity=[0, 0], color="white"):
        super().__init__()

        self.size = size
        self.mass = mass
        self._velocity = velocity
        self.color = color

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

        self.gravity = 0 # added for a feature for future use case

        self.invincible = invincible # added because current platforms do not get affected by gravity nor momentum

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self._velocity[0]
        self.rect.y += self._velocity[1]



    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, new_velocity):
        if not self.invincible:
            self._velocity = new_velocity


