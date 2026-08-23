successors: dict[str, list[str]] = dict()

with open('day_11/input.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(': ')
        if len(parts) < 2:
            continue
        key = parts[0]
        values = parts[1].split(' ')
        if key in successors:
            successors[key].extend(values)
        else:
            successors[key] = values

paths: set[tuple[str, ...]] = set()
required_nodes: set[str] = {'svr', 'dac', 'fft'}

def dfs(current: str, current_path: list[str], visited: set[str]) -> None:
    print(f"Visiting: {current}, Current Path: {current_path}, Visited: {visited}")
    for successor in successors.get(current, []):
        if successor == 'out' and required_nodes.issubset(set(current_path)):
            paths.add(tuple(current_path + ['out']))
            print(f"Found path: {current_path + ['out']}")
        elif successor not in visited:
            visited.add(successor)
            current_path.append(successor)
            dfs(successor, current_path, visited)
            current_path.pop()
            visited.remove(successor)

print("Starting DFS from 'svr'...")
dfs('svr', ['svr'], {'svr'})
print(len(paths))