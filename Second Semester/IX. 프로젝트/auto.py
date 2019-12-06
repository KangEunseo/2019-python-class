import pyautogui as pag
import time

if __name__ == '__main__':
    # while(True):
    #     x, y = pag.position()
    #     print("x: {}\ty: {}".format(x, y), end="\r")
    # pag.moveTo(44, 280, duration=2)
    # pag.doubleClick()
    # pag.drag(0, 200, duration=2)
    # pag.rightClick()
    pag.doubleClick(44, 280, duration=2)

    time.sleep(1)             #크롬이 열리기를 기다려야 함
    # pag.press("hangul")       한영키
    # pag.typewrite("rkddmstj") 강은서 영어로
    # pag.typewrite("https://ticket.interpark.com/")
    # pag.press("enter")

    pag.hotkey("alt", "tab")
    pag.scroll(clicks=200, x=798, y=185)