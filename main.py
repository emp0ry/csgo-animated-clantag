print('''
▄▀█ █▄░█ █ █▀▄▀█ ▄▀█ ▀█▀ █▀▀ █▀▄   █▀▀ █░░ ▄▀█ █▄░█ ▀█▀ ▄▀█ █▀▀
█▀█ █░▀█ █ █░▀░█ █▀█ ░█░ ██▄ █▄▀   █▄▄ █▄▄ █▀█ █░▀█ ░█░ █▀█ █▄█

█▄▄ █▄█   █▀▀ █▀▄▀█ █▀█ █▀█ █▀█ █▄█
█▄█ ░█░   ██▄ █░▀░█ █▀▀ █▄█ █▀▄ ░█░''')

DELAY = 0.35 # it's a time between click f6

import os
import sys
import time

try: import keyboard
except: os.system("pip install keyboard"); import keyboard
try: import winsound
except: os.system("pip install winsound"); import winsound
try: import win32process
except: os.system("pip install pywin32");  import win32process
try: import win32gui
except: os.system("pip install win32gui"); import win32gui
try: import psutil
except: os.system("pip install psutil"); import psutil

# detect if you in csgo
def in_csgo():
    time.sleep(0.1)
    try:
        hwnd = win32gui.GetForegroundWindow()
        pid = win32process.GetWindowThreadProcessId(hwnd)[1]
        process = psutil.Process(pid).name()
        return True if process == 'csgo.exe' else False
    except:
        in_csgo()

def main():
    switch, timer = False, 0

    while True:
        if in_csgo():
            if time.time() - timer > 2 and keyboard.is_pressed('f7'):
                switch = not switch
                if switch:
                    print('ON')
                    winsound.Beep(800, 250)
                else:
                    print('OFF')
                    winsound.Beep(600, 250)
                timer = time.time()
            if switch:
                keyboard.press_and_release('f6')
                time.sleep(DELAY - 0.1)

if __name__ == "__main__":
    sys.setrecursionlimit(10000) # without it the code crashes
    main()
