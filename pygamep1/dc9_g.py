from ursina import *
import random
from dc9_1 import *
class Gamer:
        def __init__(self,lx,supertexter,superattck,superhealth,levelmin, levelmax,levelminh, levelmaxh):
                arar = MainMe()
                camera.orthographic = True
                camera.fov = 4
                camera.position = (1, 1)   
                board = [[None for x in range(lx)] for y in range(lx)]
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
                for y in range(lx-1):
                        for x in range(lx-1):
                                global b,boss,itemcount
                                b = Monster(position = (x,y))
                                board[x][y] = b
                                b.collision = False
                                b.visible = False
                                if x == lx-2 and y == lx-2:
                                        Game(b=b)
                                def Game(b=b):
                                        global lperdagame,mainslot,resentitme,increaseper,player1,scorecount,health,player_dmg,boss,itemcount,player_battat,scoredefault,scoreb
                                        lperdagame = 0
                                        increaseper = 0
                                        health = superhealth
                                        player_dmg = superattck
                                        boss =0  
                                        resentitme = ""
                                        player_battat = player_dmg
                                        itemcount = 0 
                                        scoredefault = 0   
                                        scoreb = scoredefault
                                        scorecount = Bar(scene,"score " + str(scoredefault),255,255,255,2,-10) 
                                        scorecount.scale = (10,10)          
                                        score_update()      
                                        player1 = Player(position = (1,1),texture = supertexter)
                                        mainslot = Item(position = (3,2))
                                        mainslot.texture = player1.itemtexter
                                        player1.Bar_maker(health,player_dmg)
                                        for y in range(lx-1):
                                                for x in range(lx-1):  
                                                        board[x][y].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])  
                                                        board[x][y].visible = True
                                                        M_Attack = random.randrange(levelmin, levelmax)
                                                        M_Health = random.randrange(levelminh, levelmaxh) 
                                                        board[x][y].Bar_maker(M_Health,M_Attack)
                                                        board[x][y].typer = "monster"
                                                        board[x][y].name = "monster"
                                                        boss=0
                                        board[1][1].visible = False
                                        block(board[1][1])
                                def on_click(b=b):
                                        global boss
                                        a = player1.position
                                        player_attack(b,a,b=b)    
                                        score_update()
                                        
                                def game_over(a1):
                                        global itemcount,resentitme
                                        if a1.item != resentitme:
                                                if itemcount == 0:                                                         
                                                        resentitme = a1.item
                                                        itemcount = 2
                                                        print(itemcount)
                                                elif a1.item != resentitme and resentitme != "":           
                                                        itemcount = 2
                                        if a1.health <= 1:
                                                a1.collision = True
                                                for y in range(lx-1):
                                                        for x in range(lx-1):  
                                                                board[x][y].collision = False
                                                destroy(a1.m_health)   
                                                a1.health = 0  
                                                a1.m_health = Bar(a1,str(a1.health),255,255,255,-1.6,-2)  
                                def reset(self, key):
                                        global player_battat
                                        if key == 'r':
                                                self.health = 500
                                                self.attack = 20
                                                player_battat = 20
                                                self.Bar_changer(self.health,self.attack)
                                        if self.health <=0:
                                                if key == 'r':  
                                                        destroy(self)
                                                        for y in range(lx-1):
                                                                        for x in range(lx-1):  
                                                                                destroy(board[x][y].m_health)
                                                                                destroy(board[x][y].m_damage) 
                                                        destroy(scorecount)
                                                        destroy(mainslot)
                                                        Game(b=b)
                                                        
                                        if self.health <=0:
                                                if self.hovered:
                                                        if key == 'left mouse down': 
                                                                destroy(self)
                                                                for y in range(lx-1):
                                                                        for x in range(lx-1):  
                                                                                destroy(board[x][y].m_health)
                                                                                destroy(board[x][y].m_damage) 
                                                                destroy(mainslot)
                                                                destroy(scorecount)
                                                                Game(b=b)  
                                                                   
                                def score_update():
                                        global scoreb,scoredefault,scorecount
                                        if scoredefault != scoreb:
                                                destroy(scorecount)
                                                scorecount = Bar(scene,"score " + str(scoredefault),255,255,255,2,-10)  
                                                scorecount.scale = (10,10) 
                                                scoreb = scoredefault
                                                if scoreb >= 10:
                                                        scorecount.origin = (1.75,-10)
                                def slot_update(self):
                                        if itemcount != 0:
                                                mainslot.texture = player1.itemtexter
                                        elif itemcount == 0:
                                                mainslot.texture = "ground.png"
                                b.on_click = on_click
                                Player.update = game_over 
                                Player.input =  reset
                                Item.update = slot_update
                def switch(self,a,boss):
                        global lperdagame,increaseper
                        x = int(self.x)
                        y = int(self.y)  
                        self.visible = False 
                        M_Attack = random.randrange(levelmin, levelmax)
                        M_Health = random.randrange(levelminh, levelmaxh) 
                        M_Attack += increaseper
                        M_Health += increaseper
                        lperdagame += 1
                        print(boss)
                        if lperdagame%10 ==0 and lperdagame != 0:
                                increaseper += 1
                        fromlastm= -2    
                        fromlastp= 0
                        chooser = random.randrange(50, 100)
                        if x-a.x != 0:
                                if x-a.x == -1 and board[x+2][y] != None:
                                        if chooser < 90:
                                                if boss==10:
                                                        board[fromlastm][y].name = random.choice(["boss"])
                                
                                                else:
                                                        board[fromlastm][y].name = random.choice(["monster"])
                                        elif chooser >90:
                                                board[fromlastm][y].name = random.choice(["chest"])
                                if x-a.x == -1 and board[x+2][y] == None:
                                        if chooser < 90:
                                                if boss==10:
                                                        board[fromlastm][y].name = random.choice(["boss"])
                                                       
                                                else:
                                                        board[fromlastm][y].name = random.choice(["monster"])
                                        elif chooser >90:
                                                board[fromlastm][y].name = random.choice(["chest"])
                                if x-a.x == 1 and board[x-2][y] != None:
                                        if chooser < 90:
                                                if boss==10:
                                                        board[fromlastp][y].name = random.choice(["boss"])
                                                        
                                                else:
                                                        board[fromlastp][y].name = random.choice(["monster"])
                                        elif chooser >90:
                                                board[fromlastp][y].name = random.choice(["chest"])
                                if x-a.x == 1 and board[x-2][y] == None:
                                        if chooser < 90:
                                                if boss==10:
                                                        board[fromlastp][y].name = random.choice(["boss"])
                                                        
                                                else:
                                                        board[fromlastp][y].name = random.choice(["monster"])
                                        elif chooser >90:
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
                                                        board[-2][y].Bar_mover(M_Health+6,M_Attack+6)
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
                                        board[-2][y].Bar_mover(M_Health+6,M_Attack+6) 
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
                                                        board[0][y].Bar_mover(M_Health+6,M_Attack+6)
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
                                                while board[x-1][y] != None:
                                                        board[x][y].Bar_mover(board[x-1][y].health,board[x-1][y].damage)
                                                        board[x][y].texture =  board[x-1][y].texture
                                                        board[x][y].typer =  board[x-1][y].typer
                                                        x = x-1
                                        board[0][y].typer ="boss"
                                        board[0][y].Bar_mover(M_Health+6,M_Attack+6) 
                                        board[0][y].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])              
                        if a.y-y != 0:
                                if y-a.y == -1 and board[x][y+2] != None:
                                        if chooser < 90:
                                                if boss==10:
                                                        board[x][fromlastm].name = random.choice(["boss"])
                                                        
                                                        
                                                else:
                                                        board[x][fromlastm].name = random.choice(["monster"])
                                        elif chooser > 90:
                                                board[x][fromlastm].name = random.choice(["chest"])
                                if y-a.y == -1 and board[x][y+2] == None:
                                        if chooser < 90:
                                                if boss==10:
                                                        board[x][fromlastm].name = random.choice(["boss"])
                                                

                                                else:  
                                                        board[x][fromlastm].name = random.choice(["monster"])
                                                        
                                        elif chooser > 90:
                                                board[x][fromlastm].name = random.choice(["chest"])
                                if y-a.y == 1 and board[x][y-2] != None:
                                        if chooser < 90:
                                                if boss==10:
                                                        board[x][fromlastp].name = random.choice(["boss"])
                                                        print(board[x][fromlastp].name)
                                                        
                                                else:
                                                        board[x][fromlastp].name = random.choice(["monster"])
                                        elif chooser > 90:
                                                board[x][fromlastp].name = random.choice(["chest"])
                                if y-a.y == 1 and board[x][y-2] == None:
                                        if chooser <= 90:
                                                if boss==10:
                                                        board[x][fromlastp].name = random.choice(["boss"])                                                   
                                                else:  
                                                        board[x][fromlastp].name = random.choice(["monster"])
                                                        
                                        elif chooser > 90:
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
                                                        board[x][-2].Bar_mover(M_Health+6,M_Attack+6)
                                                        board[x][-2].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
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
                                        board[x][-2].Bar_mover(M_Health+6,M_Attack+6)
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
                                                        board[x][0].Bar_mover(M_Health+6,M_Attack+6)
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
                                        board[x][0].Bar_mover(M_Health+6,M_Attack+6) 
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
                        global boss,itemcount,player_battat,scoredefault
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
                                        if b.typer == "boss":
                                                scoredefault += 5
                                        else: 
                                                scoredefault += 1
                                        if itemcount != 0:
                                                itemcount -= 1   
                                        if itemcount == 1:
                                                player1.damage = player_battat                                                                                       
                                        block(b)    
                                elif self.typer == "chest":
                                        if boss >=10:
                                              boss = boss+1  
                                        self.Open()  
                                elif self.typer != "chest" and self.typer != "monster": 
                                        if player1.item == "":
                                                player_battat = player1.damage 
                                        if player1.item != "":
                                                player1.damage = player_battat
                                        self.Usepotion(player1)
                                        player_battat = player_battat + player1.damageinc
                                        player1.damageinc = 0
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