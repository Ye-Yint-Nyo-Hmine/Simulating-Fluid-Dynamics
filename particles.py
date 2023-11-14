import pygame

GRAVITY = 9.81

class Particle(pygame.sprite.Sprite):
    def __init__(self, surface, color, position, radius):
        super().__init__()

        self._surface = surface
        self._color = color
        self._radius = radius
        self._mass = 2
        self._velocity = [0, 0] # magnitude of force with respect to x, y
        self.collided = False

        self.image = pygame.Surface([radius*2, radius*2])
        pygame.draw.circle(self.image, self._color, (radius, radius), self._radius)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def update(self):
        #print(self._force[0], self._force[1])
        self._velocity = [(self._mass * 0), (self._mass * GRAVITY)] #? I change the syntax of this line a little bit so it would be easier to read hope you dont mind.
        # TODO: Fix collision and bouncing
        if self.collided:
            print("colided")
            self._velocity[1] *= -1
            self.collided = False

        self.rect.x += self._velocity[0]
        self.rect.y += self._velocity[1]

        #? Because of the nested conditions, self.collided works only for the top and bottom of the screen
        #? I thing we should change the collision checks, because we need for the particle to be able to push each other
        #? The way I would do it is coding a way for the particle to insert a force on the object it interacts with and give the particle same force in oposite direction
        #?                                                                                                 (And calculate the velocity based on all the forces (including gravity))
        if self.rect.x > 0 and self.rect.x + self._radius*2 < self._surface.get_width():
            if self.rect.y > 0 and self.rect.y + self._radius*2 < self._surface.get_height():
                pass
            else:
                self.collided = True
        #? As I said earlier, the collisions should be a little different. Maybe you though to make collisions for the envirnment separated from the collision between the particles.
        #? I would probably make the collisions together.
        #? For the particle to be able to insert a force and get an oposite force, it could be handy to know from what sides the particles interacted. However that
        #? may be a little bit hard to implement, so I though I would just use pygame's sprite class to better detect collisions and always apply oposite force on the object it interacts with.
        
        #? If you are okay with that, I could start working on it.



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