from kivy.app import App
from kivy.uix.button import Button

class FunkyButton(Button):
    super(LoginScreen, self).__init__(**kwargs)
    self.text='Hello World'
    self.pos=(50,50)
    self.size=(100,100)
    self.size_hint=(.25,.25)


class TestApp(App):
    def build(self):
        return FunkyButton
TestApp().run()