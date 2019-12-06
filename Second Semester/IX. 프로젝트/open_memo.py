import pyautogui as pag
import time
from mouse import mouse

if __name__ == '__main__':
    # m = mouse()
    # pag.click(31, 1054, duration=2)
    pag.press("winleft")
    time.sleep(1)
    pag.typewrite("memo")
    pag.press("enter")
    time.sleep(1)
    pag.typewrite("hello world\n\n")
    pag.press("hangul")
    pag.typewrite("qksrkqrnsk tptkddk")
    pag.hotkey("Ctrl", "s")
    time.sleep(1)
    pag.typewrite("vkdlTJs dPwp")
    pag.press("hangul")
    pag.typewrite(" Hello World")
    pag.press("enter")