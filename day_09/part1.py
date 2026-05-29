with open("day_09/input.txt") as f:
    positions: list[tuple[int, int]] = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]

max_delta = 0

for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
        delta_x = abs(positions[i][0] - positions[j][0]) + 1
        delta_y = abs(positions[i][1] - positions[j][1]) + 1
        if delta_x * delta_y > max_delta:
            max_delta = delta_x * delta_y

print(max_delta)