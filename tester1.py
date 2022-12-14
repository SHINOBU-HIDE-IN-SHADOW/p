import sys, pygame
pygame.init()

class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self):
        self.pos = self.pos.move(self.speed, 0)
        if self.pos.right > 600:
            self.pos.left = 0
screen = pygame.display.set_mode((640, 480))
player = pygame.image.load('m1.png').convert()
background = pygame.image.load('ground.png').convert()
screen.blit(background, (0, 0))
objects = []

for x in range(10):                  
    o = GameObject(player, x*40, x)
    objects.append(o)
while 1:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            sys.exit()
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    pygame.display.update()
    pygame.time.delay(100)