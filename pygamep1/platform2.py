from ursina import *            
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

window.fps_counter.enabled = False

window.exit_button.visible = False

camera.orthographic = True

camera.fov = 20

window.title = 'game1'

traps = []

trap = Entity(model = 'cube', collider = 'cube',
                parent = scene, texture = 'image/spike.png',
                color = color.white, position = Vec2(0,3),)
traps.append(trap)
trap_1 = duplicate(trap, x=5)
traps.append(trap_1)


class ground(Entity):
    def __init__(self, position=(0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            texture = 'brick',
            color = color.white,
            highlight_color = color.lime,
            scale= 1.0,
            collider = 'box' 
        )

for x in range(30):
        for y in range(3):
            ground(position=(x, y))
         
player = PlatformerController2d(jump_height=3, max_jumps= 2, texture = 'image\\cover.png', scale = (1,1), position = (10,10) )
player.y = raycast(player.world_position, player.down).world_point[1] + .01
camera.add_script(SmoothFollow(target=player, offset=[0,5,-30], speed=4))

b=Button(text='x', scale=.25, x = - .77, y = .4)

b.on_click = application.quit

b.tooltip = Tooltip('exit')

def input(key):
    if key == 'escape':
         application.quit()
    
def input(key):
    if key == 'r':
         player.position = (10,10)

def update():
    hit_info = player.intersects()
    if hit_info.hit:
        if hit_info.entity in traps:
            player.position = (10,10)

player.add_script(NoclipMode2d())
               
app.run()                      
