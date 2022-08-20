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
scalef = round(100/(width+height),2)
longlist = []
listid = 0
#image[widht,height,scale,framex,framey]
score = 0
class Snake_head(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.head = images.getim(384,384,scales,2,0)
        self.image = self.head 
        self.rect = self.image.get_rect()
        self.x = 0
        self.y= 0
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = 1
        self.wayr=""
    def update(self):
        if self.wayr == "x":
            self.x+= self.speed
            self.image = pygame.transform.rotate(self.head, 0)
        elif self.wayr == "-x":
            self.x-= self.speed
            self.image = pygame.transform.rotate(self.head, 180)
        elif self.wayr == "y":
            self.y+= self.speed
            self.image = pygame.transform.rotate(self.head, -90)
        elif self.wayr == "-y":
            self.y-= self.speed
            self.image = pygame.transform.rotate(self.head, 90)
        self.rect.x = self.x
        self.rect.y = self.y
class Snake_body(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagelist = []
        self.body1= images.getim(384,384,scales,1,0)
        self.body2= images.getim(384,384,scales,0,1)
        self.body3= images.getim(384,384,scales,1,1)
        self.body4= images.getim(384,384,scales,2,1)
        self.body5= images.getim(384,384,scales,3,1)
        self.tail = images.getim(384,384,scales,0,0)
        self.imagelist.append(self.body1)
        self.imagelist.append(self.body2)
        self.imagelist.append(self.body3)
        self.imagelist.append(self.body4)
        self.imagelist.append(self.body5)
        self.imagelist.append(self.tail)
        self.image = self.imagelist[0]
        self.rect = self.image.get_rect()
       
        self.wayr = ""
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
        self.patile1 = images.getim(384,384,0.1,3,0)
        self.getrect = self.patile1.get_rect()
    def anyt(self,a):
        global score,listid
        if self.getrect.colliderect(a):
            score +=1
            snake_body = Snake_body() 
            snake_group.add(snake_body)
            longlist.append([snake_body,listid])
            snake_body.rect.x= snake.rect.x
            snake_body.rect.y= snake.rect.y
            listid += 1
            snake.speed += 0.1
            self.position_maker()
    def position_maker(self):
        a=self.patile1.get_width()
        b=self.patile1.get_height()
        self.x=random.randrange(0, width-a)
        self.y=random.randrange(0, height-b)
        self.getrect.x = self.x
        self.getrect.y = self.y
    def maker(self):
        screen.blit(self.patile1,(self.x,self.y))
tiles= Tile()
fruit = Fruit()
tiles.backgroundmake()
fruit.position_maker()
snake = Snake_head()
snake_body = Snake_body() 
snake_body.image = snake_body.imagelist[-1]
snake_group = pygame.sprite.Group()
snakere_group = pygame.sprite.Group()
snakere_group.add(snake)
longlist.append([snake,listid])
listid += 1
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d and snake.wayr != "x" and snake.wayr != "-x":
                snake.wayr="x"
            if event.key == pygame.K_a and snake.wayr != "x" and snake.wayr != "-x":
                snake.wayr="-x"
            if event.key == pygame.K_w and snake.wayr != "y" and snake.wayr != "-y":
                snake.wayr="-y"
            if event.key == pygame.K_s and snake.wayr != "y" and snake.wayr != "-y":
                snake.wayr="y"
    screen.fill(black)
    for tile in tiles.tilelist:
        tile_image,x,y = tile
        screen.blit(tile_image,(x,y))
    listmover()
    fruit.maker()
    snakere_group.draw(screen)
    snakere_group.update()
    snake_group.draw(screen)
    snake_group.update()
    fruit.anyt(snake.rect)
    pygame.display.update()