import pygame,random,sys,spritemaker
pygame.init()
size = width,height = 500,500
screen = pygame.display.set_mode(size)
run = True
text = pygame.image.load("image/Textures.png")
getim = spritemaker.spriter(text)
player = getim.getim(384,384,0.16666666666666666,2,0)
print(player)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255,255,255))
    screen.blit(player,(0,0))
    pygame.display.update()