with open("day_04/input.txt") as f:
    lines = f.read().splitlines()

neighbours = (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)
answer = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        number_of_adjacent_at_symbols = 0
        char = lines[y][x]
        if char != "@":
            continue
        for dx, dy in neighbours:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(lines[y]) and 0 <= ny < len(lines):
                if lines[ny][nx] == "@":
                    number_of_adjacent_at_symbols += 1

        if number_of_adjacent_at_symbols < 4: answer += 1

print(answer)