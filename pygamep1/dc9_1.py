from ursina import *
import random
class Bar(Text):
    def __init__(self,parent,text,r,g,b,ox,oy):
            super().__init__()
            self.parent = parent
            self.color = color.rgb(r,g,b)
            self.text = text
            self.scale = (5,5)
            self.origin = (ox,oy)
            self.z = -2
class Monster(Button):  
    def __init__(self, position=(0,0), texture = "ground"):
            super().__init__(
            parent=scene, position=position,
                    color = color.white,highlight_color = color.white,texture = texture,
                    visible = False,name = "monster")   
            self.typer = "monster"
            self.health = 0    
            self.damage = 0   
            self.m_health = 0
            self.m_damage = 0
    def Bar_maker(self, health,damage):
            self.health = health    
            self.damage = damage   
            self.m_health = Bar(self,str(self.health),255,255,255,-1.6,-2)
            self.m_damage = Bar(self,str(self.damage),255,255,255,1.3,-2)
    def Bar_mover(self, health,damage):
            destroy(self.m_health)
            destroy(self.m_damage)
            self.health = health    
            self.damage = damage   
            self.m_health = Bar(self,str(self.health),255,255,255,-1.6,-2)
            self.m_damage = Bar(self,str(self.damage),255,255,255,1.3,-2) 
    def Open(self):
            openchoose = random.choice(["position","item"])
            if openchoose == "position":
                self.typer = random.choice(["Attack","Health","Attack","Health","Attack","Health","Attack_Health"])
            elif openchoose == "item":
                self.typer = random.choice(["item1","item2","item3","item4","item5"]) 

            if self.typer =="Attack":
                    self.texture ="ap1.png"
            elif self.typer =="Health":
                    self.texture ="hp1.png"
            elif self.typer =="Attack_Health":
                    self.texture ="hap1.png" 
            elif self.typer =="item1":
                    self.texture ="item1.png"
            elif self.typer =="item2":
                    self.texture ="item2.png" 
            elif self.typer =="item3":
                    self.texture ="item3.png"
            elif self.typer =="item4":
                    self.texture ="item4.png" 
            elif self.typer =="item5":
                    self.texture ="item5.png" 
    def Usepotion(self,Player):
            if self.typer =="Attack":
                    Player.damage = Player.damage +2
                    Player.damageinc = 2
            if self.typer =="Health":
                    Player.health = Player.health + 20 
            if self.typer =="Attack_Health":
                    Player.health = Player.health + 30
                    Player.damage = Player.damage +3
                    Player.damageinc = 3
            if self.typer =="item1":
                    Player.damage = Player.damage + 5 
                    Player.item = "item1"
                    Player.itemtexter = "item1.png"
            if self.typer =="item2":
                    Player.damage = Player.damage + 5 
                    Player.item = "item2"
                    Player.itemtexter = "item2.png"
            if self.typer =="item3":
                    Player.damage = Player.damage + 5   
                    Player.item = "item3"
                    Player.itemtexter = "item3.png"
            if self.typer =="item4":
                    Player.damage = Player.damage + 5 
                    Player.item = "item4"
                    Player.itemtexter = "item4.png"
            if self.typer =="item5":
                    Player.damage = Player.damage + 5   
                    Player.item = "item5" 
                    Player.itemtexter = "item5.png"
    def Delt(self):
            destroy(self)        
class Player(Button):
    def __init__(self, position=(0,0), texture = "" ):
            super().__init__(
            parent=scene, color=color.white,  position = position, texture = texture,collision = False
            ) 
            self.item = ""
            self.itemtexter = "ground.png"
            self.damageinc = 0
    def Bar_maker(self, health,damage):
            self.health = health    
            self.damage = damage   
            self.m_health = Bar(self,str(self.health),255,255,255,-1.6,-2)
            self.m_damage = Bar(self,str(self.damage),255,255,255,1.3,-2)
    def Bar_changer(self, health,damage):
            destroy(self.m_health)
            destroy(self.m_damage)
            self.health = health    
            self.damage = damage   
            self.m_health = Bar(self,str(self.health),255,255,255,-1.6,-2)
            self.m_damage = Bar(self,str(self.damage),255,255,255,1.3,-2)
    def Delt(self):
            destroy(self)
class Main_Button(Button):
    def __init__(self, position=(0,0), text = "" ):
            super().__init__(
            parent=scene, color=color.white,  position = position, text = text,collision = True, z= 1
            ) 
    def Delt(self):
            self.collision = False
            self.visible = False
class MainMe:
    def back_button(self):
        self.f = Main_Button(position = (3,2), text = "back")
        self.f.on_click = self.exits
    def exits(self):
        self.f.Delt()
        scene.clear()
        self.Main_menu()
    def Main_menu(self):
        self.a = Main_Button(position = (1,1), text = "start")
        self.b = Main_Button(position = (0,1), text = "setting")
        self.c = Main_Button(position = (2,1), text = "credit")
        #d = Main_Button(position = (1,0), text = "collection")
    def arturn(self):
        self.a.Delt()
        self.b.Delt()
        self.c.Delt()
    def back_button_delete(self):
        self.f.Delt()     
class Item(Button):
    def __init__(self, position=(0,0), text = "" ):
            super().__init__(
            parent=scene, color=color.white,  position = position, text = text,collision = True, z= 1
            ) 