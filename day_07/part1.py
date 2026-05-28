with open("day_07/input.txt") as f:
    board = f.read().splitlines()

beams: set[tuple[int, int]] = set()

beams.add((board[0].find("S"), 0))

def position_is_valid(position: tuple[int, int]) -> bool:
    if position[0] < 0 or position[0] >= len(board[0]):
        return False
    if position[1] < 0 or position[1] >= len(board):
        return False
    return True

solution = 0

for y in range(len(board) - 1):
    for beam in beams.copy():
        new_position = (beam[0], beam[1] + 1)
        if board[new_position[1]][new_position[0]] == "^":
            solution += 1
            left_position = (new_position[0] - 1, new_position[1])
            right_position = (new_position[0] + 1, new_position[1])
            if position_is_valid(left_position):
                beams.add(left_position)
            if position_is_valid(right_position):
                beams.add(right_position)
        else:
            beams.add(new_position)
        beams.remove(beam)

print(solution)