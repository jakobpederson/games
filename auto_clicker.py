#!python

import pyautogui
import time

count = 0
print("Starting")
progress_bar = "["
end = "__________]"
percentage = 0
print(progress_bar + end + " " + str(percentage) + "%")
try:
    while(True):
        count += 1
        pyautogui.click()
        time.sleep(.001)
        if count % 50 == 0:
            progress_bar += '#'
            end = end[1:]
            percentage = (count / 100) * 20
            print(progress_bar + end + " " + str(percentage) + "%")
        if count >= 500:
            print("10 second pause")
            answer = input('Continue Y/N? ')
            if answer == "N":
                print("Starting in 10 seconds")
                break
            time.sleep(10)
            count = 0
            print("Starting")
            progress_bar = "["
            end = "__________]"
            percentage = 0
            print(progress_bar + end + " " + str(percentage) + "%")
except KeyboardInterrupt:
    print('Close Loop')
