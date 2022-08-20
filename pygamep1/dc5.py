from ursina import *
import random
app = Ursina()

camera.orthographic = True
camera.fov = 4
camera.position = (1, 1)

board = [[None for x in range(3)] for y in range(3)]

class health_bar(Text):
        def __init__(self,parent,text,r,g,b,ox,oy):
                super().__init__()
                self.parent = parent
                self.color = color.rgb(r,g,b)
                self.text = text
                self.scale = (5,5)
                self.origin = (ox,oy)
                self.z = -2

class monster(Button):
        def __init__(self, position=(0,0)):
                super().__init__(
                parent=scene, position=position,
                        color = color.white,highlight_color = color.white
                )

player = Button(parent=scene, color=color.red,  position = (1,1), text = "start" )  
health = 100
player_bar = health_bar(player,str(health),0,255,255,1.5,-2) 
player_dmg = 10
player_attack = health_bar(player,str(player_dmg),0,255,255,-1.5,-2)
player_bar.visible = False
player_attack.visible = False
for y in range(3):
    for x in range(3):
        b = monster(position = (x,y))
        board[x][y] = b 
        b.collision = False
         
        def start(b=b):
                global text1,text2,text3,text4,text5,text6,text7,text8,text9,damage9,damage1,damage2,damage3,damage4,damage5,damage6,damage7,damage8,health1,health2,health3,health4,health5,health6,health7,health8,health9,mon_health1,mon_health2,mon_health3,mon_health4,mon_health5,mon_health6,mon_health7,mon_health8,mon_health9
                player_bar.visible = True
                player_attack.visible = True
                board[1][1].texture = "ground.png"
                board[1][1].color = color.black 
                player.collision = False
                player.texture = "cover.png" 
                player.text = ""
                player.color = color.white
                player.highlight_color = color.white
                board[0][0].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[0][1].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[0][2].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[1][0].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[1][2].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[2][0].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[2][1].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[2][2].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                
                damage1 = random.randrange(4, 20)
                damage2 = random.randrange(4, 20)
                damage3 = random.randrange(4, 20)
                damage4 = random.randrange(4, 20)
                damage5 = random.randrange(4, 20)
                damage6 = random.randrange(4, 20)
                damage7 = random.randrange(4, 20)
                damage8 = random.randrange(4, 20)
                damage9 = random.randrange(4, 20)

                text1 = health_bar(board[0][0],str(damage1),255,255,255,1.5,-2) 
                text2 = health_bar(board[0][1],str(damage2),255,255,255,1.5,-2) 
                text3 = health_bar(board[0][2],str(damage3),255,255,255,1.5,-2) 
                text4 = health_bar(board[1][0],str(damage4),255,255,255,1.5,-2)
                text5 = health_bar(board[1][1],"",255,255,255,1.5,-2)
                text6 = health_bar(board[1][2],str(damage5),255,255,255,1.5,-2) 
                text7 = health_bar(board[2][0],str(damage6),255,255,255,1.5,-2) 
                text8 = health_bar(board[2][1],str(damage7),255,255,255,1.5,-2) 
                text9= health_bar(board[2][2],str(damage8),255,255,255,1.5,-2) 
                
                health1 = random.randrange(10, 20)
                health2 = random.randrange(10, 20)
                health3 = random.randrange(10, 20)
                health4 = random.randrange(10, 20)
                health5 = random.randrange(10, 20)
                health6 = random.randrange(10, 20)
                health7 = random.randrange(10, 20)
                health8 = random.randrange(10, 20)
                health9 = random.randrange(10, 20)

                mon_health1 = health_bar(board[0][0],str(health1),255,255,255,-1.5,-2) 
                mon_health2 = health_bar(board[0][1],str(health2),255,255,255,-1.5,-2) 
                mon_health3 = health_bar(board[0][2],str(health3),255,255,255,-1.5,-2) 
                mon_health4 = health_bar(board[1][0],str(health4),255,255,255,-1.5,-2)
                mon_health5 = health_bar(board[1][1],"",255,255,255,-1.5,-2)
                mon_health6 = health_bar(board[1][2],str(health6),255,255,255,-1.5,-2) 
                mon_health7 = health_bar(board[2][0],str(health7),255,255,255,-1.5,-2) 
                mon_health8 = health_bar(board[2][1],str(health8),255,255,255,-1.5,-2) 
                mon_health9= health_bar(board[2][2],str(health9),255,255,255,-1.5,-2) 
                if player.position == (1,1,0):
                        player.position = (1,1,0)
                        board[2][2].collision = False
                        board[2][1].collision = True
                        board[2][0].collision = False
                        board[1][2].collision = True
                        board[1][1].collision = True
                        board[1][0].collision = True 
                        board[0][2].collision = False
                        board[0][1].collision = True 
                        board[0][0].collision = False 
        def on_click(b=b):
                global health, player_bar,health1,mon_health1,health2,mon_health2,health3,mon_health3,health4,mon_health4,health5,mon_health5,health6,mon_health6,health7,mon_health7,health8,mon_health8,health9,mon_health9       
                pos('left mouse down',b=b)              
                mover()
                game_over()
                destroy(player_bar)
                player_bar = health_bar(player,str(health),255,255,255,1.5,-2)
        b.on_click = on_click
        player.on_click = start
def mover():

                if player.position == (0,0,0):
                                board[2][2].collision = False  
                                board[2][1].collision = False
                                board[2][0].collision = False 
                                board[1][2].collision = False
                                board[1][1].collision = False
                                board[1][0].collision = True  
                                board[0][2].collision = False
                                board[0][1].collision = True 
                                board[0][0].collision = True
                                
                elif player.position == (0,1,0):
                        board[2][2].collision = False  
                        board[2][1].collision = False
                        board[2][0].collision = False 
                        board[1][2].collision = False
                        board[1][1].collision = True
                        board[1][0].collision = False  
                        board[0][2].collision = True
                        board[0][1].collision = True 
                        board[0][0].collision = True
                        
                elif player.position == (0,2,0):
                        board[2][2].collision = False  
                        board[2][1].collision = False
                        board[2][0].collision = False 
                        board[1][2].collision = True
                        board[1][1].collision = False
                        board[1][0].collision = False 
                        board[0][2].collision = True
                        board[0][1].collision = True 
                        board[0][0].collision = False 
                        
                elif player.position == (1,0,0):
                        board[2][2].collision = False  
                        board[2][1].collision = False
                        board[2][0].collision = True 
                        board[1][2].collision = False
                        board[1][1].collision = True
                        board[1][0].collision = True  
                        board[0][2].collision = False
                        board[0][1].collision = False 
                        board[0][0].collision = True 
                        
                elif player.position == (1,1,0):
                        board[2][2].collision = False
                        board[2][1].collision = True
                        board[2][0].collision = False
                        board[1][2].collision = True
                        board[1][1].collision = True
                        board[1][0].collision = True 
                        board[0][2].collision = False
                        board[0][1].collision = True 
                        board[0][0].collision = False 
                        
                elif player.position == (1,2,0):
                        board[2][2].collision = True  
                        board[2][1].collision = False
                        board[2][0].collision = False 
                        board[1][2].collision = True
                        board[1][1].collision = True
                        board[1][0].collision = False  
                        board[0][2].collision = True
                        board[0][1].collision = False
                        board[0][0].collision = False  
                       
                elif player.position == (2,0,0):
                        board[2][2].collision = False  
                        board[2][1].collision = True
                        board[2][0].collision = True 
                        board[1][2].collision = False
                        board[1][1].collision = False
                        board[1][0].collision = True  
                        board[0][2].collision = False
                        board[0][1].collision = False
                        board[0][0].collision = False 
                       
                elif player.position == (2,1,0):
                        board[2][2].collision = True  
                        board[2][1].collision = True
                        board[2][0].collision = True 
                        board[1][2].collision = False
                        board[1][1].collision = True
                        board[1][0].collision = False 
                        board[0][2].collision = False
                        board[0][1].collision = False
                        board[0][0].collision = False 
        
                elif player.position == (2,2,0):
                        board[2][2].collision = False  
                        board[2][1].collision = True
                        board[2][0].collision = False 
                        board[1][2].collision = True
                        board[1][1].collision = False
                        board[1][0].collision = False 
                        board[0][2].collision = False
                        board[0][1].collision = False
                        board[0][0].collision = False  
def monster_mover():
        global text1,text2,text3,text4,text5,text6,text7,text8,text9,health,damage9,damage1,damage2,damage3,damage4,damage5,damage6,damage7,damage8,health1,mon_health1,health2,mon_health2,health3,mon_health3,health4,mon_health4,health5,mon_health5,health6,mon_health6,health7,mon_health7,health8,mon_health8,health9,mon_health9
        if board[1][1].color == color.black and player.position == (1,2,0) :              
                destroy(text5)
                destroy(text6)     
                mon_health5 = health_bar(board[1][1],str(health5),255,255,255,-1.5,-2) 
                text5 = health_bar(board[1][1],str(text4.text),255,255,255,1.5,-2)
                damage9 = damage4
                destroy(text4)
                damage4 =random.randrange(4, 20)
                text4 = health_bar(board[1][0],str(damage4),255,255,255,1.5,-2)
                health = health - damage5
                board[1][1].texture = board[1][0].texture
                board[1][0].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[1][1].color = color.white               
        if board[1][1].color == color.black and player.position == (1,0,0) :
                board[1][1].texture = board[1][2].texture
                board[1][2].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[1][1].color = color.white
                destroy(text4)
                destroy(text5)
                mon_health5 = health_bar(board[1][1],str(health5),255,255,255,-1.5,-2)
                text5 = health_bar(board[1][1],str(text6.text),255,255,255,1.5,-2)
                damage9 = damage5
                destroy(text6)
                damage6 =random.randrange(4, 20)
                text6 = health_bar(board[1][2],str(damage6),255,255,255,1.5,-2)
                health = health - damage4
        if board[1][1].color == color.black and player.position == (0,1,0) :
                board[1][1].texture = board[2][1].texture
                board[2][1].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[1][1].color = color.white
                destroy(text2)
                destroy(text5)
                mon_health5 = health_bar(board[1][1],str(health5),255,255,255,-1.5,-2)
                text5 = health_bar(board[1][1],str(text8.text),255,255,255,1.5,-2)
                damage9 = damage7
                destroy(text8)
                damage7 =random.randrange(4, 20)
                text8 = health_bar(board[2][1],str(damage7),255,255,255,1.5,-2)
                health = health - damage2 
        if board[1][1].color == color.black and player.position == (2,1,0) :
                board[1][1].texture = board[0][1].texture
                board[0][1].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[1][1].color = color.white
                destroy(text8)
                destroy(text5)
                mon_health5 = health_bar(board[1][1],str(health5),255,255,255,-1.5,-2)
                text5 = health_bar(board[1][1],str(text2.text),255,255,255,1.5,-2)
                damage9 = damage2
                destroy(text2)
                damage2 =random.randrange(4, 20)
                text2 = health_bar(board[0][1],str(damage2),255,255,255,1.5,-2) 
                health = health - damage7
        if board[0][1].color == color.black and player.position == (0,2,0) :
                board[0][1].texture = board[0][0].texture
                board[0][0].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[0][1].color = color.white
                destroy(text3)
                destroy(text2)
                mon_health2 = health_bar(board[0][1],str(health2),255,255,255,-1.5,-2)
                text2 = health_bar(board[0][1],str(text1.text),255,255,255,1.5,-2)
                damage2 = damage1
                destroy(text1)
                damage1 =random.randrange(4, 20)
                text1 = health_bar(board[0][0],str(damage1),255,255,255,1.5,-2) 
                health = health - damage3
        if board[0][1].color == color.black and player.position == (0,0,0) :
                board[0][1].texture = board[0][2].texture
                board[0][2].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[0][1].color = color.white
                destroy(text1)
                destroy(text2)
                mon_health2 = health_bar(board[0][1],str(health2),255,255,255,-1.5,-2)
                text2 = health_bar(board[0][1],str(text3.text),255,255,255,1.5,-2)
                damage2 = damage3
                destroy(text3)
                damage3 =random.randrange(4, 20)
                text3 = health_bar(board[0][2],str(damage3),255,255,255,1.5,-2) 
                health = health - damage1
        if board[1][2].color == color.black and player.position == (0,2,0) :
                board[1][2].texture = board[2][2].texture
                board[2][2].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[1][2].color = color.white
                destroy(text6)
                destroy(text3)
                mon_health6 = health_bar(board[1][2],str(health6),255,255,255,-1.5,-2)
                text6 = health_bar(board[1][2],str(text9.text),255,255,255,1.5,-2)
                damage5 = damage8
                destroy(text9)
                damage8 =random.randrange(4, 20)
                text9 = health_bar(board[2][2],str(damage8),255,255,255,1.5,-2)
                health = health - damage3 
        if board[1][2].color == color.black and player.position == (2,2,0) :
                board[1][2].texture = board[0][2].texture
                board[1][2].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[1][2].color = color.white
                destroy(text9)
                destroy(text6)
                mon_health6 = health_bar(board[1][2],str(health6),255,255,255,-1.5,-2)
                text6 = health_bar(board[1][2],str(text3.text),255,255,255,1.5,-2)
                damage5 = damage3
                destroy(text3)
                damage3 =random.randrange(4, 20)
                text3 = health_bar(board[0][2],str(damage3),255,255,255,1.5,-2) 
                health = health - damage8       
        if board[2][1].color == color.black and player.position == (2,2,0) :
                board[2][1].texture = board[2][0].texture
                board[2][0].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[2][1].color = color.white
                destroy(text9)
                destroy(text8)
                mon_health8 = health_bar(board[2][1],str(health8),255,255,255,-1.5,-2)
                text8 = health_bar(board[2][1],str(text7.text),255,255,255,1.5,-2)
                damage7 = damage6
                destroy(text7)
                damage6 =random.randrange(4, 20)
                text7 = health_bar(board[2][0],str(damage6),255,255,255,1.5,-2) 
                health = health - damage8  
        if board[2][1].color == color.black and player.position == (2,0,0) :
                board[2][1].texture = board[2][2].texture
                board[2][2].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[2][1].color = color.white
                destroy(text7)
                destroy(text8)
                mon_health8 = health_bar(board[2][1],str(health8),255,255,255,-1.5,-2)
                text8 = health_bar(board[2][1],str(text9.text),255,255,255,1.5,-2)
                damage7 = damage8
                destroy(text9)
                damage8 =random.randrange(4, 20)
                text9 = health_bar(board[2][2],str(damage8),255,255,255,1.5,-2)
                health = health - damage6   
        if board[1][0].color == color.black and player.position == (0,0,0) :
                board[1][0].texture = board[2][0].texture
                board[2][0].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[1][0].color = color.white
                destroy(text1)
                destroy(text4)
                mon_health4 = health_bar(board[1][0],str(health4),255,255,255,-1.5,-2)
                text4 = health_bar(board[1][0],str(text7.text),255,255,255,1.5,-2)
                damage4 = damage6
                destroy(text7)
                damage6 =random.randrange(4, 20)
                text7 = health_bar(board[2][0],str(damage6),255,255,255,1.5,-2)
                health = health - damage1   
        if board[1][0].color == color.black and player.position == (2,0,0) :
                board[1][0].texture = board[0][0].texture
                board[0][0].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[1][0].color = color.white
                destroy(text7)
                destroy(text4)
                mon_health4 = health_bar(board[1][0],str(health4),255,255,255,-1.5,-2)
                text4 = health_bar(board[1][0],str(text1.text),255,255,255,1.5,-2)
                damage4 = damage1
                destroy(text1)
                damage1 =random.randrange(4, 20)
                text1 = health_bar(board[0][0],str(damage1),255,255,255,1.5,-2)
                health = health - damage6   
        if board[0][2].color == color.black and player.position == (1,2,0) :
                board[0][2].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[0][2].color = color.white
                destroy(text6)
                destroy(text3)
                mon_health3 = health_bar(board[0][2],str(health3),255,255,255,-1.5,-2)
                damage3 =random.randrange(4, 20)
                text3 = health_bar(board[0][2],str(damage3),255,255,255,1.5,-2)   
                health = health - damage5
        if board[0][2].color == color.black and player.position == (0,1,0) :
                board[0][2].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[0][2].color = color.white
                destroy(text2)
                destroy(text3)
                mon_health3 = health_bar(board[0][2],str(health3),255,255,255,-1.5,-2)
                damage3 =random.randrange(4, 20)
                text3 = health_bar(board[0][2],str(damage3),255,255,255,1.5,-2)
                health = health - damage2  
        if board[2][2].color == color.black and player.position == (1,2,0) :
                board[2][2].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[2][2].color = color.white
                destroy(text6)
                destroy(text9)
                mon_health9 = health_bar(board[2][2],str(health9),255,255,255,-1.5,-2)
                damage8 =random.randrange(4, 20)
                text9 = health_bar(board[2][2],str(damage8),255,255,255,1.5,-2)
                health = health - damage6  
        if board[2][2].color == color.black and player.position == (2,1,0) :
                board[2][2].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[2][2].color = color.white
                destroy(text8)
                destroy(text9)
                mon_health9 = health_bar(board[2][2],str(health9),255,255,255,-1.5,-2)
                damage8 =random.randrange(4, 20)
                text9 = health_bar(board[2][2],str(damage8),255,255,255,1.5,-2)
                health = health - damage7   
        if board[2][0].color == color.black and player.position == (2,1,0) :
                board[2][0].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[2][0].color = color.white
                destroy(text7)
                destroy(text8)
                mon_health7 = health_bar(board[2][0],str(health7),255,255,255,-1.5,-2)
                damage6 =random.randrange(4, 20)
                text7 = health_bar(board[2][0],str(damage6),255,255,255,1.5,-2)
                health = health - damage7    
        if board[2][0].color == color.black and player.position == (1,0,0) :
                board[2][0].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[2][0].color = color.white
                destroy(text7)
                destroy(text4)
                mon_health7 = health_bar(board[2][0],str(health7),255,255,255,-1.5,-2)
                damage6 =random.randrange(4, 20)
                text7 = health_bar(board[2][0],str(damage6),255,255,255,1.5,-2)
                health = health - damage4 
        if board[0][0].color == color.black and player.position == (0,1,0) :
                board[0][0].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[0][0].color = color.white
                destroy(text1)
                destroy(text2)
                mon_health1 = health_bar(board[0][0],str(health1),255,255,255,-1.5,-2)
                damage1 =random.randrange(4, 20)
                text1 = health_bar(board[0][0],str(damage1),255,255,255,1.5,-2)
                health = health - damage2   
        if board[0][0].color == color.black and player.position == (1,0,0) :
                board[0][0].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[0][0].color = color.white
                destroy(text1)
                destroy(text4)
                mon_health1 = health_bar(board[0][0],str(health1),255,255,255,-1.5,-2)
                damage1 =random.randrange(4, 20)
                text1= health_bar(board[0][0],str(damage1),255,255,255,1.5,-2)
                health = health - damage4     
        if board[2][1].color == color.black and player.position == (1,1,0) :
                board[2][1].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[2][1].color = color.white
                destroy(text5)
                destroy(text8)
                mon_health8 = health_bar(board[2][1],str(health8),255,255,255,-1.5,-2)
                damage7 =random.randrange(4, 20)
                text8 = health_bar(board[2][1],str(damage7),255,255,255,1.5,-2)
                health = health - damage9    
        if board[1][2].color == color.black and player.position == (1,1,0) :
                board[1][2].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[1][2].color = color.white
                destroy(text6)
                destroy(text5)
                mon_health6 = health_bar(board[1][2],str(health6),255,255,255,-1.5,-2)
                damage5 =random.randrange(4, 20)
                text6 = health_bar(board[1][2],str(damage5),255,255,255,1.5,-2)
                health = health - damage9    
        if board[1][0].color == color.black and player.position == (1,1,0) :
                board[1][0].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[1][0].color = color.white
                destroy(text4)
                destroy(text5)
                mon_health4 = health_bar(board[1][0],str(health4),255,255,255,-1.5,-2)
                damage4 = random.randrange(4, 20)
                text4 = health_bar(board[1][0],str(damage4),255,255,255,1.5,-2)
                health = health - damage9   
        if board[0][1].color == color.black and player.position == (1,1,0) :
                board[0][1].texture = random.choice(["m1.png","m2.png","m3.png","m4.png","m5.png"])
                board[0][1].color = color.white
                destroy(text2)
                destroy(text5)
                mon_health2 = health_bar(board[0][1],str(health2),255,255,255,-1.5,-2)
                damage2 =random.randrange(4, 20)
                text2 = health_bar(board[0][1],str(damage2),255,255,255,1.5,-2)
                health = health - damage9  
def game_over():
        global health
        if health < 1 :
                player.texture = 'ground.png'
                player.text = "game over"
                board[2][2].collision = False
                board[2][1].collision = False
                board[2][0].collision = False
                board[1][2].collision = False
                board[1][1].collision = False
                board[1][0].collision = False 
                board[0][2].collision = False
                board[0][1].collision = False 
                board[0][0].collision = False  
def pos(key,b=b):
        global health,health1,mon_health1,health2,mon_health2,health3,mon_health3,health4,mon_health4,health5,mon_health5,health6,mon_health6,health7,mon_health7,health8,mon_health8,health9,mon_health9
        if board[0][0].hovered:
            if key == 'left mouse down': 
                    destroy(mon_health1)
                    health1 -= player_dmg    
                    mon_health1 = health_bar(board[0][0],str(health1),255,255,255,-1.5,-2) 
                    if health1 < 1:
                                health2 = random.randrange(10, 20)
                                destroy(mon_health1)
                                player.position = b.position
                                monster_mover()
                                b.color = color.black
                                b.texture = "ground.png" 
                
                    else:
                                health -= damage1                            
        if board[0][1].hovered:
            if key == 'left mouse down':
                    destroy(mon_health2)
                    health2 -= player_dmg    
                    mon_health2 = health_bar(board[0][1],str(health2),255,255,255,-1.5,-2) 
                    if health2 < 1:
                                health2 = random.randrange(10, 20)
                                destroy(mon_health2)
                                player.position = b.position
                                monster_mover()
                                b.color = color.black
                                b.texture = "ground.png" 
                    else:
                                health -= damage2           
        if board[0][2].hovered:
            if key == 'left mouse down': 
                    destroy(mon_health3)
                    health3 -= player_dmg    
                    mon_health3 = health_bar(board[0][2],str(health3),255,255,255,-1.5,-2) 
                    if health3 < 1:
                                health3 = random.randrange(10, 20)
                                destroy(mon_health3)
                                player.position = b.position
                                monster_mover()
                                b.color = color.black
                                b.texture = "ground.png" 
                    else:
                                health -= damage3         
        if board[1][0].hovered:
            if key == 'left mouse down':
                    destroy(mon_health4)
                    health4 -= player_dmg    
                    mon_health4 = health_bar(board[1][0],str(health4),255,255,255,-1.5,-2) 
                    if health4 < 1:
                                health4 = random.randrange(10, 20)
                                destroy(mon_health4)
                                player.position = b.position
                                monster_mover()
                                b.color = color.black
                                b.texture = "ground.png" 
                    else:
                                health -= damage4      
        if board[1][1].hovered:
            if key == 'left mouse down': 
                    destroy(mon_health5)
                    health5 -= player_dmg    
                    mon_health5 = health_bar(board[1][1],str(health5),255,255,255,-1.5,-2) 
                    if health5 < 1:
                                health5 = random.randrange(10, 20)
                                destroy(mon_health5)
                                player.position = b.position
                                monster_mover()
                                b.color = color.black
                                b.texture = "ground.png" 
                    else:
                                health -= damage9                 
        if board[1][2].hovered:
            if key == 'left mouse down':
                    destroy(mon_health6)
                    health6 -= player_dmg    
                    mon_health6 = health_bar(board[1][2],str(health6),255,255,255,-1.5,-2) 
                    if health6 < 1:
                                health6 = random.randrange(10, 20)
                                destroy(mon_health6)
                                player.position = b.position
                                monster_mover()
                                b.color = color.black
                                b.texture = "ground.png" 
                    else:
                                health -= damage5     
        if board[2][0].hovered:
            if key == 'left mouse down': 
                    destroy(mon_health7)
                    health7 -= player_dmg    
                    mon_health7 = health_bar(board[2][0],str(health7),255,255,255,-1.5,-2) 
                    if health7 < 1:
                                health7 = random.randrange(10, 20)
                                destroy(mon_health7)
                                player.position = b.position
                                monster_mover()
                                b.color = color.black
                                b.texture = "ground.png" 
                    else:
                                health -= damage6     
                                     
        if board[2][1].hovered:
            if key == 'left mouse down':
                    destroy(mon_health8)
                    health8 -= player_dmg    
                    mon_health8 = health_bar(board[2][1],str(health8),255,255,255,-1.5,-2) 
                    if health8 < 1:
                                health8 = random.randrange(10, 20)
                                destroy(mon_health8)
                                player.position = b.position
                                monster_mover()
                                b.color = color.black
                                b.texture = "ground.png" 
                    else:
                                health -= damage7                 
        if board[2][2].hovered:
            if key == 'left mouse down':
                    destroy(mon_health9)
                    health9 -= player_dmg    
                    mon_health9 = health_bar(board[2][2],str(health9),255,255,255,-1.5,-2) 
                    if health9 < 1:
                                health9 = random.randrange(10, 20)
                                destroy(mon_health9)
                                player.position = b.position
                                monster_mover()
                                b.color = color.black
                                b.texture = "ground.png" 
                    else:
                                health -= damage8    
                
app.run()