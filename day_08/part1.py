"""
Advent of Code
Where your worst enemy is reading and understanding the problem statement.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    x: int
    y: int
    z: int

def distance(p1: Position, p2: Position) -> float:
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)**0.5

positions = []
with open("day_08/input.txt") as f:
    for line in f:
        line = line.strip()
        if line:
            positions.append(Position(*map(int, line.split(","))))

n = len(positions)

parent = list(range(n))
size = [1] * n

def find(x) -> int:
    while parent[x] != x:
        x = parent[x]
    return x

def union(a, b) -> bool:
    a, b = find(a), find(b)
    if a == b:
        return False
    if size[a] < size[b]:
        a, b = b, a
    parent[b] = a
    size[a] += size[b]
    return True

pairs = []
for i in range(n):
    for j in range(i + 1, n):
        d = distance(positions[i], positions[j])
        pairs.append((d, i, j))

pairs.sort()

connections = 0
for d, i, j in pairs:
    if connections == 1000:
        break
    union(i, j)
    connections += 1

root_sizes = {}
for i in range(n):
    r = find(i)
    root_sizes[r] = root_sizes.get(r, 0) + 1

sizes = sorted(root_sizes.values(), reverse=True)
print(sizes[0] * sizes[1] * sizes[2])