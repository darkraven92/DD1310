def draw_rectangles(img, upper_left, lower_right):
    # Draw white rectangle
    draw_rectangle(img, (0, 0), (SIZE-1, SIZE-1), "#ffffff")
    
    # Draw black rectangle
    draw_rectangle(img, upper_left, lower_right, "#000000")
