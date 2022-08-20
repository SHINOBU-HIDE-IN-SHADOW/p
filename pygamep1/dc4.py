from ursina import *
import random
app = Ursina()

camera.orthographic = True
camera.fov = 4
camera.position = (1, 1)

player = Button(parent=scene, color=color.red,  position = (1,1), text = "start" )
board = [[None for x in range(3)] for y in range(3)]
player_last = []

for y in range(3):
    for x in range(3):
        b = Button(parent=scene, position=(x,y),collision = False, color = color.white,highlight_color = color.white)
        board[x][y] = b 
        destroy(board[1][1])
        def start(b=b):
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
                
                if player.position == (1,1,0):
                        player.position = (1,1)
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
                player.position = b.position
                player_last.clear()
                player_last.append(player.position)
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
                        destroy(board[0][0])
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
                        destroy(board[0][1])
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
                        destroy(board[0][2])
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
                        destroy(board[1][0])
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
                        destroy(board[1][1])
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
                        destroy(board[1][2])
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
                        destroy(board[2][0])
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
                        destroy(board[2][1])
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
                        destroy(board[2][2])
        b.on_click = on_click
        player.on_click = start
    
   
app.run()