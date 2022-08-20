import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label  
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder

#Builder.load_file('D:\\Users\\lobot\\Desktop\\pyprojects\\tensorflow_stud\\nonoe.kv') 
Builder.load_string(""" 
<Login>
    name: name
    pizza: pizza
    eat: eat
    GridLayout:
        cols: 1
        size: root.width , root.height

        GridLayout:
            cols: 2

            Label:
                text: "name"
            TextInput:
                id: name
                multiline: False

            Label:
                text: "pizza"
            TextInput:
                id: pizza
                multiline: False

            Label:
                text: "eat"
            TextInput:
                id: eat
                multiline: False

        Button:
            text: "Submit"    
            font_size: 32  
            on_press: root.press()          """)
class Login(Widget):
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    eat = ObjectProperty(None)

    def press(self):
        name = self.name.text

        pizza = self.pizza.text

        eat = self.eat.text

        print ('{} order {} eat in {}'.format(name,pizza,eat))

        self.name.text = ""

        self.pizza.text = ""

        self.eat.text = ""

class logapp(App):
    def build(self):
        return Login()
        
if __name__ == '__main__':
    logapp().run()
