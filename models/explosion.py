import pygame
from engine import Spritesheet

Explosion_Group = pygame.sprite.Group()

Explosion1 = Spritesheet("assets/explosions/explosion.png").parse_sprite(6,0,0,32,32,1)

class Explosion(pygame.sprite.Sprite):
    def __init__(self,x,y,images):
        super().__init__(self)


        self.images = images

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.counter = 0
        self.limit = len(self.images)
        self.explosion_timer = 0
        self.explosion_time = 50

    def update(self):


        if self.explosion_timer >= self.explosion_timer :
            self.counter += 1
            if self.counter >= self.limit :
                self.kill()
            self.explosion_timer = 0
        else :
            self.explosion_timer += 1

        self.image = self.images[self.counter]


