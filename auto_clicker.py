#!python

import pyautogui
import time


def progress_bar(progress, end, percentage):
    return '{}{} {} %'.format(progress, end, str(percentage))

count = 0
print("\n" * 100)
print("Starting")
progress = "["
end = "__________]"
percentage = 0
print(progress_bar(progress, end, percentage))
try:
    while(True):
        count += 1
        pyautogui.click()
        time.sleep(.001)
        if count % 10 == 0 and percentage <= 90:
            print("\n" * 100)
            progress += '#'
            end = end[1:]
            percentage = count
            print("Running...")
            print(progress_bar(progress, end, percentage))
        if count >= 100:
            print("Pause")
            answer = input('Continue Y/N? ')
            if answer == "N":
                break
            print("Starting in 10 seconds")
            time.sleep(5)
            count = 0
            print("\n" * 100)
            print("Starting")
            progress = "["
            end = "__________]"
            percentage = 0
            print(progress_bar(progress, end, percentage))
except KeyboardInterrupt:
    print('Close Loop')
