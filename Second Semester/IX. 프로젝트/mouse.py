import pyautogui as pag

class mouse:
    def __init__(self):
        while True:
            x, y = pag.position()
            print(x, y)
