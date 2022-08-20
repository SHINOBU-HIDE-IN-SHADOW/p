from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("kivr26.kv")

class MyLayout(Widget):
    def word_on(self):
        self.ids.my_label.text = "Pressing"
        self.ids.my_image.source = ''
    def word_off(self):
        self.ids.my_image.source = 'love/iloveu.jpg'    
        if self.ids.my_label.text == "Press button":
            self.ids.my_label.text  = "Pressed"
         
class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__' :
    MyApp().run()