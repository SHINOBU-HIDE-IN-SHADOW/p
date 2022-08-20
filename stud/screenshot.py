import pyautogui
run = True
while run = True:
if pyautogui.press('enter'):
    i = pyautogui.position()
    pyautogui.screenshot("1.jpg", region=(i))
    pass