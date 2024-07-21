import pygame
from models.enemies import enemy_group
bullet_group = pygame.sprite.Group()


class Bullet(pygame.sprite.Sprite) :
    def __init__(self,x,y,image,speed,forward=True):
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

        if len(pygame.sprite.spritecollide(self,enemy_group,False)) > 0 :
            pygame.sprite.spritecollide(self, enemy_group, False)[0].health -= 20

            self.kill()









