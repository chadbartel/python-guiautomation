from pyautogui import *

# size() gives us a 2 int tuple of the screen's width & height in pix
winSize = size()
w, h = size()

print('Width ' + str(w))
print('Height ' + str(h))

# the following will move your mouse in a square 5 times
# the coordinates are in an EXPLICIT region of the screen
for i in range(5):
    moveTo(100, 100, duration=0.25)
    moveTo(200, 100, duration=0.25)
    moveTo(200, 200, duration=0.25)
    moveTo(100, 200, duration=0.25)

# the following will move your mouse in a square 5 times
# the coordinates are in a RELATIVE region of the screen
# it's relative to where your mouse is
for i in range(5):
    moveRel(100, 0, duration=0.25)
    moveRel(0, 100, duration=0.25)
    moveRel(-100, 0, duration=0.25)
    moveRel(0, -100, duration=0.25)
