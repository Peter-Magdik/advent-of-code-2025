lights: list[tuple[int]] = []
buttons: list[tuple[tuple[int]]] = []

with open("day_10/input.txt") as f:
    for line in f.read().splitlines():
        l, r = line.split(" ", 1)
        r = r.split(" {")[0]

        temp_lights: list[int] = []
        for char in l:
            if char == ".":
                temp_lights.append(0)
            elif char == "#":
                temp_lights.append(1)
        lights.append(tuple(temp_lights))

        temp_buttons: list[int] = []
        index = 0
        while index < len(r):
            start = r.find("(", index)
            end = r.find(")", index)
            if start == -1 or end == -1:
                break
            index = end + 1
            button = r[start + 1 : end]
            temp_buttons.append(tuple(map(int, button.split(","))))
        buttons.append(tuple(temp_buttons))

solution = 0

for l in range(len(lights)):
    A: list[list[int]] = []
    b: list[int] = lights[l]

    for i in range(len(lights[l])):
        A.append([])
        for button in buttons[l]:
            if i in button:
                A[i].append(1)
            else:
                A[i].append(0)
    
    # Gaussian elimination... lord forgive me what Im about to do
    C = [A[i] + [b[i]] for i in range(len(A))]

    n_lights = len(lights[l])
    n_buttons = len(buttons[l])

    # swaping rows
    pivot_row = 0
    pivot_col_of = {}

    for col in range(n_buttons):
        found = -1
        for row in range(pivot_row, n_lights):
            if C[row][col] == 1:
                found = row
                break
        if found == -1:
            continue

        C[pivot_row], C[found] = C[found], C[pivot_row]
        pivot_col_of[col] = pivot_row

        # reduction
        for row in range(n_lights):
            if row != pivot_row and C[row][col] == 1:
                C[row] = [a ^ b for a, b in zip(C[row], C[pivot_row])]
    
        pivot_row += 1

    for row in C:
        if all(v == 0 for v in row[:-1]) and row[-1] == 1:
            print("No solution for machine: ", l)
            break

    # dealing with free variables
    free_cols = [c for c in range(n_buttons) if c not in pivot_col_of]

    best = float('inf')
    for mask in range(2 ** len(free_cols)): # mask is binary represencation of free variables combinations
        x = [0] * n_buttons
        for i, fc in enumerate(free_cols):
            x[fc] = (mask >> i) & 1 # bit indexing magic here
        
        for col, row in pivot_col_of.items():
            val = C[row][-1]
            for fc in free_cols:
                val ^= C[row][fc] * x[fc]
            x[col] = val
        
        best = min(best, sum(x))

    solution += best

print(solution)