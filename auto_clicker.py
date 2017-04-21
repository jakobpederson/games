#!python

import pyautogui
import time

count = 0
print("Starting")
progress_bar = "["
end = "_____]"
percentage = 0
print(progress_bar + end + " " + str(percentage) + "%")
try:
    while(True):
        count += 1
        pyautogui.click()
        time.sleep(.001)
        if count % 100 == 0:
            progress_bar += '#'
            end = end[1:]
            percentage = (count / 100) * 20
            print(progress_bar + end + " " + str(percentage) + "%")
        if count >= 500:
            print("10 second pause", count)
            answer = input('Continue Y/N? ')
            if answer == "N":
                break
            time.sleep(10)
            count = 0
except KeyboardInterrupt:
    print('Close Loop')


