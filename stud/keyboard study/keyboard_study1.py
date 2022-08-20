import keyboard
shortcut = keyboard.read_hotkey("a")

def on_triggered():
    print("Triggered!")

keyboard.hook(on_triggered)
keyboard.wait('esc')