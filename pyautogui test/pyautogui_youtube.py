import pyautogui
import keyboard
import time

pyautogui.press('win')
time.sleep(1)
pyautogui.write('google',interval=0.2)
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.6)


pyautogui.hotkey('ctrl','shift','n')
time.sleep(1)


pyautogui.write('youtube.com',interval=0.2)
time.sleep(1)
pyautogui.press('enter')
time.sleep(5)

pyautogui.moveTo(737,153,2,pyautogui.easeInQuad)
pyautogui.click()
time.sleep(2)
pyautogui.write('pyautogui',interval=0.2)
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)

pyautogui.scroll(-10)

pyautogui.moveTo(652,723,2,pyautogui.easeInQuad)
time.sleep(1)
pyautogui.click()