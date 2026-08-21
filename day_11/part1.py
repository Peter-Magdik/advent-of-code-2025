successors: dict[str, list[str]] = dict()

with open('input.txt', 'r') as file:
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

nodes: dict[str, int] = {key: 0 for key in successors.keys()}
nodes['you'] = 1
nodes['out'] = 0
current_key = 'you'

def update_num_of_possible_paths(key: str) -> None:
    if key not in successors or key == 'out':
        return
    for successor in successors[key]:
        nodes[successor] += 1
        update_num_of_possible_paths(successor)

update_num_of_possible_paths(current_key)
print(nodes['out'])