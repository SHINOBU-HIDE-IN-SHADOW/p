from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("kivr13.kv")

class MyLayout(Widget):
    pass
class onetwozeroApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()
        
if __name__== '__main__':
    onetwozeroApp().run()