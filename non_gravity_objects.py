import pygame

#* On these objects, gravity is not applied

class Platform(pygame.sprite.Sprite):
    def __init__(self, position, size, mass=1000, velocity=[0, 0], color="white"):
        super().__init__()

        self.size = size
        self.mass = mass
        self.velocity = velocity
        self.color = color

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def update(self):
        #print(self.velocity[1])
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


