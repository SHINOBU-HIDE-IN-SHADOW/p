from ursina import *

app = Ursina()

class monster(Button):
    def __init__(self, position=(0,0)):
        super().__init__(
            position = position,
            model = 'cube',
            color=color.white, scale= .15
        )


class player(Button):
    def __init__(self, position=(0,0)):
        super().__init__(
            position = position,
            model = 'cube',
            color=color.red, scale= .15

        )

monster1 = monster(position=(0.25,0))
monster2 = monster(position=(0,0.25))
monster3 = monster(position=(-0.25,0))
monster4 = monster(position=(0,-0.25))
monster5 = monster(position=(-0.25,-0.25))
monster6 = monster(position=(0.25,0.25))
monster7 = monster(position=(0.25,-0.25))
monster8 = monster(position=(-0.25,0.25))
player1 = player(position=(0,0))

def input(self): 
        if monster1.on_click:
            player(position = (0.25,0)) 
        elif monster2.on_click:
            player(position = (0,0.25)) 
        elif monster3.on_click:
            player(position = (-0.25,0)) 
        elif monster4.on_click:
            player(position = (0,-0.25)) 
        elif monster5.on_click:
            player(position = (-0.25,-0.25)) 
        elif monster6.on_click:
            player(position = (0.25,0.25)) 
        elif monster7.on_click:
            player(position = (0.25,-0.25)) 
        elif monster8.on_click:
            player(position = (-0.25,0.25)) 
app.run()