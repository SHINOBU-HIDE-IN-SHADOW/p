from ursina import *            

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
print(color.brightness(color.blue))

p = Entity(x=-2)
for key in color.colors:
    print(key)
    b = Button(parent=p, model=Quad(subdivisions=2), color=color.colors[key], text=key)
    b.text_entity.scale *= .5

grid_layout(p.children, max_x=8)

for name in ('r', 'g', 'b', 'h', 's', 'v', 'brightness'):
    print(name + ':', getattr(color.random_color(), name))

e = Entity(model='cube', color=color.lime)
print(e.color.name)


e = Entity(model='quad', texture='brick')
e.texture.set_pixel(0, 2, color.blue)
e.texture.apply()

for y in range(e.texture.height):
    for x in range(e.texture.width):
        if e.texture.get_pixel(x,y) == color.blue:
            print('found blue pixel at:', x, y)

ground = Entity(
    model = 'cube',
    color = color.magenta,
    z = -.1,
    y = -3,
    origin = (0, .5),
    scale = (50, 1, 10),
    collider = 'box'
    )

app.run()                    