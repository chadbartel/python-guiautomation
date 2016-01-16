from pyautogui import *
from time import sleep

PAUSE = 2.5
FAILSAFE = True

autoGUIPicFolder = 'c:\\pictures\\'

def findImage(image):
    try:
        sleep(3)
        x, y = locateCenterOnScreen(image)
        moveTo(x, y)
        return x, y
    except:
        alert(text='Could not locate image!', title='Error', button='OK')
        return None

print(findImage(autoGUIPicFolder + 'find-me.png'))
