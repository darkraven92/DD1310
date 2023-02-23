from tkinter import *

def draw_triangle(img, x1, y1, x2, y2, x3, y3, color="#000000"):
    """Draws a filled triangle in img, given the coordinates of its three corners."""
    # Sort coordinates by y value
    if y1 > y2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    if y2 > y3:
        x2, y2, x3, y3 = x3, y3, x2, y2
    if y1 > y2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    
    # Calculate slopes and intercepts
    if y2 == y3:
        inv_slope_1 = 0
        inv_slope_2 = (x2 - x1) / (y2 - y1)
        intercept_1 = x1
        intercept_2 = x2 - inv_slope_2 * y2
    elif y1 == y2:
        inv_slope_1 = (x3 - x2) / (y3 - y2)
        inv_slope_2 = 0
        intercept_1 = x2 - inv_slope_1 * y2
        intercept_2 = x2
    else:
        inv_slope_1 = (x3 - x1) / (y3 - y1)
        inv_slope_2 = (x2 - x1) / (y2 - y1)
        intercept_1 = x1 - inv_slope_1 * y1
        intercept_2 = x2 - inv_slope_2 * y2
    
    # Fill in triangle using scanlines
    for y in range(y1, y3+1):
        x_start = int(inv_slope_1 * y + intercept_1)
        x_end = int(inv_slope_2 * y + intercept_2)
        if x_start > x_end:
            x_start, x_end = x_end, x_start
        for x in range(x_start, x_end+1):
            img.put(color, (x, y))
