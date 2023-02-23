from tkinter import *

SIZE = 600

def draw_filled_triangle(img, x1, y1, x2, y2, x3, y3, color):
    """Draws a filled triangle on img with vertices (x1, y1), (x2, y2), and (x3, y3) and color color."""
    coords = [x1, y1, x2, y2, x3, y3]
    img.put(color, tuple(coords), "polygon")

def draw_filled_circle(img, x, y, r, color):
    """Draws a filled circle on img with center (x, y) and radius r and color color."""
    x1, y1 = x - r, y - r
    x2, y2 = x + r, y + r
    coords = [x1, y1, x2, y2]
    img.ellipse(tuple(coords), fill=color)

def draw_tree(img, x, y, height, color):
    """Draws a tree on img with base at (x, y), height height, and color color."""
    draw_filled_triangle(img, x - height / 2, y, x + height / 2, y, x, y - height, color)
    draw_filled_circle(img, x, y - height, height / 4, "#663300")
    draw_filled_circle(img, x - height / 4, y - height / 2, height / 4, "#006600")
    draw_filled_circle(img, x + height / 4, y - height / 2, height / 4, "#006600")

def draw_house(img, x, y, height, color):
    """Draws a house on img with base at (x, y), height height, and color color."""
    draw_filled_triangle(img, x - height / 2, y, x + height / 2, y, x, y - height, color)
    draw_filled_rectangle(img, x - height / 4, y, x + height / 4, y - height / 2, "#663300")

def draw_sun(img, x, y, r, color):
    """Draws a sun on img with center (x, y), radius r, and color color."""
    draw_filled_circle(img, x, y, r, color)
    for i in range(8):
        angle = i * 45
        x1, y1 = x + r * math.cos(math.radians(angle)), y - r * math.sin(math.radians(angle))
        x2, y2 = x + 2 * r * math.cos(math.radians(angle)), y - 2 * r * math.sin(math.radians(angle))
        img.create_line(x1, y1, x2, y2, fill=color, width=2)

def main():
    """Draw a picture of a house with a sun above it."""
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#66ccff")
    canvas.pack()
    img = PhotoImage(width=SIZE, height=SIZE)
    canvas.create_image((SIZE / 2, SIZE / 2), image=img, state="normal")
    draw_house(img, 300, 400, 200, "#ff9933")
    draw_tree(img, 100, 400, 200, "#006600")
    draw_tree(img, 500, 400, 
