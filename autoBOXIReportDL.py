from pyautogui import *
from tkinter import *
from time import sleep
from datetime import date

# activate the failsafe just in case.
# move your cursor to the top left of the screen
# to deactivate the program
FAILSAFE = True
PAUSE = 2.5

boxiEmailDict = {}
autoGUIPicsFolder = '\'

# look for email folder in gmail
def findGmailFolder():
    bfx, bfy = locateCenterOnScreen(autoGUIPicsFolder + 'breports-gmail-folder.png')
    click(bfx, bfy)
    sleep(1.5)
    findUnreadBOXIReports()

# look for each key [image] on screen from dict.
# when found click on the unread email and wait for
# the excel icon to appear
def findUnreadBOXIReports():
    boxiUnreadPicsFolder = ''
    try:
        for k, v in boxiEmailDict.items():
            x, y = locateCenterOnScreen(boxiUnreadPicsFolder + k)
            click(x, y)
            while not locateOnScreen(autoGUIPicsFolder + 'excel-icon-email.png'):
                sleep(0.25)
            findAttachedDoc(k, v)
    except:
        pass

# look for download button and wait for active 'OK' button to appear
def findAttachedDoc(key, value):
    x1, y1 = locateCenterOnScreen(autoGUIPicsFolder + 'excel-icon-email.png')
    moveTo(x1, y1)
    x2, y2 = locateCenterOnScreen(autoGUIPicsFolder + 'download-file-button.png')
    click(x2, y2)
    while not locateOnScreen(autoGUIPicsFolder + 'ok-active.png'):
        sleep(0.25)
    saveAttachedDoc(key, value)

# save report to appropriate folder based on key-value pair
def saveAttachedDoc(key, value):
    x1, y1 = locateCenterOnScreen(autoGUIPicsFolder + 'ok-active.png')
    click(x1, y1)
    sleep(0.25)
    x2, y2 = locateCenterOnScreen(autoGUIPicsFolder + 'save-active.png')
    moveTo(x2, y2)
    moveRel(-98, -416)
    click()
    sleep(0.25)
    typewrite(value, interval=0.25)
    press('enter')
    sleep(1)

# if specific report, then change the file name
    if key == 'lsmp161-unread.png':
        x3, y3 = locateCenterOnScreen(autoGUIPicsFolder + 'save-as-filename.png')
        moveTo(x3, y3)
        moveRel(30)
        click()
        sleep(0.25)
        hotkey('ctrl', 'a')
        press('delete', interval=0.25)
        typewrite('MP161 US Les Schwab ' + str(date.today()), interval=0.25)
        x4, y4 = locateCenterOnScreen(autoGUIPicsFolder + 'save-active.png')
        click(x4, y4)
        sleep(0.25)
        x5, y5 = locateCenterOnScreen(autoGUIPicsFolder + 'gmail-back-button.png')
        click(x5, y5)
# if not, no need to change the file name and just click save and back out of email
    else:
        x6, y6= locateCenterOnScreen(autoGUIPicsFolder + 'save-active.png')
        click(x6, y6)
        sleep(0.25)
        x7, y7 = locateCenterOnScreen(autoGUIPicsFolder + 'gmail-back-button.png')
        click(x7, y7)

# TODO: pack function in tkinter
class Application(Frame):

    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        pass
