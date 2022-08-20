import os,pygame,sys,walllister,colorsys
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")
wallist = walllister.lister()
class a1:
    def __init__(self):
        self.background = pygame.image.load(os.path.join(image_path, "background.png"))
        wall1 = walllister.wallcreate(300,400)
        wallist.appender(wall1)
        
class a2:
    def __init__(self):
        self.background = pygame.image.load(os.path.join(image_path, "background.png"))
        color = colorsys.hsv_to_rgb(1,1,1)
        self.background.fill((color[0]*255, color[1]*255, color[2]*255), special_flags=pygame.BLEND_ADD)
        for x in range(3):
            wall1 = walllister.wallcreate(4*x,100*x)
            wallist.appender(wall1)
        door1 = walllister.door(20,300)
        wallist.dooradd(door1)
class maps:
    def __init__(self):
        self.list = [[None for x in range(3)] for y in range(3)]
        self.list[0][0] = a1
        self.list[0][1] = a2
        self.list[0][2] = a1
        self.list[1][0] = a2
        self.list[1][1] = a1
        self.list[1][2] = a2
        self.list[2][0] = a1
        self.list[2][1] = a2
        self.list[2][2] = a1
        self.map_now = a1()
    def updater(self,a,b,c):
        c.blit(self.map_now.background, (0, 0))
        for wall1 in wallist.list:
            a.blocker(b,wall1.rect)
        for door1 in wallist.listdoor:
            if b.colliderect(door1.rect):
                self.mapchange(1,2)
                a.moverx=1
                a.movery=2
                a.positionx =0
                a.positiony =0
        for wall1 in wallist.list:
            c.blit(wall1.wall,(wall1.x,  wall1.y))  
        for door1 in wallist.listdoor:
            c.blit(door1.door,(door1.x,  door1.y))  
        print(b,wall1.rect)
    def mapchange(self,x,y):
        print(len(self.list))
        if self.list[x][y] == a1:
            wallist.listreserer()
            self.map_now = a1()
            x = 3
            y = 3
        elif self.list[x][y] == a2:
            wallist.listreserer()
            self.map_now = a2()
            x = 3
            y = 3
        elif self.list[x][y] == a3:
            wallist.listreserer()
            self.map_now = a1()
            x = 3
            y = 3
        elif self.list[x][y] == a4:
            wallist.listreserer()
            self.map_now = a2()
            x = 3
            y = 3
        elif self.list[x][y] == a5:
            wallist.listreserer()
            self.map_now = a1()
            x = 3
            y = 3
        elif self.list[x][y] == a6:
            wallist.listreserer()
            self.map_now = a2()
            x = 3
            y = 3
        elif self.list[x][y] == a7:
            wallist.listreserer()
            self.map_now = a1()
            x = 3
            y = 3
        elif self.list[x][y] == a8:
            wallist.listreserer()
            self.map_now = a2()
            x = 3
            y = 3
        elif self.list[x][y] == a9:
            wallist.listreserer()
            self.map_now = a1()
            x = 3
            y = 3