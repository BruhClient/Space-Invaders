import pygame

class Spritesheet:
    def __init__(self,filename):
        self.filename = filename
        self.spritesheet = pygame.image.load(filename).convert()


    def get_sprite(self,x,y,w,h):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.spritesheet,(0,0),(x,y,w,h))
        return sprite

    def parse_sprite(self,frames,x,y,w,h,scale=1,horizontal=True):
        images = []
        if horizontal :

            for frame in range(frames):
                image = self.get_sprite(x + frame * w,y,w,h)
                images.append(pygame.transform.scale_by(image,scale))

            return images
        else :
            for frame in range(frames):
                image = self.get_sprite(x, y + frame * h , w, h)
                images.append(pygame.transform.scale_by(image,scale))

            return images







