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

Builder.load_file('kyrus.kv') 

class MyLayout(Widget):
   pass

class bgapp(App):
    def build(self):
        Window.clearcolor = (1,1,1,0.5)
        return MyLayout()
        
if __name__ == '__main__':
    bgapp().run()
