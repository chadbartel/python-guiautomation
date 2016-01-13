#! python3
# mouseNow.py - Displays the mouse cursor's current position.

from pyautogui import position
from time import sleep
from tkinter import *

class Application(Frame):

    def __init__(self, master=NONE):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # TODO: create 2 labels
        self.instructLabel = Label(self,
                                   text='The button below will return your mouse\'s\n' +
                                   'position after counting down from five.',
                                   justify=CENTER,
                                   padx=2,
                                   pady=2)

        self.resultsLabelVar = StringVar()
        self.resultsLabel = Label(self,
                                  padx=2,
                                  pady=2,
                                  textvariable=self.resultsLabelVar)
        self.resultsLabelVar.set('Results displayed here.')

        # TODO: create button to begin countdown and get mouse coords
        self.bVar = StringVar()
        self.b = Button(self,
                        textvariable=self.bVar,
                        command=self.countThenMouse)
        self.bVar.set('Click me to get\nyour cursor\'s position!')

        # TODO: arrange each widget in the window
        self.instructLabel.grid(row=0, column=0, sticky=W+E)
        self.b.grid(row=1, column=0)
        self.resultsLabel.grid(row=2, column=0, sticky=W+E)

    def countDown(self):
        count = 5
        while count > 0:
            self.bVar.set(str(count))
            sleep(1)
            count -= 1

    def getMouse(self):
        x, y = position()
        self.resultsLabelVar.set('X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4))

    def countThenMouse(self):
        self.countDown()
        self.bVar.set('Say cheese!')
        sleep(0.5)
        self.getMouse()
        self.bVar.set('Click me to get\nyour cursor\'s position!')

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.master.title("Find My Mouse!")
    root.mainloop()
