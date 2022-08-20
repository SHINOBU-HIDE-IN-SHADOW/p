from ursina import *



app = Ursina()

class player(Entity):
    def __init__(self, position=(0,0)):
        super().__init__(
            position = position,
            model = 'quad',
            color=color.red, scale = 1.25
        )
class mover(Entity):
    def __init__(self,position=(0,0)):
        super().__init__()
        destroy(self)
        player(self.position)
        


monster1 = Button(color=color.white, scale= .15 , model = 'quad',eternal = False,position = (0.25,0),on_click = mover(position=(0.25,0)))
monster2 = Button(color=color.white, scale= .15 , model = 'quad', position = (0,0.25))
monster3 = Button(color=color.white, scale= .15 , model = 'quad',position = (-0.25,0))
monster4 = Button(color=color.white, scale= .15 , model = 'quad', position = (0,-0.25))
monster5 = Button(color=color.white, scale= .15 , model = 'quad',position = (-0.25,-0.25))
monster6 = Button(color=color.white, scale= .15 , model = 'quad',position = (0.25,0.25))
monster7 = Button(color=color.white, scale= .15 , model = 'quad',position = (0.25,-0.25))
monster8 = Button(color=color.white, scale= .15 , model = 'quad', position = (-0.25,0.25))
    
player1 = player(position=(0,0))



app.run()