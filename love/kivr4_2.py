import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label  
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class LoginScreen(Widget):
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

class myapp(App):
    def build(self):
        return LoginScreen()
if __name__ == '__main__':
    myapp().run()
