import os,pygame,sys
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")
class wallcreate:
    def __init__(self,size_x,size_y):
        self.wall1 =(pygame.image.load(os.path.join(image_path, "balloon1.png")))
        self.wall = pygame.transform.scale(self.wall1,(10,10))
        self.rect = self.wall.get_rect()
        self.x = size_x
        self.y = size_y
        self.rect.left = self.x
        self.rect.top = self.y
class door:
    def __init__(self,size_x,size_y):
        self.door1 =(pygame.image.load(os.path.join(image_path, "balloon2.png")))
        self.door1.fill((0, 255, 255), special_flags=pygame.BLEND_ADD)
        self.door = pygame.transform.scale(self.door1,(50,50))
        self.rect = self.door.get_rect()
        self.x = size_x
        self.y = size_y
        self.px = 0
        self.py = 0
        self.rect.left = size_x
        self.rect.top = size_y
class lister:
    def __init__(self):
        self.list = []
        self.listdoor = []
    def appender(self,a):
        self.list.append(a)
    def dooradd(self,a):
        self.listdoor.append(a)
    def listreserer(self):
        self.list = []
        self.listdoor =[]
        
    
