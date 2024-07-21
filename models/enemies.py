import random
import pygame



enemy_group = pygame.sprite.Group()
missile_group = pygame.sprite.Group()

class Missile(pygame.sprite.Sprite) :
    def __init__(self,x,y,image,speed,forward=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


        if forward :
            self.speed = -speed
        else :
            self.speed = speed

    def update(self):
        self.rect.y += self.speed

        if self.rect.y < -50 :
            self.kill()

        if self.rect.y > 600 :
            self.kill()
class EnemySpaceship(pygame.sprite.Sprite):
    def __init__(self,x,y,image,speed,scale,health):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale_by(image,scale)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.speed = speed
        self.health = health

        self.counter = 0
        self.speed_counter = 50

        self.missile_img = pygame.transform.flip(pygame.image.load("assets/bullets/missile00.png"),False,True)

        self.firerate = random.randint(150,200)
        self.firerate_couter = 0


    def update(self):

        if self.counter > self.speed_counter :
            self.rect.y += self.speed
            self.counter = 0
        else :
            self.counter += 1


        if self.firerate_couter > self.firerate :
            missile_group.add(Missile(self.rect.center[0], self.rect.center[1],self.missile_img,3))
            self.firerate_couter = 0
        else :
            self.firerate_couter += 1


        if self.health <= 0 :

            self.kill()







