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

        self.row_force_default= True
        self.row_default_height= 40
        self.col_force_default = True
        self.col_default_width=100

        self.top_grid = GridLayout(
            row_force_default= True,
            row_default_height= 40,
            col_force_default = True,
            col_default_width=100
            )

        self.top_grid.cols = 2

        self.top_grid.add_widget(Label(text='name:',size_hint_x = None, size_hint_y = None, height = 50 , width = 200))

        self.name = TextInput(multiline=False,size_hint_x = None, size_hint_y = None, height = 50 , width = 200)

        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text='pizza:',size_hint_x = None, size_hint_y = None, height = 50 , width = 200))

        self.pizza = TextInput(multiline=False,size_hint_x = None, size_hint_y = None, height = 50 , width = 200)

        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(Label(text='eat:'))

        self.eat = TextInput(multiline=False,size_hint_x = None, size_hint_y = None, height = 50 , width = 200)

        self.top_grid.add_widget(self.eat)

        self.add_widget(self.top_grid)

        self.submit = Button(text= 'submit', font_size=32, size_hint_x = None, size_hint_y = None, height = 50 , width = 200 )

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
