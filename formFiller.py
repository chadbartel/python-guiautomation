#! python3
# formFiller.py - Automatically fills in the form.
# https://www.nostarch.com/automatestuffresources

import pyautogui, time

# Set these to the correct coordinates for your computer
nameField = (180, 347)
submitButton = (222, 845)
submitButtonColor = (74, 140, 246)
submitAnotherLink = (327, 261)

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
             'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet',
             'robocop': 4, 'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
             'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
             'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'}]

pyautogui.PAUSE = 0.5

for person in formData:
    # Give the user a chance to kill the script
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)

    # Wait until the form page has loaded.
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1],
                                          submitButtonColor):
        time.sleep(0.5)
    print("loaded")

# TODO: Fill ou the Name Field.

# TODO: Fill out the Greatest Fear(s) field.

# TODO: Fill out the Source or Wizard Powers field.

# TODO: Fill out the Robocop field.

# TODO: Fill out the Additional Comments field.

# TODO: Click Submit.

# TODO: Click the Submit another response link.
