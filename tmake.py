import os,pygame,sys
#######
pygame.display.set_caption("z")
pygame.init()
run = True
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
########
######background
background = pygame.image.load(os.path.join(image_path, "background.png"))
ball1 = pygame.image.load(os.path.join(image_path, "balloon1.png"))
ball = pygame.transform.scale(ball1,(100,100))
##player
class Player:
    def __init__(self):
        self.moverf = []
        self.moverl = []
        self.moverr = []
        self.moverb = []
        self.texteruref= pygame.image.load(os.path.join(image_path,'front.png'))
        self.texterurel= pygame.image.load(os.path.join(image_path,'left.png'))
        self.texterurer= pygame.image.load(os.path.join(image_path,'right.png'))
        self.texterureb= pygame.image.load(os.path.join(image_path,'back.png'))
        self.moverl.append(pygame.image.load(os.path.join(image_path,'right.png')))
        self.moverl.append(pygame.image.load(os.path.join(image_path,'rightwalk1.png')))
        self.moverl.append(pygame.image.load(os.path.join(image_path,'rightwalk2.png')))
        self.moverr.append(pygame.image.load(os.path.join(image_path,'left.png')))
        self.moverr.append(pygame.image.load(os.path.join(image_path,'leftwalk1.png')))
        self.moverr.append(pygame.image.load(os.path.join(image_path,'leftwalk2.png')))
        self.moverb.append(pygame.image.load(os.path.join(image_path,'front.png')))
        self.moverb.append(pygame.image.load(os.path.join(image_path,'frontwalk1.png')))
        self.moverb.append(pygame.image.load(os.path.join(image_path,'frontwalk2.png')))
        self.moverf.append(pygame.image.load(os.path.join(image_path,'back.png')))
        self.moverf.append(pygame.image.load(os.path.join(image_path,'backwalk1.png')))
        self.moverf.append(pygame.image.load(os.path.join(image_path,'backwalk2.png')))
        self.texterure = self.texteruref
        self.a = self.texterure.get_rect()
        self.speed = 1
        self.spritenow = 0
        self.spritemovers = False
        self.positionx = 0
        self.positiontox = 0
        self.positiontox1 = 0
        self.positiony = 0
        self.positiontoy = 0
        self.positiontoy1 = 0
        self.x = 0
        self.y = 0
        self.pos = self.a.move(self.positionx, self.positiony)
    def block(self):
        if self.positionx > width-20:
            self.positionx = width-20
        if self.positionx < 0:
            self.positionx = 0
        if self.positiony > height-20:
            self.positiony = height-20
        if self.positiony <0:
            self.positiony = 0
    def updateron(self):
        self.spritemovers = True
    def updateroff(self):
        self.spritemovers = False
        self.spritenow = 0
        self.playersprite(0)
    def playersprite(self,a):
        if self.positiontox != 0:
            if self.positiontoy == 0 and self.positiontoy1 == 0:
                self.x = 1
                self.y = 0
                self.spritenow +=a
                if int(self.spritenow) >= len(self.moverl):
                    self.spritenow = 1
                self.texterure = self.moverr[int(self.spritenow)]
            else:
                self.texterure = self.texterure
        elif self.positiontox1 != 0:
            if self.positiontoy == 0 and self.positiontoy1 == 0:
                self.x = -1
                self.y = 0
                self.spritenow +=a
                if int(self.spritenow) >= len(self.moverl):
                    self.spritenow = 1
                self.texterure = self.moverl[int(self.spritenow)]
                # self.texterure = self.texterurer
            else:
                self.texterure = self.texterure
        elif self.positiontoy1 != 0:
            if self.positiontox == 0 and self.positiontox1 == 0:
                self.x = 0
                self.y = 1
                self.spritenow +=a
                if int(self.spritenow) >= len(self.moverl):
                    self.spritenow = 1
                self.texterure = self.moverf[int(self.spritenow)]
                # self.texterure = self.texterureb
        elif self.positiontoy != 0:
            if self.positiontox == 0 and self.positiontox1 == 0:
                self.x = 0
                self.y = -1
                self.spritenow +=a
                if int(self.spritenow) >= len(self.moverl):
                    self.spritenow = 1
                self.texterure = self.moverb[int(self.spritenow)]
                # self.texterure = self.texteruref
        else: 
            if self.x == 1 and self.y == 0:
                self.texterure = self.moverr[0]
            if self.x == -1 and self.y == 0:
                self.texterure = self.moverl[0]
            if self.x == 0 and self.y == 1:
                self.texterure = self.moverf[0]
            if self.x == 0 and self.y == -1:
                self.texterure = self.moverb[0]
    def blocker(self,a,b):
         if self.a.colliderect(b):
            if a.left == b.right-2:
                self.positionx+=2
            elif a.right == b.left+1:
                self.positionx-=1
            elif a.bottom == b.top+1:
                self.positiony-=1
            elif a.top == b.bottom-2:
                self.positiony+=2   
##main run
player1 =Player()
asw = 1
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RIGHT,pygame.K_d):      
                player1.positiontox += player1.speed
            elif event.key in (pygame.K_LEFT,pygame.K_a):
                player1.positiontox1 -= player1.speed
            elif event.key in (pygame.K_UP,pygame.K_w):
                player1.positiontoy1 -= player1.speed
            elif event.key in (pygame.K_DOWN,pygame.K_s):
                player1.positiontoy += player1.speed
            player1.block()
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_RIGHT,pygame.K_d):
                player1.positiontox = 0
            elif event.key in (pygame.K_LEFT,pygame.K_a):
                player1.positiontox1 = 0
            elif event.key in (pygame.K_DOWN,pygame.K_s):
                player1.positiontoy = 0
            elif event.key in (pygame.K_UP,pygame.K_w):
                player1.positiontoy1 = 0
            player1.updateroff()
    player1.playersprite(0.1)
    ball_rect = ball.get_rect()
    ball_x = 100
    ball_y= 50
    ball_rect.left = ball_x
    ball_rect.top = ball_y
    #######33
    player_rect = player1.a
    player_rect.left = player1.positionx
    player_rect.top = player1.positiony
    screen.blit(background, (0, 0))
    player1.blocker(player_rect,ball_rect)
    # if player1.a.colliderect(ball_rect):
    #         if player_rect.left == ball_rect.right-2:
    #             player1.positionx+=2
    #         elif player_rect.right == ball_rect.left+1:
    #             player1.positionx-=1
    #         elif player_rect.bottom == ball_rect.top+1:
    #             player1.positiony-=1
    #         elif player_rect.top == ball_rect.bottom-2:
    #             player1.positiony+=2  
    player1.positionx += player1.positiontox
    player1.positiony += player1.positiontoy
    player1.positionx += player1.positiontox1
    player1.positiony += player1.positiontoy1
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(player1.texterure,(player1.positionx,player1.positiony)) 
    player1.block()
    pygame.display.update()
    
    