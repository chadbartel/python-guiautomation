from pyautogui import locateCenterOnScreen, click, alert
from time import sleep

def findGmailFolder(image):
    try:
        x, y = locateCenterOnScreen('C:\\Users\\cbartel\\Pictures\\autoguipics\\' + image)
        sleep(3)
        click(x, y)
    except:
        alert(text='Could not locate image!', title='Error', button='OK')

findGmailFolder('smk-gmail-folder.png')
