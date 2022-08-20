import pygame,random,sys,spritemaker
pygame.init()
size = width,height = 500,500
screen = pygame.display.set_mode(size)
run = True
text = pygame.image.load("image/Textures.png")
images = spritemaker.spriter(text)
tile_group = pygame.sprite.Group()
#image[widht,height,scale,framex,framey]
class Snake(pygame.sprite.Sprite):
    def __init__(self,pict):
        super().__init__()
        self.image = pygame.image.load(pict)
        self.rect = self.image.get_rect()
class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        tile1 = images.getim(384,384,0.2,1,6)
        tile2 = images.getim(384,384,0.2,1,5)
        tile3 = images.getim(384,384,0.2,1,7)
        tile4 = images.getim(384,384,0.2,2,5)
        tile5 = images.getim(384,384,0.2,2,6)
        tile6 = images.getim(384,384,0.2,2,7)
class fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        patile1 = images.getim(384,384,0.2,4,1)

player = Snake("image/Vignette.png")
snake_group = pygame.sprite.Group()
snake_group.add(player)
Tile()
print(tile_group)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0,0,0))
    snake_group.draw(screen)
    pygame.display.update()