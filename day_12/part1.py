shapes: dict[int, list[str]] = {}
christmas_tree_regions: list[tuple[int, int, tuple[int, ...]]] = []

with open('day_12/input.txt') as f:
    parsing_shape = False
    current_shape = None

    for line in f:
        line = line.strip()

        if not line:
            parsing_shape = False
            continue

        if line.endswith(':'): # indexing of a new shape
            current_shape = int(line[:-1])
            shapes[current_shape] = []
            parsing_shape = True
        elif parsing_shape:
            shapes[current_shape].append(line)
        else: # parsing regions
            dimensions, number_of_shapes = line.split(': ')
            width, height = map(int, dimensions.split('x'))
            number_of_shapes = tuple(map(int, number_of_shapes.split(' ')))
            christmas_tree_regions.append((width, height, number_of_shapes))
"""
# converting shapes to bitmap
# 3x3 is converted to 9 bit long int from left to right, top to bottom
bitmap_shapes: dict[int, int] = {}
# bitmap is in reverse
for shape_id, lines in shapes.items():
    bitmap = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                bitmap |= 1 << (y * 3 + x)
    bitmap_shapes[shape_id] = bitmap
    print(f"Shape {shape_id} -> {bitmap:09b}")

"""

# this should not worked, but it did ...
shapes_space_count: dict[int, int] = {}
for shape_id, lines in shapes.items():
    space_count = sum(line.count('#') for line in lines)
    shapes_space_count[shape_id] = space_count

result = 0
for width, height, number_of_shapes in christmas_tree_regions:
    total_space = width * height
    total_shapes_space = sum(shapes_space_count[shape_id] * count for shape_id, count in zip(shapes_space_count.keys(), number_of_shapes))
    if total_shapes_space <= total_space:
        result += 1

print(result)