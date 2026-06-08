def point_on_edge(px, py, x1, y1, x2, y2):
    if not (min(x1,x2) <= px <= max(x1,x2) and min(y1,y2) <= py <= max(y1,y2)):
        return False

    cross = (px - x1) * (y2 - y1) - (py - y1) * (x2 - x1)
    return cross == 0

def point_in_polygon(px, py, polygon):
    n = len(polygon)
    inside = False

    j = n - 1
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[j]

        if point_on_edge(px, py, xi, yi, xj, yj):
            return True

        if ((yi > py) != (yj > py)) and (px <= (xj - xi) * (py - yi) / (yj - yi) + xi):
            inside = not inside
        j = i

    return inside

def is_valid_rectangle(rectangle, shape):
    x1, y1 = rectangle[2]
    x2, y2 = rectangle[3]

    rx_min, rx_max = min(x1, x2), max(x1, x2)
    ry_min, ry_max = min(y1, y2), max(y1, y2)

    if not (point_in_polygon(x1, y2, shape)) and ( point_in_polygon(x2, y1, shape)):
        return False

    for px in range(min(x1, x2), max(x1, x2) + 1):
        for py in range(min(y1, y2), max(y1, y2) + 1):
            on_border = (px == rx_min or px == rx_max or py == ry_min or py == ry_max)
        
            dx = rx_max - rx_min
            dy = ry_max - ry_min
            on_diag1 = (dx == 0 or dy == 0) or ((px - rx_min) * dy == (py - ry_min) * dx)
            on_diag2 = (dx == 0 or dy == 0) or ((px - rx_min) * dy == (ry_max - py) * dx)
            
            if not (on_border or on_diag1 or on_diag2):
                continue
            if not point_in_polygon(px, py, shape):
                return False
    return True

with open("day_09/input.txt") as f:
    shape: list[tuple[int, int]] = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]

rectangles: list[tuple[int, int, tuple[int, int], tuple[int, int]]] = list() 

for i in range(len(shape)):
    for j in range(i + 1, len(shape)):
        delta_x = abs(shape[i][0] - shape[j][0]) + 1
        delta_y = abs(shape[i][1] - shape[j][1]) + 1
        rectangles.append((delta_x, delta_y, shape[i], shape[j]))

rectangles.sort(key=lambda x: x[0] * x[1], reverse=True)

for i in range(len(rectangles)):
    if is_valid_rectangle(rectangles[i], shape):
        print(rectangles[i][0] * rectangles[i][1])
        break
    else:
        print(f"Checked {i}/{len(rectangles)}")

# WA: 3010021322