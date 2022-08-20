from ursina import *

app = Ursina()

Entity(
    parent = scene,
    model = 'quad',
    scale = 500,
    color = color.black,
    double_sided = True,
    z =10
    
)

class player(Entity):
    def __init__(self, position=(0,0)):
        super().__init__(
            position = position,
            parent = scene,
            model = 'quad',
            color=color.red, scale = 1.25
        )
class Monster(Button):
    def __init__(self, position=(0,0)):
        super().__init__( position = position,
            parent = scene,
            model = 'quad',
            color=color.white, scale = 1)
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                destroy(self)

player1 = player(position=(0,0))

for x in range(3):
        for y in range(3):
           monster = Monster(position=(x, y))           

app.run()