#!python
# http://orteil.dashnet.org/cookieclicker/

import pyautogui
import time

for x in range(1000):
    pyautogui.click()
    time.sleep(.0001)
    print(x)
