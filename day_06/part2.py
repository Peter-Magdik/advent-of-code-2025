import math

with open("day_06/input.txt") as f:
    lines = f.read().splitlines()

solution = 0

problems = lines[:-1]
operators = lines[-1]
x = 0
while x < len(operators):
    if operators[x] in ["+", "*"]:
        left_index = x
        plus_index = operators.index("+", x + 1) if "+" in operators[x + 1:] else math.inf
        product_index = operators.index("*", x + 1) if "*" in operators[x + 1:] else math.inf
        right_index = min(plus_index, product_index) - 1 if min(plus_index, product_index) != math.inf else len(operators)
        x = right_index + 1

        numbers = ["" for _ in range(left_index, right_index)]
        for index in range(left_index, right_index):
            for problem in problems:
                if problem[index] != " ":
                    numbers[index- left_index] += problem[index]
        
        if operators[left_index] == "+":
            solution += sum(int(n) for n in numbers)
        elif operators[left_index] == "*":
            product = 1
            for n in numbers:
                product *= int(n)
            solution += product
    else: 
        x += 1
            
print(solution)


# I just need to parse the data in raw state and then apply the operations in the correct order
#Note: every space matter which is crazy