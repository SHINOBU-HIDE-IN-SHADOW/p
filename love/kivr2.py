import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label  
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        self.cols = 1

        self.top_grid = GridLayout()

        self.top_grid.cols = 2

        self.top_grid.add_widget(Label(text='name:'))

        self.name = TextInput(multiline=False)

        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text='pizza:'))

        self.pizza = TextInput(multiline=False)

        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(Label(text='eat:'))

        self.eat = TextInput(multiline=False)

        self.top_grid.add_widget(self.eat)

        self.add_widget(self.top_grid)

        self.submit = Button(text= 'submit', font_size=32)

        self.submit.bind(on_press= self.press)

        self.add_widget(self.submit)
    def press(self,instance):
        name = self.name.text

        pizza = self.pizza.text

        eat = self.eat.text

        self.add_widget(Label(text= '{} order {} eat in {}'.format(name,pizza,eat)))

        self.name.text = ""

        self.pizza.text = ""

        self.eat.text = ""

class myapp(App):
    def build(self):
        return LoginScreen()
if __name__ == '__main__':
    myapp().run()
