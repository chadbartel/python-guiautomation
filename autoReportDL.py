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
boxiEmailDict = {'a.png': 'C:\\a folder',
                 'b.png': 'C:\\b folder'}
autoGUIPicsFolder = 'C:\\'

# TODO: pack function in tkinter
class Application(Frame):

    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):

# create 2 frames
        self.labelButtonFrame = Frame(self,
                                      padx=2,
                                      pady=2)
        self.progressListFrame = Frame(self,
                                       padx=2,
                                       pady=2)

# create 2 labels to instruct user and display "Progress"
        self.autoGUILabel = Label(self.labelButtonFrame,
                                  text="Click the button below to begin downloading "
                                       "your reports automatically! Yay!",
                                  pady=2,
                                  wrap=125)
        self.progressLabel = Label(self.progressListFrame,
                                   text="Progress")

# create button to execute program
        self.beginButton = Button(self.labelButtonFrame,
                                  text="Begin!",
                                  pady=2,
                                  command=self.findGmailFolder)

# create list to keep track of progress
        self.progressList = Listbox(self.progressListFrame)

# create scrollbars for listbox
        self.scrollbarY = Scrollbar(self.progressListFrame)
        self.scrollbarX = Scrollbar(self.progressListFrame, orient=HORIZONTAL)
        self.progressList.config(yscrollcommand=self.scrollbarY.set,
                                xscrollcommand=self.scrollbarX.set)
        self.scrollbarY.config(command=self.progressList.yview)
        self.scrollbarX.config(command=self.progressList.xview)


# TODO: arrange your widgets in the window
        self.labelButtonFrame.grid(row=0, column=0, sticky=N+E+S+W)
        self.autoGUILabel.grid(row=0, column=0)
        self.beginButton.grid(row=1, column=0)
        self.progressListFrame.grid(row=0, column=1, sticky=N+E+S+W)
        self.progressLabel.grid(row=0, column=0)
        self.progressList.grid(row=1, column=0)
        self.scrollbarY.grid(row=1, column=1, sticky=N+S)
        self.scrollbarX.grid(row=2, column=0, sticky=W+E)

# look for email folder in gmail
    def findGmailFolder(self):
        # clear previous values from rollList
        self.progressList.delete(0, END)
        bfx, bfy = locateCenterOnScreen(autoGUIPicsFolder + 'breports-gmail-folder.png')
        click(bfx, bfy)
        sleep(1.5)
        self.findUnreadBOXIReports()

# look for each key [image] on screen from dict.
# when found click on the unread email and wait for
# the excel icon to appear
    def findUnreadBOXIReports(self):
        boxiUnreadPicsFolder = 'C:\\'
        for k, v in boxiEmailDict.items():
            self.progressList.insert(END, "Searching...")
            try:
                x, y = locateCenterOnScreen(boxiUnreadPicsFolder + k)
                self.progressList.insert(END, "Found " + str(k))
                click(x, y)
                while not locateOnScreen(autoGUIPicsFolder + 'excel-icon-email.png'):
                    sleep(0.25)
                self.findAttachedDoc(k, v)
            except:
                self.progressList.insert(END, "Could not find " + str(k))

# look for download button and wait for active 'OK' button to appear
    def findAttachedDoc(self, key, value):
        x1, y1 = locateCenterOnScreen(autoGUIPicsFolder + 'excel-icon-email.png')
        moveTo(x1, y1)
        x2, y2 = locateCenterOnScreen(autoGUIPicsFolder + 'download-file-button.png')
        click(x2, y2)
        while not locateOnScreen(autoGUIPicsFolder + 'ok-active.png'):
            sleep(0.25)
        self.saveAttachedDoc(key, value)

# save report to appropriate folder based on key-value pair
    def saveAttachedDoc(self, key, value):
        x1, y1 = locateCenterOnScreen(autoGUIPicsFolder + 'ok-active.png')
        click(x1, y1)
        sleep(0.25)
        x2, y2 = locateCenterOnScreen(autoGUIPicsFolder + 'save-active.png')
        moveTo(x2, y2)
        moveRel(-98, -416)
        click()
        sleep(0.25)
        typewrite(value, interval=0.1)
        press('enter', interval=0.5)

# if specific report, then change the file name
        if key == 'lsmp161-unread.png':
            x3, y3 = locateCenterOnScreen(autoGUIPicsFolder + 'save-as-filename.png')
            moveTo(x3, y3)
            moveRel(50)
            click()
            sleep(0.25)
            hotkey('ctrl', 'a')
            press('delete', interval=0.5)
            typewrite('MP161 US Les Schwab ' + str(date.today()), interval=0.1)
            x4, y4 = locateCenterOnScreen(autoGUIPicsFolder + 'save-active.png')
            click(x4, y4)
            self.progressList.insert(END, "Saved " + str(key) + " to " + str(value))
            sleep(0.25)
            x5, y5 = locateCenterOnScreen(autoGUIPicsFolder + 'gmail-back-button.png')
            click(x5, y5)
# if not, no need to change the file name and just click save and back out of email
        else:
            x6, y6= locateCenterOnScreen(autoGUIPicsFolder + 'save-active.png')
            click(x6, y6)
            self.progressList.insert(END, "Saved " + str(key) + " to " + str(value))
            sleep(0.25)
            x7, y7 = locateCenterOnScreen(autoGUIPicsFolder + 'gmail-back-button.png')
            click(x7, y7)

# create instance, launch window
if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("Download And Save Your Reports")
    root.mainloop()
