import ctypes
import time
import math
import keyboard


def do_move():
    i = 0
    while i < 28800:
        y = 666 + int(235 * math.sin(i * math.pi/180))
        x = 777 + int(235 * math.cos(i * math.pi/180))
        print(i, x, y)
        ctypes.windll.user32.SetCursorPos(x, y)
        keyboard.SendInput(keyboard.Keyboard(keyboard.VK_F15))
        time.sleep(60)
        i = i + 1


if __name__ == '__main__':
    do_move()
