import pygame

GRAVITY = 0 # Temporarily changed gravity to zero for doing density stuff

class Particle(pygame.sprite.Sprite):
    def __init__(self, position, radius, mass=1
                 , velocity=[0, 0], color="blue"):
        super().__init__()

        
        self.radius = radius
        self.mass = mass
        self._color = color

        self._velocity = velocity

        self.image = pygame.Surface([radius*2, radius*2],  pygame.SRCALPHA) #* I made it so that the surface is transpratent
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def colorCoding(self):
        # start = (0, 255, 255) rgb gradient
        # p1 = (0, 255, 0) -3
        # p2 = (255, 255, 0) +1
        # p3 = (255, 0, 0) -2
        # 3 parts to it
        average_vel = (abs(self._velocity[0]) + abs(self._velocity[1]))/2
        max_vel_reached = 12 # max vel reached
        if average_vel <= max_vel_reached/3: # p1
            return (0, 255, 255 - int(255*(3/(max_vel_reached))*average_vel))
        elif max_vel_reached/3 < average_vel <= (max_vel_reached/3)*2: # p2
            return (int(255*(3/(max_vel_reached))*(average_vel/2)), 255, 0)
        elif (max_vel_reached/3)*2 < average_vel < max_vel_reached: # p3
            return (255, 255 - int(255*(3/(max_vel_reached))*(average_vel/3)), 0)
        else:
            return (255, 0, 0)

    def update(self):

    
        self.velocity[1] += GRAVITY//8

        self.rect.x += self._velocity[0]
        self.rect.y += self._velocity[1]
        self._color = self.colorCoding()
        pygame.draw.circle(self.image, self._color, (self.radius, self.radius), self.radius)

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
