import keyboard

x = True
while x == True:
    a = keyboard.record(until="A")

    print (a)

    if keyboard.press_and_release("A"):
        break