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

print(shapes)
print(christmas_tree_regions)