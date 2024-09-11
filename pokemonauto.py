import pyautogui
import time
import keyboard
import random
import win32api, win32con
#1476,983
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def poke():
    click(1375,983)
    pyautogui.write('$P')  
    pyautogui.press('enter')

def roll():
    time.sleep(1)
    click(1375,983)
    pyautogui.write('/mx')
    time.sleep(1)
    click(1381,920)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    if pyautogui.pixel(1347, 894)!=(255,156,44):
        if pyautogui.pixel(1347, 894)==(20,195,52) or pyautogui.pixel(1347, 894)==(20,194,52):
            click(1375,924)
            print("grabbed wish")
        #if not yellow blue or green grab
        elif pyautogui.pixel(1374,932)!=(217,211,96) and pyautogui.pixel(1374,932)!=(94,220,90) and pyautogui.pixel(1374,932)!=(73,197,215) and pyautogui.pixel(1374,932)!=(66,197,216) and pyautogui.pixel(1374,932)!=(218,211,87) and pyautogui.pixel(1374,932)!=(91,220,80) and pyautogui.pixel(1374,932)!=(78,218,66) and pyautogui.pixel(1374,932)!=(218, 211, 87) and pyautogui.pixel(1374,932)!=(91, 220, 81):
            print("grabbed k")
            click(1375,924)
            return False

def rolls():
    for x in range(15):
        roll()
        
sleepytime=0            
poke()
while keyboard.is_pressed('q') == False:
    time.sleep(sleepytime*60)
    if time.localtime()[3]%2==0:
        poke()
        if time.localtime()[3]==1:
            click(1375,983)
            pyautogui.write('$daily')  
            pyautogui.press('enter')
            time.sleep(3)
            pyautogui.write('$dk')  
            pyautogui.press('enter')
    rolls()
    if time.localtime()[4]>39:
        sleepytime=60-time.localtime()[4]+39
    else:
        sleepytime=39-time.localtime()[4]
    
    
    
