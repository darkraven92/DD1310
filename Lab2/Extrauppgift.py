def draw_filled_triangle(img, p1, p2, p3, color):
    # Sortera punkterna så att p1 är längst upp och p3 längst ner
    sorted_points = sorted([p1, p2, p3], key=lambda x: x[1])
    p1, p2, p3 = sorted_points[0], sorted_points[1], sorted_points[2]

    # Räkna ut lutningarna för linjerna mellan punkterna
    if p1[1] != p2[1]:
        m1 = (p2[0] - p1[0]) / (p2[1] - p1[1])
    else:
        m1 = 0

    if p2[1] != p3[1]:
        m2 = (p3[0] - p2[0]) / (p3[1] - p2[1])
    else:
        m2 = 0

    if p1[1] != p3[1]:
        m3 = (p3[0] - p1[0]) / (p3[1] - p1[1])
    else:
        m3 = 0

    # Rita linjer mellan punkterna, fyll i triangeln mellan linjerna
    for y in range(p1[1], p3[1]+1):
        x1 = int(p1[0] + m1 * (y - p1[1]))
        x2 = int(p1[0] + m3 * (y - p1[1]))
        for x in range(x1, x2+1):
            img.put(color, (x, y))
