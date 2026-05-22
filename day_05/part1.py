with open("day_05/input.txt") as f:
    ranges: list[range] = []
    while True:
        line = f.readline()
        if line == "\n":
            break

        start, end = line.split("-")
        ranges.append(range(int(start), int(end) + 1))

    food = set()
    for line in f:
        food.add(line.strip())

answer = 0
for f in food:
    for r in ranges:
        if int(f) in r:
            answer += 1
            break

print(answer)