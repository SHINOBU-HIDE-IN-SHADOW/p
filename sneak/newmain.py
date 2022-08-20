import pygame,random,sys,spritemaker,random
pygame.init()
size = width,height = 500,400
screen = pygame.display.set_mode(size)
run = True
textures = pygame.image.load("image/Textures.png")
images = spritemaker.spriter(textures)
black = (255,255,255)
scales = round(50/(width+height),2)
scalet = round(150/(width+height),2)
scalef = round(50/(width+height),2)
clock = pygame.time.Clock()
fontsize =int((width+height)*0.02)
font = pygame.font.Font("scr/7_Emulogic.ttf",fontsize)
lost= pygame.image.load("image/LoseScreen.png")
lost = pygame.transform.scale(lost,(width,height))
start= pygame.image.load("image/StartScreen.png")
start = pygame.transform.scale(start,(width,height))
mainmusic = pygame.mixer.Sound("scr/birds.ogg")
bite = pygame.mixer.Sound("scr/apple_bite.ogg")
losesound = pygame.mixer.Sound("scr/losesound2.wav")
mainmusic.set_volume(0.5)
#image[widht,height,scale,framex,framey]
score = 0
class Snake:
    def __init__(self,a,b):    
        self.x = a
        self.y = b
        self.way = ""
        self.imagelist = []
        self.head = images.getim(384,384,scales,2,0)
        self.body1= images.getim(384,384,scales,1,0)
        self.body2= images.getim(384,384,scales,0,1)
        self.body3= images.getim(384,384,scales,1,1)
        self.body4= images.getim(384,384,scales,2,1)
        self.body5= images.getim(384,384,scales,3,1)
        self.tail = images.getim(384,384,scales,0,0)
        self.imagelist.append(self.head)
        self.imagelist.append(self.body1)
        self.imagelist.append(self.body2)
        self.imagelist.append(self.body3)
        self.imagelist.append(self.body4)
        self.imagelist.append(self.body5)
        self.imagelist.append(self.tail)
        self.image = self.imagelist[0]
        self.rect = self.image.get_rect()
        self.width = self.head.get_width()
        self.height = self.head.get_height()
        self.speedx =(self.width%width)-1
        self.speedy =(self.height%height)-1
        self.speedmax = 50000/(width+height)
    def update(self):
        if self.way == "y" :
            self.y += self.height
        elif self.way == "-y" :
            self.y -= self.height
        elif self.way == "x" :
            self.x += self.width
        elif self.way == "-x" :
            self.x -= self.width
        self.rect.x = self.x
        self.rect.y = self.y
        if self.rect.x <=0:
            self.x = 1
        elif self.rect.x >=width-self.width:
            self.x= width-self.width
        elif self.rect.y<=0:
            self.y = 1
        elif self.rect.y >=height-self.height:
            self.y = height-self.width
class Tile:
    def __init__(self):
        self.tile1 = images.getim(384,384,scalet,4,0)
        self.tile2 = images.getim(384,384,scalet,5,0)
        self.tile3 = images.getim(384,384,scalet,6,0)
        self.tile4 = images.getim(384,384,scalet,4,1)
        self.tile5 = images.getim(384,384,scalet,5,1)
        self.tile6 = images.getim(384,384,scalet,6,1)
    def backgroundmake(self):
        self.tilelist = []
        a = self.tile1.get_width()
        b = self.tile4.get_height()
        tox =int(width/a)+1
        toy = int(height/b)+1
        for x in range(tox):
            for y in range(toy):
                if (y+x)%2==0:
                    self.tilelist.append([self.tile4,x*a,y*b])
                elif (y+x)%2!=0:
                    self.tilelist.append([self.tile1,x*a,y*b])  
class Fruit:
    def __init__(self):
        self.patile1 = images.getim(384,384,scalef,3,0)
        self.getrect = self.patile1.get_rect()
    def position_maker(self):
        a=self.patile1.get_width()
        b=self.patile1.get_height()
        self.x=random.randrange(0, width-a)
        self.y=random.randrange(0, height-b)
        self.getrect.x = self.x
        self.getrect.y = self.y
    def maker(self):
        screen.blit(self.patile1,(self.x,self.y))
class Game:
    def __init__(self): 
        self.list = []  
        self.applepoint = 1
        self.image = snake.image
        self.scorex = width/2
        self.state = "game"
        self.test = 0
    def update(self):
        global run
        sx,sy = snake.x,snake.y
        way = snake.way
        if way =="x":
            self.image = pygame.transform.rotate(snake.image, 0)
        elif way =="-x":
            self.image = pygame.transform.rotate(snake.image, 180)
        elif way =="y":
            self.image = pygame.transform.rotate(snake.image, -90)
        elif way =="-y":
            self.image = pygame.transform.rotate(snake.image, 90)
        self.list.append([self.image,snake.way,sx,sy])
        if len(self.list) > self.applepoint:
            del self.list[0]
        for sneak in range(len(self.list)-1):
            if sneak == 0:
                a= snake.imagelist[6] 
                if self.list[sneak][1] =="x":
                    a = pygame.transform.rotate(a, 0)
                elif self.list[sneak][1] =="-x":
                    a = pygame.transform.rotate(a, 180)
                elif self.list[sneak][1] =="y":
                    a = pygame.transform.rotate(a, -90)
                elif self.list[sneak][1] =="-y":
                    a = pygame.transform.rotate(a, 90)
            else:
                try:
                    if self.list[sneak][2] == self.list[sneak-1][2] and self.list[sneak][3] == self.list[sneak+1][3]:
                        if self.list[sneak][1] == "-y":
                            if self.list[sneak+1][1] == "x":
                                a= snake.imagelist[2]  
                            elif self.list[sneak+1][1] == "-x":
                                a= snake.imagelist[3]  
                        elif self.list[sneak][1] == "y":
                            if self.list[sneak+1][1] == "-x":
                                a= snake.imagelist[5] 
                            elif self.list[sneak+1][1] == "x":
                                a= snake.imagelist[4]  
                    elif self.list[sneak][2] == self.list[sneak+1][2] and self.list[sneak][3] == self.list[sneak-1][3]:
                        if self.list[sneak][1] == "-x":
                            if self.list[sneak+1][1] == "-y":
                                a= snake.imagelist[4]  
                            elif self.list[sneak+1][1] == "y":
                                a= snake.imagelist[2] 
                        if self.list[sneak][1] == "x":
                            if self.list[sneak+1][1] == "-y":
                                a= snake.imagelist[5]  
                            elif self.list[sneak+1][1] == "y":
                                a= snake.imagelist[3] 
                    else:    
                        a= snake.imagelist[1]
                except:    
                    a= snake.imagelist[1]        
            self.list[sneak][0] = a 
        for sneak in self.list:
            a,w,x,y = sneak
            screen.blit(a,(x,y))
        for sneak in self.list[:-1]:
            img,way,x,y = sneak
            if snake.x == x and snake.y == y:
                if self.state == "game":
                    clock.tick(1)
                    losesound.play()
                    self.state = "lose"
        if fruit.getrect.colliderect([sx,sy,snake.width,snake.height]):
            self.applepoint += 1
            bite.play()
            bite.fadeout(500)
            fruit.position_maker()
        score = font.render("SCORE: "+str(self.applepoint-2),0,(255,255,255))
        screen.blit(score,(0,0))
    def positionchanger(self):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.applepoint += 20
                if event.key == pygame.K_w and snake.way != "y":
                    snake.way = "-y"
                elif event.key == pygame.K_a and snake.way != "x":
                    snake.way = "-x"
                elif event.key == pygame.K_s and snake.way != "-y":
                    snake.way = "y"
                elif event.key == pygame.K_d and snake.way != "-x":
                    snake.way = "x"
                if self.applepoint ==1:
                    self.applepoint +=1
tiles = Tile()
tiles.backgroundmake()
snake = Snake(1,1)
fruit = Fruit()
fruit.position_maker()
game = Game()
game.state = "start"
while run:
    if game.state == "start":
        if pygame.mixer.get_busy() == False:
            mainmusic.play() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                mainmusic.stop()
                game.state = "game"
        screen.blit(start,(0,0))
        pygame.display.update()
    elif game.state == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            game.positionchanger()
        for tile in tiles.tilelist:
            tile_image,x,y = tile
            screen.blit(tile_image,(x,y))
        fruit.maker()
        snake.update()
        game.update()
        pygame.display.update()
        clock.tick(15)
    elif game.state == "lose":       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    tiles = Tile()
                    tiles.backgroundmake()
                    snake = Snake(1,1)
                    fruit = Fruit()
                    fruit.position_maker()
                    game = Game()
        screen.blit(lost,(0,0))
        pygame.display.update()
        clock.tick(15)
        