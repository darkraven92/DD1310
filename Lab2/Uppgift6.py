import random
from tkinter import *

SIZE = 600


def draw_triangle(canvas, x1, y1, x2, y2, x3, y3, fill):
    """Draws a filled triangle with given coordinates and fill color."""
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=fill, outline="")

def draw_circle(canvas, x, y, r, fill):
    """Draws a filled circle with given center coordinates, radius and fill color."""
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=fill, outline="")

def draw_tree(canvas, x, y, size):
    """Draws a Christmas tree with given center coordinates and size."""
    trunk_width = size / 8
    trunk_height = size / 4
    tree_height = size - trunk_height
    tree_width = tree_height / 2
    triangle_colors = ["#1a936f", "#88d8b0", "#c6dabf", "#f6e8b1", "#f6bc67"]
    
    # Draw trunk
    canvas.create_rectangle(x - trunk_width / 2, y + tree_height, x + trunk_width / 2, y + tree_height + trunk_height, fill="#663300", outline="")
    
    # Draw tree triangles
    for i in range(5):
        triangle_size = tree_width * (5 - i) / 5
        x1 = x - triangle_size / 2
        y1 = y + tree_height - tree_height * i / 5
        x2 = x + triangle_size / 2
        y2 = y1
        x3 = x
        y3 = y1 - triangle_size * 0.866
        fill = triangle_colors[i]
        draw_triangle(canvas, x1, y1, x2, y2, x3, y3, fill)
    
    # Draw tree ornaments
    for i in range(20):
        r = random.uniform(5, 15)
        x = random.uniform(x - tree_width / 2, x + tree_width / 2)
        y = random.uniform(y - tree_height, y + trunk_height)
        fill = random.choice(["red", "yellow", "blue", "purple"])
        draw_circle(canvas, x, y, r, fill)

def main():
    """Create your canvas and call your functions inside this function."""
    window = Tk()
    canvas = Canvas(window, width=SIZE, height=SIZE, bg="#ffffff")
    canvas.pack()
    draw_tree(canvas, SIZE / 2, SIZE * 3 / 4, SIZE / 2)
    mainloop()


if __name__ == '__main__':
    main()
