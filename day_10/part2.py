from scipy.optimize import LinearConstraint, Bounds, milp
import numpy as np

buttons: list[tuple[tuple[int]]] = []
voltage: list[tuple[int]] = []

with open("day_10/input.txt") as f:
    for line in f.read().splitlines():
        _, r = line.split(" ", 1)
        l, r = r.split(" {")

        temp_buttons: list[int] = []
        index = 0
        while index < len(l):
            start = l.find("(", index)
            end = l.find(")", index)
            if start == -1 or end == -1:
                break
            index = end + 1
            button = l[start + 1 : end]
            temp_buttons.append(tuple(map(int, button.split(","))))
        buttons.append(tuple(temp_buttons))

        voltage.append(tuple(map(int, r[:-1].split(","))))

solution = 0

for l in range(len(voltage)):
    A: list[list[int]] = []
    b: list[int] = voltage[l]

    n_buttons = len(buttons[l])

    for i in range(len(voltage[l])):
        A.append([])
        for button in buttons[l]:
            if i in button:
                A[i].append(1)
            else:
                A[i].append(0)
    
    c = [1] * n_buttons

    constraints = LinearConstraint(np.array(A), b, b)
    bounds = Bounds(lb=0)

    result = milp(c, constraints=constraints, bounds=bounds, integrality=c)

    solution += int(result.fun)

print(solution)