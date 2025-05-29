import pyautogui
import keyboard
import time

pyautogui.press('win')
time.sleep(2)

pyautogui.write('Google chrome', interval=0.2)
time.sleep(1)

pyautogui.press('enter')
time.sleep(1)

pyautogui.hotkey('ctrl','shift','n')
time.sleep(2)

pyautogui.write('siga')
time.sleep(1)

for i in range(10):
    pyautogui.press('tab',interval=0.1)

time.sleep(1)

pyautogui.press('enter')
time.sleep(1)

pyautogui.write('aliceshigihara',interval=0.1)
time.sleep(1)

pyautogui.press('tab')
time.sleep(1)


