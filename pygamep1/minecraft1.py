from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController



app = Ursina()

window.fps_counter.enabled = False

window.exit_button.visible = False

Entity(
    parent = scene,
    model = 'sphere',
    scale = 500,
    color = color.rgb(65,105,225),
    double_sided = True,
    
)

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white_cube',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime,
            scale= 1.0,
        )


    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)

            if key == 'right mouse down':
                destroy(self)


for y in range(3):
    for z in range(15):
        for x in range(15):
            voxel = Voxel(position=(x, y,z))


player = FirstPersonController()
app.run()