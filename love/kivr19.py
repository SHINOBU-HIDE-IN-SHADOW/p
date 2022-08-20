from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('kivr19.kv')

class MyLayout(Widget):

    checks = []
    def checkbox_click(self, instance, value, top):
        if value == True:
           MyLayout.checks.append(top)
           tops = ""
           for x in MyLayout.checks:
               tops = f"{tops} {x}"
           self.ids.output_label.text = "you add {}".format(tops)
        else:
            MyLayout.checks.remove(top)
            tops = ""
            for x in MyLayout.checks:
               tops = f"{tops} {x}"
            self.ids.output_label.text = "you add {}".format(tops)    

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    MyApp().run()