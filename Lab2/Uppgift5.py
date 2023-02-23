from math import pi
from tkinter import *


def draw_filled_circle(img, center_x, center_y, radius, color="#000000"):
    for x in range(center_x - radius, center_x + radius + 1):
        for y in range(center_y - radius, center_y + radius + 1):
            if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
                img.put(color, (x, y))
