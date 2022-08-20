import pyautogui
import time
import keyboard
from tkinter import *
window = Tk()
window.title("title")
window.geometry("400x400+100+100")

def motion(event):
    label = Label(window, text="event.x event.y")
    label.pack()
    return event.x, event.y

msg = Label(window, text = "a")
msg.bind('<Motion>', motion)
msg.pack()

window.mainloop()
