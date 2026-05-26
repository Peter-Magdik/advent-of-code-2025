with open("day_06/input.txt") as f:
    problems = []
    for line in f.read().splitlines():
        problems.append(list(filter(lambda x: x != "", line.strip().split(" "))))
    
    for i in range(len(problems) - 1):
        problems[i] = list(map(int, problems[i]))

solution = 0

for x in range(len(problems[-1])):
    operator = problems[-1][x]
    problem_solution = problems[0][x]
    for y in range(1, len(problems) - 1):
        if operator == "*":
            problem_solution *= problems[y][x]
        else: # +
            problem_solution += problems[y][x]
    
    solution += problem_solution

print(solution)