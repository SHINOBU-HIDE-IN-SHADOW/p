import os,pygame,sys
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")
class Player:
    def __init__(self,width,height):
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
        self.width = width
        self.height = height
        self.speed = 2
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
        self.moverx = 0
        self.movery = 0
        self.pos = self.a.move(self.positionx, self.positiony)
    def block(self,x1):
        if x1-1 == self.moverx:
            if self.positionx+self.a.width-20 > self.width-20:
                self.positionx =  self.width-self.a.width
        elif self.moverx == 0:
            if self.positionx < 0:
                self.positionx = 0
        if x1-1 == self.movery:
            if self.positiony+self.a.height-20 > self.height-20:
                self.positiony = self.height-self.a.height
        elif self.movery == 0:   
            if self.positiony <0:
                self.positiony = 0
    def updateron(self):
        self.spritemovers = True
    def updateroff(self):
        self.spritemovers = False
        self.spritenow = 0
        self.playersprite(0)
    def playersprite(self,a):
        if self.positiontoy1 != 0:
            if self.positiontox == 0 and self.positiontox1 == 0:
                self.x = 0
                self.y = 1
                self.spritenow +=a
                if int(self.spritenow) >= len(self.moverf):
                    self.spritenow = 0
                self.texterure = self.moverf[int(self.spritenow)]
                # self.texterure = self.texterureb
            elif self.y != 0 and (self.positiontox != 0 or self.positiontox1 != 0):
                    self.x = 0
                    self.y = 1
                    self.spritenow +=a
                    if int(self.spritenow) >= len(self.moverf):
                        self.spritenow = 1
                    self.texterure = self.moverf[int(self.spritenow)]
        elif self.positiontoy != 0:
            if self.positiontox == 0 and self.positiontox1 == 0:
                self.x = 0
                self.y = -1
                self.spritenow +=a
                if int(self.spritenow) >= len(self.moverl):
                    self.spritenow = 1
                self.texterure = self.moverb[int(self.spritenow)]
                # self.texterure = self.texteruref
            elif self.y != 0 and (self.positiontox != 0 or self.positiontox1 != 0):
                    self.x = 0
                    self.y = -1
                    self.spritenow +=a
                    if int(self.spritenow) >= len(self.moverl):
                        self.spritenow = 1
                    self.texterure = self.moverb[int(self.spritenow)]
        else: 
            if self.x == 1 and self.y == 0:
                self.texterure = self.moverr[0]
            if self.x == -1 and self.y == 0:
                self.texterure = self.moverl[0]
            if self.x == 0 and self.y == 1:
                self.texterure = self.moverf[0]
            if self.x == 0 and self.y == -1:
                self.texterure = self.moverb[0]
        if self.positiontox != 0:
            if self.positiontoy == 0 and self.positiontoy1 == 0:
                self.x = 1
                self.y = 0
                self.spritenow +=a
                if int(self.spritenow) >= len(self.moverr):
                    self.spritenow = 1
                self.texterure = self.moverr[int(self.spritenow)]
            elif self.y == 0 and (self.positiontoy != 0 or self.positiontoy1 != 0):
                self.x = 1
                self.y = 0
                self.spritenow +=a
                if int(self.spritenow) >= len(self.moverr):
                    self.spritenow = 1
                self.texterure = self.moverr[int(self.spritenow)]
        elif self.positiontox1 != 0:
            if self.positiontoy == 0 and self.positiontoy1 == 0:
                self.x = -1
                self.y = 0
                self.spritenow +=a
                if int(self.spritenow) >= len(self.moverl):
                    self.spritenow = 1
                self.texterure = self.moverl[int(self.spritenow)]
                # self.texterure = self.texterurer
            elif self.y == 0 and (self.positiontoy != 0 or self.positiontoy1 != 0):
                self.x = -1
                self.y = 0
                self.spritenow +=a
                if int(self.spritenow) >= len(self.moverl):
                    self.spritenow = 1
                self.texterure = self.moverl[int(self.spritenow)]
    def blocker(self,a,b):
        if a.colliderect(b):
            if a.left == b.right-2:
                self.positionx+=2
            if a.right == b.left+2:
                self.positionx-=2
            if a.bottom == b.top+2:
                self.positiony-=2
            if a.top == b.bottom-2:
                self.positiony+=2
