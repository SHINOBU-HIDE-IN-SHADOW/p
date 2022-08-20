import pygame,random,sys
pygame.init()
size = width,height = 500,500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
run = True
class Sneak:
    def __init__(self,a,b):      
        self.x = a
        self.y = b
        self.way = ""
        self.width = width/16
        self.height = height/16
        self.speedx =(self.width%width)-1
        self.speedy =(self.height%height)-1
        self.speedmax = 50000/(width+height)
        
    def update(self):
        if self.way == "y" :
            self.y += self.speedy
        elif self.way == "-y" :
            self.y -= self.speedy
        elif self.way == "x" :
            self.x += self.speedx
        elif self.way == "-x" :
            self.x -= self.speedx
        if self.x <=0:
            self.x = width+1
        elif self.x >=width:
            self.x = 1
        elif self.y<=0:
            self.y = height+1
        elif self.y >=height:
            self.y = 1
class Game:
    def __init__(self,a): 
        self.list = []  
        self.applepoint = 1
    def update(self):
        sx,sy = sneak.x,sneak.y
        self.list.append((sx,sy))
        if len(self.list) > self.applepoint:
            del self.list[0]
        for (x,y) in self.list:
            self.image = pygame.draw.rect(screen, (255,0,0),[x,y,sneak.width,sneak.height])
        for (x,y) in self.list[:-1]:
            if sx == x and sy == y:
                print(x,y)
        if fruit.image.colliderect([sx,sy,sneak.width,sneak.height]):
            self.applepoint += 1
            fruit.reposition()
    def positionchanger(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and sneak.way != "y":
                sneak.way = "-y"
            if event.key == pygame.K_a and sneak.way != "x":
                sneak.way = "-x"
            if event.key == pygame.K_s and sneak.way != "-y":
                sneak.way = "y"
            if event.key == pygame.K_d and sneak.way != "-x":
                sneak.way = "x"
class Fruit:
    def __init__(self):        
        self.x = 0
        self.y = 0
        self.width = width/16
        self.height = height/16
        self.rx = int(width-self.width)
        self.ry = int(height-self.height)
    def update(self):
        self.image = pygame.draw.rect(screen, (255,255,255), [self.x, self.y, self.width, self.height])    
    def reposition(self):
        self.x,self.y = random.randrange(0, self.rx),random.randrange(0, self.ry)
sneak = Sneak(110,110)
fruit = Fruit()
game = Game(sneak)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        game.positionchanger()
    screen.fill((0,0,0))
    fruit.update()
    game.update()
    sneak.update()
    pygame.display.update()
    clock.tick(20)