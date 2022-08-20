import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [1, 1]
black = 255, 255, 255

screena = pygame.display.set_mode(size)
screenb = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screena.fill(black)
    screenb.fill(black)
    pygame.display.flip()