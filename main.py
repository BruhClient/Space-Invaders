import pygame
from engine import Spritesheet
from models.spaceships import Spaceship
from models.bullet import bullet_group
from models.enemies import enemy_group,EnemySpaceship,missile_group
from models.explosion import Explosion_Group
pygame.init()


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))



clock = pygame.time.Clock()
FPS = 60

# Player Spaceship
Lightning = Spritesheet("assets/spaceships/Lightning.png").parse_sprite(4,0,0,32,32,1.8)
Ligher = Spritesheet("assets/spaceships/Ligher.png").parse_sprite(4,0,0,32,32,1.8)
Dove = Spritesheet("assets/spaceships/Dove.png").parse_sprite(4,0,0,32,32,1.8)
Ninja = Spritesheet("assets/spaceships/Ninja.png").parse_sprite(4,0,0,32,32,1.8)
Paranoid = Spritesheet("assets/spaceships/Paranoid.png").parse_sprite(4,0,0,32,32,1.8)

# Bullets
bullet_img = pygame.image.load("assets/bullets/bullet.png").convert()
bullet_img.set_colorkey((255,255,255))

# Enemies
enemy_spaceship_img1 = pygame.transform.flip(pygame.image.load("assets/enemies/Spaceship1.png").convert_alpha(),False,True)
enemy_group.add(EnemySpaceship(100,10,enemy_spaceship_img1,10,2,100))

# Explosions
Explosion1 = Spritesheet("assets/explosions/explosion.png").parse_sprite(6,0,0,32,32,1)

player_spaceship = Spaceship(100,100,Paranoid,bullet_img,3)

running = True
while running :
    clock.tick(60)
    screen.fill((0,0,0))
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False




    bullet_group.draw(screen)
    missile_group.draw(screen)
    Explosion_Group.draw(screen)
    player_spaceship.update(screen,FPS)


    enemy_group.draw(screen)

    for enemy in enemy_group :

        pygame.draw.rect(screen,(255,0,0),pygame.Rect(enemy.rect.x , enemy.rect.y -5,enemy.rect.width ,5))
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(enemy.rect.x , enemy.rect.y -5,(enemy.health / 100) *  enemy.rect.width, 5))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(enemy.rect.x , enemy.rect.y -5, enemy.rect.width, 5),1)

    bullet_group.update()
    missile_group.update()
    enemy_group.update()
    Explosion_Group.update()

    pygame.display.update()