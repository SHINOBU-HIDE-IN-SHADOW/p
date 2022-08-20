import pygame
class spriter:
    def __init__(self,image):
        self.sheet = image

    def getim(self,width,height,scale,framex,framey):
        image = pygame.Surface((width,height),pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet,(0,0),((width*framex),(height*framey),width,height))
        image = pygame.transform.scale(image,(int(width* scale),int(height*scale)))
        image.set_colorkey((0,0,0))
        return image