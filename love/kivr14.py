from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("kivr14.kv")

class MyLayout(Widget):
        def selected(self,filename):
            try:
                 self.ids.my_image.source = filename[0]
                 print(filename[0])
            except:
                pass
class onetwozeroApp(App):
    def build(self):
        return MyLayout()
        
if __name__== '__main__':
    onetwozeroApp().run()