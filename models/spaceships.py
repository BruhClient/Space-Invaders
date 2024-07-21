import pygame
from models.bullet import Bullet,bullet_group
from models.enemies import missile_group
class Spaceship(pygame.sprite.Sprite) :
    def __init__(self,x,y,images,bullet,speed):
        pygame.sprite.Sprite.__init__(self)

        self.images = images
        self.frames = len(self.images)
        self.rect = self.images[0].get_rect()
        self.rect.center = (x,y)

        self.image_speed = 0.1
        self.image_counter = 0
        self.image_selector = 0

        self.speed = speed
        self.speed_x = 1 * self.speed
        self.speed_y = 1 * self.speed



        self.bullet_img = bullet
        self.fire_rate = 30
        self.counter = 0

        self.health = 40



    def controls(self):
        keys = pygame.key.get_pressed()



        if keys[pygame.K_LEFT] :
            self.rect.x -= self.speed_x
        if keys[pygame.K_RIGHT] :
            self.rect.x += self.speed_x
        if keys[pygame.K_UP] :
            self.rect.y -= self.speed_y
        if keys[pygame.K_DOWN] :
            self.rect.y += self.speed_y

        if keys[pygame.K_SPACE] and self.counter >= self.fire_rate:
            bullet_group.add(Bullet(self.rect.center[0],self.rect.center[1],self.bullet_img,10))
            self.counter =0

        if self.counter < self.fire_rate :
            self.counter += 1

        if self.rect.x < 0 :
            self.rect.x = 0

        if self.rect.x > 500 - self.rect.width:
            self.rect.x =  500 - self.rect.width

        if self.rect.y > 500 - self.rect.height :
            self.rect.y = 500 - self.rect.height

        if self.rect.y < 0 :
            self.rect.y  = 0


    def update(self,screen,FPS):

        if self.health <= 0:
            return # GameOver
        if pygame.sprite.spritecollide(self,missile_group,True) :
            self.health-= 20


        if self.image_counter > self.image_speed * FPS :
            self.image_selector = ( self.image_selector + 1 ) % self.frames
            self.image_counter = 0
        else :
            self.image_counter += 1

        self.controls()

        pygame.draw.rect(screen,(255,0,0),pygame.Rect(10 , 10,200 ,20))
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(10, 10,(self.health / 100) *  200, 20))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(10, 10, 200, 20),1)

        screen.blit(self.images[self.image_selector],self.rect)







