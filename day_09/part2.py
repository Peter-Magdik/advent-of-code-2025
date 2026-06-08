def is_valid_rectangle(rectangle):
    x1, y1 = rectangle[2]
    x2, y2 = rectangle[3]

    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)

    for (px1, py1), (px2, py2) in polygon_edges:
        if py1 == py2:
            if y_min < py1 < y_max and min(px1,px2) < x_max and max(px1,px2) > x_min:
                return False
        else:
            if x_min < px1 < x_max and min(py1,py2) < y_max and max(py1,py2) > y_min:
                return False
    
    return True

with open("day_09/input.txt") as f:
    shape: list[tuple[int, int]] = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]

polygon_edges: list[tuple[tuple[int, int], tuple[int, int]]] = list()
for index in range(len(shape) - 1):
    polygon_edges.append((shape[index], shape[index + 1]))
polygon_edges.append((shape[-1], shape[0]))

rectangles: list[tuple[int, int, tuple[int, int], tuple[int, int]]] = list() 

for i in range(len(shape)):
    for j in range(i + 1, len(shape)):
        delta_x = abs(shape[i][0] - shape[j][0]) + 1
        delta_y = abs(shape[i][1] - shape[j][1]) + 1
        rectangles.append((delta_x, delta_y, shape[i], shape[j]))

rectangles.sort(key=lambda x: x[0] * x[1], reverse=True)

for i in range(len(rectangles)):
    if is_valid_rectangle(rectangles[i]):
        print(rectangles[i][0] * rectangles[i][1])
        break
    else:
        print(f"Checked {i}/{len(rectangles)}")