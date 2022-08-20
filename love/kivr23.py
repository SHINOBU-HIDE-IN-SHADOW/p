from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file("kivr23.kv")

class MyLayout(Widget):
   def spinner_clicked(self, value):
       self.ids_click_label = f'you selected {value}'
class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()