from pyautogui import *
from tkinter import *
from time import sleep
from datetime import date

# activate the failsafe just in case.
# move your cursor to the top left of the screen
# to deactivate the program
FAILSAFE = True
PAUSE = 2.5

# create the k-v pair for each matched image with its save dir
boxiEmailDict = {'a.png': 'C:\\a folder\\', 'b.png': 'C:\\b folder\\'}
autoGUIPicsFolder = 'C:\\autoguipics\\'

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
    boxiUnreadPicsFolder = 'C:\\report folder\\'
    for k, v in boxiEmailDict.items():
        print("Searching for " + str(k) + "...")
        try:
            while not locateCenterOnScreen(boxiUnreadPicsFolder + k):
                sleep(0.3)
            x, y = locateCenterOnScreen(boxiUnreadPicsFolder + k)
            print("Found " + str(k))
            click(x, y)
            while not locateOnScreen(autoGUIPicsFolder + 'excel-icon-email.png'):
                sleep(0.25)
            findAttachedDoc(k, v)
        except:
            print("Could not find " + str(k))

# look for download button and wait for active 'OK' button to appear
def findAttachedDoc(key, value):
    x1, y1 = locateCenterOnScreen(autoGUIPicsFolder + 'excel-icon-email.png')
    moveTo(x1, y1)
    sleep(0.25)
    moveRel(31, -10)
    click()
    while not locateOnScreen(autoGUIPicsFolder + 'ok-active.png'):
        sleep(0.3)
    x1, y1 = locateCenterOnScreen(autoGUIPicsFolder + 'ok-active.png')
    sleep(0.1)
    click(x1, y1)
    saveAttachedDoc(key, value)

# save report to appropriate folder based on key-value pair
def saveAttachedDoc(key, value):
    while not locateCenterOnScreen(autoGUIPicsFolder + 'folder-icon.png'):
        sleep(0.3)
    x1, y1 = locateCenterOnScreen(autoGUIPicsFolder + 'folder-icon.png')
    sleep(0.1)
    click(x1, y1)
    sleep(0.1)
    typewrite(value, interval=0.1)
    press('enter', interval=0.5)

# if specific report, then change the file name
    if key == 'a.png':
        x3, y3 = locateCenterOnScreen(autoGUIPicsFolder + 'save-as-filename.png')
        moveTo(x3, y3)
        sleep(0.25)
        moveRel(50)
        click()
        sleep(0.25)
        hotkey('ctrl', 'a')
        press('delete', interval=0.5)
        typewrite('Report ' + str(date.today()), interval=0.1)
        x4, y4 = locateCenterOnScreen(autoGUIPicsFolder + 'save-active.png')
        click(x4, y4)
        print("Saved " + str(key) + " to " + str(value))
        sleep(0.25)
        x5, y5 = locateCenterOnScreen(autoGUIPicsFolder + 'gmail-back-button.png')
        click(x5, y5)
# if not, no need to change the file name and just click save and back out of email
    else:
        x6, y6 = locateCenterOnScreen(autoGUIPicsFolder + 'save-active.png')
        click(x6, y6)
        print("Saved " + str(key) + " to " + str(value))
        sleep(0.25)
        x7, y7 = locateCenterOnScreen(autoGUIPicsFolder + 'gmail-back-button.png')
        click(x7, y7)

if __name__ == "__main__":
    findGmailFolder()
