from ursina import *
import random
from dc9_1 import *
class Gamer:
        def __init__(self,lx):
                arar = MainMe()
                camera.orthographic = True
                camera.fov = 4
                camera.position = (1, 1)   
                board = [[None for x in range(lx)] for y in range(lx)]
                start  = Main_Button(position = (1,1), text = "start")
                right = Main_Button(position = (2,1), text = "right")
                left = Main_Button(position = (0,1), text = "left")
                for y in range(lx-1):
                        for x in range(lx-1):
                                global b,boss
                                b = Monster(position = (x,y))
                                board[x][y] = b
                                b.collision = False
                                b.visible = False 
                                boss =0
                                def Game(b=b):
                                        global player1,health,player_dmg,boss
                                        destroy(start)
                                        destroy(right)
                                        destroy(left)                                        
                                        health = 100
                                        player_dmg = 10
                                        player1 = Player(position = (1,1),texture ="cover.png")
                                        player1.Bar_maker(health,player_dmg)
                                        for y in range(lx-1):
                                                for x in range(lx-1):  
                                                        board[x][y].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])  
                                                        board[x][y].visible = True
                                                        M_Attack = random.randrange(1, 10)
                                                        M_Health = random.randrange(10, 20) 
                                                        board[x][y].Bar_maker(M_Health,M_Attack)
                                                        board[x][y].typer = "monster"
                                                        board[x][y].name = "monster"
                                                        boss=0
                                        board[1][1].visible = False
                                        block(board[1][1])
                                def on_click(b=b):
                                        global boss
                                        a = player1.position
                                        if b.typer == "boss":
                                                player1.health = 0
                                                b.texture = "ground.png"
                                        player_attack(b,a,b=b)   
                                        game_over(player1) 
                                def game_over(a1):
                                        if a1.health <= 1:
                                                a1.collision = True
                                                for y in range(lx-1):
                                                        for x in range(lx-1):  
                                                                board[x][y].collision = False
                                                destroy(a1.m_health)   
                                                a1.health = 0  
                                                a1.m_health = Bar(a1,str(a1.health),255,255,255,-1.6,-2)  
                                def reset(self, key):
                                        if self.health <=0:
                                                if key == 'r':  
                                                        destroy(self)
                                                        for y in range(lx-1):
                                                                        for x in range(lx-1):  
                                                                                destroy(board[x][y].m_health)
                                                                                destroy(board[x][y].m_damage) 
                                                        Game(b=b)
                                        if self.health <=0:
                                                if self.hovered:
                                                        if key == 'left mouse down': 
                                                                destroy(self)
                                                                for y in range(lx-1):
                                                                        for x in range(lx-1):  
                                                                                destroy(board[x][y].m_health)
                                                                                destroy(board[x][y].m_damage) 
                                                                Game(b=b)                              
                                b.on_click = on_click
                                start.on_click = Game 
                                Player.update = game_over 
                                Player.input =  reset   
                                                   
                def block(self):
                        x = int(self.x)
                        y = int(self.y)           
                        for y1 in range(lx-1):
                                for x1 in range(lx-1):
                                        board[x1][y1].collision = False
                        if board[x+1][y] != None:
                                board[x+1][y].collision = True
                        if board[x][y+1] != None:
                                board[x][y+1].collision = True
                        if board[x-1][y] != None:
                                board[x-1][y].collision = True
                        if board[x][y-1] != None:
                                board[x][y-1].collision = True
                def switch(self,a,boss):
                        x = int(self.x)
                        y = int(self.y)  
                        self.visible = False 
                        M_Attack = random.randrange(1, 10)
                        M_Health = random.randrange(10, 20) 
                        fromlastm= -2    
                        fromlastp= 0
                        chooser = random.randrange(0, 100)
                        print(boss)
                        if x-a.x != 0:
                                if x-a.x == -1 and board[x+2][y] != None:
                                        if chooser <= 90:
                                                if boss==10:
                                                        board[fromlastm][y].name = random.choice(["boss"])
                                
                                                else:
                                                        board[fromlastm][y].name = random.choice(["monster"])
                                        elif chooser >=90:
                                                board[fromlastm][y].name = random.choice(["chest"])
                                if x-a.x == -1 and board[x+2][y] == None:
                                        if chooser <= 90:
                                                if boss==10:
                                                        board[fromlastm][y].name = random.choice(["boss"])
                                                       
                                                else:
                                                        board[fromlastm][y].name = random.choice(["monster"])
                                        elif chooser >=90:
                                                board[fromlastm][y].name = random.choice(["chest"])
                                if x-a.x == 1 and board[x-2][y] != None:
                                        if chooser <= 90:
                                                if boss==10:
                                                        board[fromlastp][y].name = random.choice(["boss"])
                                                        
                                                else:
                                                        board[fromlastp][y].name = random.choice(["monster"])
                                        elif chooser >=90:
                                                board[fromlastp][y].name = random.choice(["chest"])
                                if x-a.x == 1 and board[x-2][y] == None:
                                        if chooser <= 90:
                                                if boss==10:
                                                        board[fromlastp][y].name = random.choice(["boss"])
                                                        
                                                else:
                                                        board[fromlastp][y].name = random.choice(["monster"])
                                        elif chooser >=90:
                                                board[fromlastp][y].name = random.choice(["chest"])

                                #### to left
                                try:
                                                if x-a.x == -1 and board[x+2][y] == None and board[x+1][y].name == "monster":
                                                        board[-2][y].Bar_mover(M_Health,M_Attack)
                                                        board[-2][y].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])  
                                                        board[-2][y].typer = "monster"
                                                if x-a.x == -1 and board[x+2][y] == None and board[x+1][y].name == "chest":
                                                        board[-2][y].Bar_mover(10,0)
                                                        board[-2][y].texture = "chest1.png"
                                                        board[-2][y].typer = "chest"
                                                if x-a.x == -1 and board[x+2][y] == None and board[x+1][y].name == "boss":
                                                        board[-2][y].Bar_mover(1,1)
                                                        board[-2][y].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])  
                                                        board[-2][y].typer = "boss"
                                except:
                                                if x-a.x == -1 and board[x+1][y] == None and board[x+1][y].name == "monster":
                                                        print("edge")
                                                if x-a.x == -1 and board[x+1][y] == None and board[x+1][y].name == "chest":
                                                        print("edge")
                                if x-a.x == -1 and board[x+2][y] != None and board[x+2][y].name == "monster" :   
                                        if board[x][y] != None:
                                                while board[x+1][y] != None:
                                                        board[x][y].Bar_mover(board[x+1][y].health,board[x+1][y].damage)
                                                        board[x][y].texture =  board[x+1][y].texture
                                                        board[x][y].typer =  board[x+1][y].typer
                                                        x = x+1
                                        board[-2][y].typer ="monster"
                                        board[-2][y].Bar_mover(M_Health,M_Attack) 
                                        board[-2][y].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                                if x-a.x == -1 and board[x+2][y] != None and board[x+2][y].name == "boss" :   
                                        if board[x][y] != None:
                                                while board[x+1][y] != None:
                                                        board[x][y].Bar_mover(board[x+1][y].health,board[x+1][y].damage)
                                                        board[x][y].texture =  board[x+1][y].texture
                                                        board[x][y].typer =  board[x+1][y].typer
                                                        x = x+1
                                        board[-2][y].typer ="boss"
                                        board[-2][y].Bar_mover(1,1) 
                                        board[-2][y].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                                if x-a.x == -1 and board[x+2][y] != None and board[x+2][y].name == "chest" :  
                                        if board[x][y] != None:
                                                while board[x+1][y] != None:
                                                        board[x][y].Bar_mover(board[x+1][y].health,board[x+1][y].damage)
                                                        board[x][y].texture =  board[x+1][y].texture
                                                        board[x][y].typer =  board[x+1][y].typer
                                                        x = x+1
                                        board[-2][y].typer = "chest"
                                        board[-2][y].Bar_mover(10,0) 
                                        board[-2][y].texture = "chest1.png" 

                        #### to right
                                try:
                                                if x-a.x == 1 and board[x-2][y] == None and board[x-1][y].name == "monster":
                                                        board[0][y].Bar_mover(M_Health,M_Attack)
                                                        board[0][y].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                                                        board[0][y].typer = "monster"
                                                if x-a.x == 1 and board[x-2][y] == None and board[x-1][y].name == "chest":
                                                        board[0][y].Bar_mover(10,0)
                                                        board[0][y].texture = "chest1.png"
                                                        board[0][y].typer = "chest"
                                                if x-a.x == 1 and board[x-2][y] == None and board[x-1][y].name == "boss":
                                                        board[0][y].Bar_mover(1,1)
                                                        board[0][y].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])  
                                                        board[0][y].typer = "boss"
                                except:
                                                if x-a.x == 1 and board[x-1][y] == None and board[x-1][y].name == "monster":
                                                        print("edge")
                                if x-a.x == 1 and board[x-2][y] != None and board[x-2][y].name == "monster" :   
                                        if board[x][y] != None:
                                                while board[x-1][y] != None:
                                                        board[x][y].Bar_mover(board[x-1][y].health,board[x-1][y].damage)
                                                        board[x][y].texture =  board[x-1][y].texture
                                                        board[x][y].typer =  board[x-1][y].typer
                                                        x = x-1                                  
                                        board[0][y].typer="monster"
                                        board[0][y].Bar_mover(M_Health,M_Attack)  
                                        board[0][y].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                                
                                if x-a.x == 1 and board[x-2][y] != None and board[x-2][y].name == "chest" :   
                                        if board[x][y] != None:
                                                while board[x-1][y] != None:
                                                        board[x][y].Bar_mover(board[x-1][y].health,board[x-1][y].damage)
                                                        board[x][y].texture =  board[x-1][y].texture
                                                        board[x][y].typer =  board[x-1][y].typer
                                                        x = x-1       
                                        board[0][y].typer="chest"
                                        board[0][y].Bar_mover(10,0) 
                                        board[0][y].texture = "chest1.png" 
                                if x-a.x == 1 and board[x-2][y] != None and board[x-2][y].name == "boss" :   
                                        if board[x][y] != None:
                                                while board[x+1][y] != None:
                                                        board[x][y].Bar_mover(board[x-1][y].health,board[x-1][y].damage)
                                                        board[x][y].texture =  board[x-1][y].texture
                                                        board[x][y].typer =  board[x-1][y].typer
                                                        x = x+1
                                        board[-2][y].typer ="boss"
                                        board[-2][y].Bar_mover(1,1) 
                                        board[-2][y].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])              
                        if a.y-y != 0:
                                if y-a.y == -1 and board[x][y+2] != None:
                                        if chooser <= 90:
                                                if boss==10:
                                                        board[x][fromlastm].name = random.choice(["boss"])
                                                        print(board[x][fromlastm].name)
                                                        
                                                else:
                                                        board[x][fromlastm].name = random.choice(["monster"])
                                        elif chooser >= 90:
                                                board[x][fromlastm].name = random.choice(["chest"])
                                elif y-a.y == -1 and board[x][y+2] == None:
                                        if chooser <= 90:
                                                if boss==10:
                                                        board[x][fromlastm].name = random.choice(["boss"])
                                                        print(board[x][fromlastm].name)
                                                else:  
                                                        board[x][fromlastm].name = random.choice(["monster"])
                                                        
                                        elif chooser >= 90:
                                                board[x][fromlastm].name = random.choice(["chest"])
                                if y-a.y == 1 and board[x][y-2] != None:
                                        if chooser <= 90:
                                                if boss==10:
                                                        board[x][fromlastp].name = random.choice(["boss"])
                                                        print(board[x][fromlastp].name)
                                                        
                                                else:
                                                        board[x][fromlastp].name = random.choice(["monster"])
                                        elif chooser >= 90:
                                                board[x][fromlastp].name = random.choice(["chest"])
                                elif y-a.y == 1 and board[x][y-2] == None:
                                        if chooser <= 90:
                                                if boss==10:
                                                        board[x][fromlastp].name = random.choice(["boss"])
                                                        print(board[x][fromlastp].name)
                                                else:  
                                                        board[x][fromlastp].name = random.choice(["monster"])
                                                        
                                        elif chooser >= 90:
                                                board[x][fromlastp].name = random.choice(["chest"])
                                #### to up
                                try:
                                                if y-a.y == -1 and board[x][y+2] == None and board[x][y+1].name == "monster":
                                                        board[x][-2].Bar_mover(M_Health,M_Attack)
                                                        board[x][-2].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                                                        board[x][-2].typer = "monster"
                                                if y-a.y == -1 and board[x][y+2] == None and board[x][y+1].name == "chest":
                                                        board[x][-2].Bar_mover(10,0)
                                                        board[x][-2].texture = "chest1.png"
                                                        board[x][-2].typer = "chest"
                                                if y-a.y == -1 and board[x][y+2] == None and board[x][y+1].name == "boss":
                                                        board[x][-2].Bar_mover(1,1)
                                                        board[x][-2].texture = "chest1.png"
                                                        board[x][-2].typer = "boss"
                                except:
                                                if y-a.y == -1 and board[x][y+1] == None and board[x][y+1].name == "monster":
                                                        print("edge")
                                if y-a.y == -1 and board[x][y+2] != None and board[x][y+2].name == "monster" :   
                                        if board[x][y] != None:
                                                while board[x][y+1] != None:
                                                        board[x][y].Bar_mover(board[x][y+1].health,board[x][y+1].damage)
                                                        board[x][y].texture =  board[x][y+1].texture
                                                        board[x][y].typer =  board[x][y+1].typer
                                                        y= y+1
                                        board[x][-2].typer = "monster" 
                                        board[x][-2].Bar_mover(M_Health,M_Attack)
                                        board[x][-2].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"]) 
                                if y-a.y == -1 and board[x][y+2] != None and board[x][y+2].name == "boss" :   
                                        if board[x][y] != None:
                                                while board[x][y+1] != None:
                                                        board[x][y].Bar_mover(board[x][y+1].health,board[x][y+1].damage)
                                                        board[x][y].texture =  board[x][y+1].texture
                                                        board[x][y].typer =  board[x][y+1].typer
                                                        y= y+1
                                        board[x][-2].typer = "boss" 
                                        board[x][-2].Bar_mover(1,1)
                                        board[x][-2].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"]) 
                                
                                if y-a.y == -1 and board[x][y+2] != None and board[x][y+2].name == "chest" :   
                                        if board[x][y] != None:
                                                while board[x][y+1] != None:
                                                        board[x][y].Bar_mover(board[x][y+1].health,board[x][y+1].damage)
                                                        board[x][y].texture =  board[x][y+1].texture
                                                        board[x][y].typer =  board[x][y+1].typer
                                                        y = y+1
                                        board[x][-2].typer = "chest"
                                        board[x][-2].Bar_mover(10,0) 
                                        board[x][-2].texture = "chest1.png"               
                        #### to down
                                try:
                                                if y-a.y == 1 and board[x][y-2] == None and board[x][y-1].name == "monster":
                                                        board[x][0].Bar_mover(M_Health,M_Attack)
                                                        board[x][0].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                                                        board[x][0].typer = "monster"
                                                if y-a.y == 1 and board[x][y-2] == None and board[x][y-1].name == "chest":
                                                        board[x][0].Bar_mover(10,0)
                                                        board[x][0].texture = "chest1.png"
                                                        board[x][0].typer = "chest"
                                                if y-a.y == 1 and board[x][y-2] == None and board[x][y-1].name == "boss":
                                                        board[x][0].Bar_mover(1,1)
                                                        board[x][0].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                                                        board[x][0].typer = "boss"
                                except:
                                                if y-a.y == 1 and board[x][y-1] == None and board[x][y-1].name == "monster":
                                                        print("edge")
                                if y-a.y == 1 and board[x][y-2] != None and board[x][y-2].name == "monster" :   
                                        if board[x][y] != None:
                                                while board[x][y-1] != None:
                                                        board[x][y].Bar_mover(board[x][y-1].health,board[x][y-1].damage)
                                                        board[x][y].texture =  board[x][y-1].texture
                                                        board[x][y].typer =  board[x][y-1].typer
                                                        y= y-1 
                                        board[x][0].typer = "monster"  
                                        board[x][0].Bar_mover(M_Health,M_Attack) 
                                        board[x][0].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                                if y-a.y == 1 and board[x][y-2] != None and board[x][y-2].name == "boss" :   
                                        if board[x][y] != None:
                                                while board[x][y-1] != None:
                                                        board[x][y].Bar_mover(board[x][y-1].health,board[x][y-1].damage)
                                                        board[x][y].texture =  board[x][y-1].texture
                                                        board[x][y].typer =  board[x][y-1].typer
                                                        y= y-1 
                                        board[x][0].typer = "boss"  
                                        board[x][0].Bar_mover(1,1) 
                                        board[x][0].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                                if y-a.y == 1 and board[x][y-2] != None and board[x][y-2].name == "chest" :   
                                        if board[x][y] != None:
                                                while board[x][y-1] != None:
                                                        board[x][y].Bar_mover(board[x][y-1].health,board[x][y-1].damage)
                                                        board[x][y].texture =  board[x][y-1].texture
                                                        board[x][y].typer =  board[x][y-1].typer
                                                        y = y-1 
                                        board[x][0].typer = "chest"
                                        board[x][0].Bar_mover(10,0) 
                                        board[x][0].texture = "chest1.png"   
                def player_attack(self,a,b=b):
                        global boss
                        player1.health=player1.health-self.damage
                        player1.Bar_changer(player1.health,player1.damage)
                        
                        if self.health <= player1.damage:
                                pox = int(a.x)
                                poy = int(a.y)
                                if self.typer == "monster":
                                        board[pox][poy].visible = True 
                                        board[pox][poy].name = "monster"
                                        board[pox][poy].typer = "monster"
                                        b.name = "player"           
                                        player1.position = b.position
                                        pnx = int(player1.x)
                                        pny = int(player1.y)
                                        board[pnx][pny].collision = False  
                                        boss = boss+1
                                        switch(b,a,boss) 
                                        block(b)    
                                elif self.typer == "chest":
                                        if boss >=10:
                                              boss = boss+1  
                                        self.Open()  
                                elif self.typer != "chest" and self.typer != "monster":
                                        self.Use(player1)
                                        print(self.typer,self.position)
                                        boss = boss+1
                                        player1.Bar_changer(player1.health,player1.damage)
                                        board[pox][poy].visible = True 
                                        board[pox][poy].name = "monster"
                                        board[pox][poy].typer = "monster"
                                        b.name = "player"           
                                        player1.position = b.position 
                                        pnx = int(player1.x)
                                        pny = int(player1.y)
                                        board[pnx][pny].collision = False  
                                        switch(b,a,boss) 
                                        block(b)   
                                
                        self.health = self.health - player1.damage 
                        self.Bar_mover(self.health,self.damage)