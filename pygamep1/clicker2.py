from ursina import *

app = Ursina()

window.color = color._20

window.fps_counter.enabled = False

window.exit_button.visible = False

window.title = 'herb'

herb = 0
counter = Text(text='0', y=.25, z=-1, scale=2, origin=(0,0), background= True)
button = Button(text='+', x = -0.7, y=.24, color=color.azure, scale= .25 , texture = "image/herb.png")

def button_click():
    global herb
    herb += 1
    counter.text = str(herb)

button.on_click = button_click



button_2 = Button(cost=10, x=.2, scale=.125, color=color.dark_gray, disabled=True)
button_2.tooltip = Tooltip(f'<gold> Herb Generator\n<default>Earn 1 herb every second.\nCosts {button_2.cost} herb.')

def buy_auto_herb():
    global herb
    if herb >= button_2.cost:
        herb -= button_2.cost
        counter.text = str(herb)
        invoke(auto_generate_herb, 1, 1)

button_2.on_click = buy_auto_herb



def auto_generate_herb(value= 1, interval=1):
    global herb
    herb += 1
    counter.text = str(herb)
    button_2.animate_scale(.125 * 1.1, duration=.1)
    button_2.animate_scale(.125, duration=.1, delay=.1)
    invoke(auto_generate_herb, value, delay=interval)


def update():
    global herb
    for b in (button_2, ):
        if herb >= b.cost:
            b.disabled = False
            b.color = color.green
        else:
            b.disabled = True
            b.color = color.gray



app.run()