import tkinter as tk

class window2:
    def __init__(self, master1):
        self.panel2 = tk.Frame(master1)
        self.panel2.grid()
        self.button2 = tk.Button(self.panel2, text = "Quit", command = self.panel2.quit)
        self.button2.grid()
        vcmd = (master1.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.dayValue = tk.StringVar()
        self.dayValue.trace('w', self.limitSizeDay)
        self.text1 = tk.Entry(self.panel2, validate = 'key', validatecommand = vcmd,textvariable=self.dayValue)
        self.text1.grid()
        self.text1.focus()
    def limitSizeDay(self,*args):
        value = self.dayValue.get()
        if len(value) > 2: self.dayValue.set(value[:2])
    def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                int(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return True
    
root1 = tk.Tk()
window2(root1)
root1.mainloop()