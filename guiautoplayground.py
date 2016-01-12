from pyautogui import *

# size() gives us a 2 int tuple of the screen's width & height in pix
winSize = size()
w, h = size()

print('Width ' + str(w))
print('Height ' + str(h))

# the following will move your mouse in a square 10 times
for i in range(10):
    moveTo(100, 100, duration=0.25)
    moveTo(200, 100, duration=0.25)
    moveTo(200, 200, duration=0.25)
    moveTo(100, 200, duration=0.25)
