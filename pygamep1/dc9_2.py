from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
from ursina.prefabs.radial_menu import *
class Setting:
    def __init__(self):
        slider = ThinSlider(text="name", min=0, max=100, x=-.65, y=.4, step=1, dynamic=True)
        slider.scale *= .75
        slider = ThinSlider(text="name", min=0, max=100, x=-.65, y=.35, step=1, dynamic=True)
        slider.scale *= .75
        
        display_selection = ButtonGroup(('1', '2', '3'))

        a = DropdownMenu('File', buttons=(
        DropdownMenuButton('New'),
        DropdownMenuButton('Open'),
        DropdownMenu('Reopen Project', buttons=(
        DropdownMenuButton('Project 1'),
        DropdownMenuButton('Project 2'),
        )),
        DropdownMenuButton('Save'),
        DropdownMenu('Options', buttons=(
            DropdownMenuButton('Option a'),
            DropdownMenuButton('Option b'),
            )),
        DropdownMenuButton('Exit'),
        ))
        a.position = (-0.67,0.3) 

        rm = RadialMenu(
        buttons = (
            RadialMenuButton(text='1'),
            RadialMenuButton(text='2'),
            RadialMenuButton(text='3'),
            RadialMenuButton(text='4'),
            RadialMenuButton(text='5', scale=.5),
            RadialMenuButton(text='6', color=color.red),
            ),
        enabled = False
        )
        RadialMenuButton(text='6', color=color.red,x =-.5, scale=.06),
        def enable_radial_menu():
            rm.enabled = True
        cube = Button(parent=scene, model='cube', color=color.orange, highlight_color=color.azure, on_click=enable_radial_menu)
        EditorCamera()