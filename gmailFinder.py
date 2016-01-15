from pyautogui import locateCenterOnScreen, click, alert
from time import sleep

def findGmailFolder(image):
    try:
        x, y = locateCenterOnScreen('C:\\pictures-folder\\' + image)
        sleep(3)
        click(x, y)
    except:
        alert(text='Could not locate image!', title='Error', button='OK')

findGmailFolder('image.png')
