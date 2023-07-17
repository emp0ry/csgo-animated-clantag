import os
import sys
import time
import ctypes
import telnetlib
import multiprocessing as mp
from pynput import keyboard as kb

BIND1 = kb.Key.f7 # for turn on or turn off script
BIND2 = kb.Key.f6 # switch animation
DELAY = 0.35 # it's a time between click f6

class Point(ctypes.Structure):
    _fields_ = [('x',ctypes.c_long), ('y', ctypes.c_long)]

class CursorInfo(ctypes.Structure):
    _fields_ = [
        ('cbSize', ctypes.c_uint),
        ('flags', ctypes.c_uint),
        ('hCursor', ctypes.c_void_p),
        ('ptScreenPos', Point)
    ]

# detect if cursor is hidden
def cursor_state():
    cinfo = CursorInfo(ctypes.sizeof(CursorInfo))
    ctypes.windll.user32.GetCursorInfo(ctypes.byref(cinfo))
    return not bool(cinfo.flags)

def write_console(command):
    try:
        tn = telnetlib.Telnet('127.0.0.1', 2121)
        tn.write(command.encode('utf-8'))
    except:
        print(f"failed to connect to csgo (game not open? -netconport 2121 not set?)")
        time.sleep(1)

# detect if pressed f7
def on_press(key, event1, event2):
    try:
        global timer1
        global timer2
        if key == BIND1 and cursor_state() and time.time() - timer1 > 1.5:
            if event1.is_set():
                ctypes.windll.kernel32.Beep(600, 250)
                print('OFF')
                write_console('cl_clanid 00000000\n')
                event1.clear()
            else:
                ctypes.windll.kernel32.Beep(800, 250)
                print('ON')
                event1.set()
            timer1 = time.time()
        elif key == BIND2 and cursor_state() and time.time() - timer2 > 1.5:
            if event2.is_set():
                ctypes.windll.kernel32.Beep(400, 100)
                print('TeamPro')
                event2.clear()
            else:
                ctypes.windll.kernel32.Beep(400, 100)
                print('GameSense')
                event2.set()
            timer2 = time.time()
    except AttributeError:
        pass

# clantag aniamtion key press
def when_pressed(event1, event2):
    while True:
        if event1.is_set():
            if event2.is_set():
                if event1.is_set():
                    write_console('cl_clanid 39977699\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 39977700\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 39977705\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 39977711\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 39977712\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 39977715\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 39977722\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 33349060\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 33349060\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 33349060\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 33349060\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 33349060\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 39977746\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 39977748\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 39977802\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 39977803\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 39977804\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 39977805\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 39977806\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 39977808\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 00000000\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 00000000\n')
                    time.sleep(DELAY)
            else:
                if event1.is_set():
                    write_console('cl_clanid 43916508\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917060\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917076\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917089\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917091\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917098\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917102\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917870\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917883\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917894\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917903\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917910\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917916\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917928\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917935\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917943\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917953\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917991\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917991\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917991\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917991\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917991\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917953\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917943\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917935\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917928\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917916\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917910\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917903\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917894\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917883\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917870\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917102\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917098\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917091\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917089\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917076\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43917060\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 43916508\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 00000000\n')
                    time.sleep(DELAY)
                if event1.is_set():
                    write_console('cl_clanid 00000000\n')
                    time.sleep(DELAY)

if __name__ == '__main__':
    os.system('cls')
    print('''
█▀▀ █░░ ▄▀█ █▄░█ ▀█▀ ▄▀█ █▀▀
█▄▄ █▄▄ █▀█ █░▀█ ░█░ █▀█ █▄█

█▄▄ █▄█   █▀▀ █▀▄▀█ █▀█ █▀█ █▀█ █▄█
█▄█ ░█░   ██▄ █░▀░█ █▀▀ █▄█ █▀▄ ░█░
https://github.com/emp0ry/''')
    print('github - https://github.com/emp0ry/')
    mp.freeze_support()
    sys.setrecursionlimit(100000) # without this, the code crashes after a while
    timer1, timer2 = 0, 0
    with mp.Manager() as manager:
        event1 = manager.Event()
        event2 = manager.Event()
        process = mp.Process(target=when_pressed, args=(event1, event2))
        with kb.Listener(on_press=lambda key: on_press(key, event1, event2)) as listener:
            process.start()
            listener.join()
            event1.clear()
            event2.clear()
            process.terminate()
