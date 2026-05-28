class Position:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def position_is_valid(self) -> bool:
        if self.x < 0 or self.x >= len(board[0]):
            return False
        if self.y < 0 or self.y >= len(board):
            return False
        return True
    
    def translate(self, dx: int, dy: int) -> "Position":
        return Position(x=self.x + dx, y=self.y + dy)

    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        if not isinstance(other, Position):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

# --------------------------------- #

with open("day_07/input.txt") as f:
    board = f.read().splitlines()

nodes: dict[Position, int] = {}
nodes[Position(x=board[0].find("S"), y=0)] = 1

for y in range(len(board)):
    for pos in [node for node in nodes if node.y == y]:
        if board[pos.y][pos.x] == "^":
            left_pos = pos.translate(-1, 2)
            right_pos = pos.translate(1, 2)
            if left_pos.position_is_valid():
                nodes[left_pos] = (nodes.get(left_pos, 0) + nodes[pos])
            if right_pos.position_is_valid():
                nodes[right_pos] = (nodes.get(right_pos, 0) + nodes[pos])
        else:
            down = pos.translate(0, 2)
            nodes[down] = (nodes.get(down, 0) + nodes[pos])

print(sum([nodes[pos] for pos in nodes if pos.y >= len(board)]))