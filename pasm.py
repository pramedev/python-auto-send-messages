import pyautogui
from time import sleep

text = str(input("Enter text to send : "))
count = int(input("Enter how many massages you want to send : "))

while True :
    sleep(3)
    pyautogui.typewrite(text)
    sleep(1)
    pyautogui.press("enter")
    sleep(1)
    count = count - 1
    if count == 0 :
        break