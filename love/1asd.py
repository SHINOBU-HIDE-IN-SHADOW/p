from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World', 
        pos=(50,50), 
        size=(100,100),
        size_hint=(None,None))
TestApp().run()