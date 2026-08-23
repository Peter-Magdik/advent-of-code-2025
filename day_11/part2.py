from functools import lru_cache


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
# start: svr
# required: dac, fft
# end: out
required_index = {
    'dac': 0,
    'fft': 1
}
FULL_MASK = (1 << len(required_index)) - 1

@lru_cache(maxsize=None)
def dp(node, mask):
    if node == 'out':
        return 1 if mask == FULL_MASK else 0

    total = 0
    for successor in successors[node]:
        new_mask = mask
        if successor in required_index:
            new_mask |= (1 << required_index[successor])
        total += dp(successor, new_mask)
    
    return total

print(dp('svr', 0b0))