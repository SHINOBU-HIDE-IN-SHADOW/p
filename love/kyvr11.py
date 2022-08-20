import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label  
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('kyvr11.kv') 

class MyLayout(Widget):
    def press(self):
        name = self.ids.name_input.text
        self.ids.name_label.text = "YES SHE IS {}".format(name)
        self.ids.name_input.text = ""

class bgapp(App):
    def build(self):
        return MyLayout()
        
if __name__ == '__main__':
    bgapp().run()
