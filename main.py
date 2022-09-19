import ctypes
import time
import math


def send_input_f15():
    vk_f15 = (0x7E)  # F15
    ctypes.windll.user32.SendInput(1, vk_f15, 1)


class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]


def do_move():
    i = 0
    old_pt = Point()
    while i < 28800:
        new_pt = Point()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(new_pt))

        if old_pt.x == new_pt.x and old_pt.y == new_pt.y:
            y = 666 + int(235 * math.sin(i * math.pi / 180))
            x = 777 + int(235 * math.cos(i * math.pi / 180))
            print(i, x, y)
            ctypes.windll.user32.SetCursorPos(x, y)
            send_input_f15()
            old_pt.x = x
            old_pt.y = y
        else:
            old_pt = new_pt
            print(i, new_pt.x, new_pt.y, 'skip')

        time.sleep(10)
        i = i + 1


if __name__ == '__main__':
    do_move()
