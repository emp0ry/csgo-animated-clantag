import os
import sys
import time

try: import psutil
except: os.system("pip install psutil"); import psutil
try: import winsound
except: os.system("pip install winsound"); import winsound
try: import win32gui
except: os.system("pip install win32gui"); import win32gui
try: import win32process
except: os.system("pip install pywin32"); import win32process
try: from pynput import keyboard as kb
except: os.system("pip install pynput"); from pynput import keyboard as kb
try: import multiprocessing as mp
except:  os.system("pip install multiprocess"); import multiprocessing as mp

BIND = kb.Key.f7 # for turn on or turn off script
CFG_BIND = kb.Key.f6 # animation key
DELAY = 0.35 # it's a time between click f6

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

# detect if pressed f7
def on_press(key, event):
    try:
        global timer
        if key == BIND and in_csgo() and time.time() - timer > 1.5:
            if event.is_set():
                winsound.Beep(600, 250)
                print('OFF')
                event.clear()
            else:
                winsound.Beep(800, 250)
                print('ON')
                event.set()
            timer = time.time()
    except AttributeError:
        pass

# clantag aniamtion key press
def when_pressed(event):
    while True:
        if event.is_set() and in_csgo():
            keyboard = kb.Controller()
            keyboard.press(CFG_BIND)
            time.sleep(0.2)
            keyboard.release(CFG_BIND)
            time.sleep(DELAY - 0.3)
        else:
            time.sleep(0.1)

if __name__ == '__main__':
    print('''
    ▄▀█ █▄░█ █ █▀▄▀█ ▄▀█ ▀█▀ █▀▀ █▀▄   █▀▀ █░░ ▄▀█ █▄░█ ▀█▀ ▄▀█ █▀▀
    █▀█ █░▀█ █ █░▀░█ █▀█ ░█░ ██▄ █▄▀   █▄▄ █▄▄ █▀█ █░▀█ ░█░ █▀█ █▄█

    █▄▄ █▄█   █▀▀ █▀▄▀█ █▀█ █▀█ █▀█ █▄█
    █▄█ ░█░   ██▄ █░▀░█ █▀▀ █▄█ █▀▄ ░█░''')
    sys.setrecursionlimit(10000) # without it the code crashes
    timer = 0
    with mp.Manager() as manager:
        event = manager.Event()
        process = mp.Process(target=when_pressed, args=(event,))
        with kb.Listener(on_press=lambda key: on_press(key, event)) as listener:
            process.start()
            listener.join()
            event.clear()
            process.terminate()
