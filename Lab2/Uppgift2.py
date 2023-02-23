from PIL import Image, ImageDraw


def draw_filled_rectangle(img, upper_left, lower_right, color):
    """Draws a filled rectangle on img with corners at upper_left and lower_right, filled with color."""
    draw = ImageDraw.Draw(img)
    draw.rectangle([upper_left, lower_right], fill=color)

img = Image.new("RGB", (SIZE, SIZE), color="#000000")
draw_filled_rectangle(img, (100, 100), (200, 200), color="#ff0000")
