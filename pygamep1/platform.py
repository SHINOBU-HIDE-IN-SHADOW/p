from ursina import *            
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

window.fps_counter.enabled = False

window.exit_button.visible = False

ground = Entity(
    model = 'quad',
    color = color.magenta,
    collider = 'quad',
    origin = (0, .5),
    scale = (50, 6),
    ignore = True
    )

         
player = PlatformerController2d(jump_height=3, model = 'quad',origin_y = -0.5, scale_y = 0.9, scale_x = 0.5, y = 5, texture = 'brick')

camera.add_script(SmoothFollow(target=player, offset=[0,1,-30], speed=4))

EditorCamera(hotkeys = {'toggle_orthographic':'shift+p', 'focus':'f', 'reset_center':'shift+f'})

b=Button(text='x', scale=.25, x = - .77, y = .4)

b.on_click = application.quit

b.tooltip = Tooltip('exit')

def input(key):
    if key == 'escape':
         application.quit()
    
def input(key):
    if key == 'r':
         player.position = (10,10)
               
app.run()                      
