print('''
▄▀█ █▄░█ █ █▀▄▀█ ▄▀█ ▀█▀ █▀▀ █▀▄   █▀▀ █░░ ▄▀█ █▄░█ ▀█▀ ▄▀█ █▀▀
█▀█ █░▀█ █ █░▀░█ █▀█ ░█░ ██▄ █▄▀   █▄▄ █▄▄ █▀█ █░▀█ ░█░ █▀█ █▄█

█▄▄ █▄█   █▀▀ █▀▄▀█ █▀█ █▀█ █▀█ █▄█
█▄█ ░█░   ██▄ █░▀░█ █▀▀ █▄█ █▀▄ ░█░''')

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
    try:
        hwnd = win32gui.GetForegroundWindow()
        pid = win32process.GetWindowThreadProcessId(hwnd)[1]
        process = psutil.Process(pid).name()
        return True if process == 'csgo.exe' else False
    except:
        in_csgo()

# press f6 if you in csgo
def press_key():
    if in_csgo():
        keyboard.press_and_release('f6')
    else:
        while not in_csgo():
            pass
        keyboard.press_and_release('f6')

# 0-10 second making input lag
def synchronized_start():
    while int(time.time() % 10) != 0:
        pass

def main():
    switch = False

    while True:
        if keyboard.is_pressed('f7'):
            switch = not switch
            if switch:
                print('ON')
                winsound.Beep(800, 250)
                while not in_csgo():
                    pass
                # synchronized_start() # <-------< to make +- synchron start with friend
            else:
                print('OFF')
                winsound.Beep(600, 250)
            time.sleep(2)

        if switch:
            press_key()
            time.sleep(0.35)
        else:
            time.sleep(0.1)

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()