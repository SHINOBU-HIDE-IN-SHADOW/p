from ursina import *
import random
from dc9_g import Gamer 
from dc9_1 import MainMe,Main_Button
from dc9_2 import Setting
from dc9_3 import Credit
#from dc9_4 import Collection
app = Ursina()
camera.orthographic = True
camera.fov = 4
camera.position = (1, 1)
x1 = 4
character = ["cover.png","m1.png","m2.png","m3.png","m4.png","m5.png"]
level = ["easy","normal","hard"]
levelch = 0
leveladjust = 1
a = MainMe()
def exits():
    a.f.Delt()
    scene.clear()
    game_set()
def Main_Gstart():
    global charmanin,attack_dmg,health,levelch,leveladjust
    charmanin = 0
    start  = Main_Button(position = (1,1), text = "start")
    right = Main_Button(position = (2,1), text = "right")
    left = Main_Button(position = (0,1), text = "left")
    start.texture = character[charmanin]
    print(character[charmanin])
    levelleft = Main_Button(position = (0,2), text = "left")
    levelright = Main_Button(position = (2,2), text = "right")
    levelmid = Main_Button(position = (1,2), text = "easy")    
    levelch = 0
    leveladjust = 1
    def Gstart():
        global attack_dmg,health
        def seterer(a,b,c,d,e,f):
            global attack_dmg,health,levelmin,levelmax,levelminh,levelmaxh
            attack_dmg = a 
            health = b
            levelmin = round(c* leveladjust)
            levelmax = round(d* leveladjust)
            levelminh = round(e* leveladjust)
            levelmaxh = round(f* leveladjust)
        if character[charmanin] == "cover.png":
            seterer(10,100,3,7,10,20)
        elif character[charmanin] == "m1.png":
            seterer(11,98,4,7,10,15)
        elif character[charmanin] == "m2.png":
            seterer(12,96,3,8,12,16)
        elif character[charmanin] == "m3.png":
            seterer(13,94,2,10,9,20)
        elif character[charmanin] == "m4.png":
            seterer(14,90,1,7,4,25)
        elif character[charmanin] == "m5.png":
            seterer(7,110,6,7,6,30)
        Gamer(x1,start.texture,attack_dmg,health,levelmin,levelmax,levelminh,levelmaxh) 
        a.arturn()
        a.back_button_delete()
        destroy(start)
        destroy(right)
        destroy(left)
        destroy(levelleft)
        destroy(levelright)
        destroy(levelmid)
    def righttext():
        global charmanin 
        try:
            charmanin = charmanin+1
            start.texture = character[charmanin]
        except:
            charmanin = 0
            start.texture = character[charmanin]
            print(charmanin)
    def lefttext():
        global charmanin
        try:
            charmanin = charmanin-1
            start.texture = character[charmanin]
        except:
            charmanin = -1
            start.texture = character[charmanin]
            print(charmanin)
    def rightlevel():
        global levelch,leveladjust
        if levelch != len(level)-1:
            levelch += 1
            levelmid.text = level[levelch]
            print(levelch,levelmid.text)
            level_adjuster()
    def leftlevel():
        global levelch,leveladjust
        if levelch != 0:
            levelch -= 1
            levelmid.text = level[levelch]
            print(levelmid.text)
            level_adjuster()
    def level_adjuster():
        global leveladjust
        if levelmid.text == "easy":
            leveladjust = 1
        elif levelmid.text == "normal":
            leveladjust = 1.3
        elif levelmid.text == "hard":
            leveladjust = 1.6
    a.back_button()
    a.arturn()
    a.f.on_click = exits
    start.on_click = Gstart
    right.on_click = righttext
    left.on_click = lefttext
    levelright.on_click = rightlevel
    levelleft.on_click = leftlevel
def Main_Setting():
    Setting()
    a.back_button()
    a.arturn()
    a.f.on_click = exits
def Main_Credit():
    Credit()
    a.back_button()
    a.arturn()
    a.f.on_click = exits
#def Main_Collection():
 #   Collection()
  #  back_button()
def game_set():
    a.Main_menu()
    a.a.on_click = Main_Gstart
    a.b.on_click = Main_Setting
    a.c.on_click = Main_Credit
game_set()

app.run()