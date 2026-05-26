with open("day_05/input.txt") as f:
    ranges: list[range] = []
    while True:
        line = f.readline()
        if line == "\n":
            break

        start, end = line.split("-")
        ranges.append((int(start), int(end)))

ranges.sort()
merged = [ranges[0]]
for start, end in ranges[1:]:
    if start <= merged[-1][1] + 1:
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

total_ids = sum(end - start + 1 for start, end in merged)
print(total_ids)

# too low: 346430794751279