"""
ONLY FOR GOOGLE MEET

"""
import webbrowser
#for web actions
import time
#for time and putting it to sleep
import pyautogui
#for all the display and cursor actions
from datetime import datetime
#for the local time

classtime = input("Enter your Class Time : ")
#Taking Class Time
endtime = input("Enter your class End time : ")
#Taking Class End Time
classlink = input("Enter Class Link : ")
#Taking Class Link

while True:
    local = datetime.now().strftime("%H:%M")
    if local == classtime:
        chrome_path = "chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome')
        webbrowser.open(classlink)
        time.sleep(6)
        pyautogui.click(x=684, y=734, button='left', clicks=1)
        time.sleep(1)
        pyautogui.click(x=765, y=739, button='left', clicks=1)
        time.sleep(1)
        pyautogui.click(x=1272, y=574, button='left', clicks=1)
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'alt','c')
        time.sleep(3)
        pyautogui.write("Present")
        time.sleep(1)
        pyautogui.keyDown('return')
        break

while True:
     local = datetime.now().strftime("%H:%M")
     if local == endtime:
        time.sleep(3)
        pyautogui.hotkey('ctrl','w')
        break






