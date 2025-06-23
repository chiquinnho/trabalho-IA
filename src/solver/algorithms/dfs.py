class PuzzleState:
    def __init__(self, board, empty_tile_pos, parent=None):
        self.board = board
        self.empty_tile_pos = empty_tile_pos
        self.parent = parent
        self.depth = 0 if parent is None else parent.depth + 1

    def is_goal(self, goal_state):
        return self.board == goal_state

    def get_possible_moves(self):
        moves = []
        x, y = self.empty_tile_pos
        directions = {
            'up': (x - 1, y),
            'down': (x + 1, y),
            'left': (x, y - 1),
            'right': (x, y + 1)
        }
        for direction, (new_x, new_y) in directions.items():
            if 0 <= new_x < len(self.board) and 0 <= new_y < len(self.board[0]):
                moves.append(direction)
        return moves

    def move(self, direction):
        x, y = self.empty_tile_pos
        new_board = [row[:] for row in self.board]
        if direction == 'up':
            new_board[x][y], new_board[x - 1][y] = new_board[x - 1][y], new_board[x][y]
            return PuzzleState(new_board, (x - 1, y), self)
        elif direction == 'down':
            new_board[x][y], new_board[x + 1][y] = new_board[x + 1][y], new_board[x][y]
            return PuzzleState(new_board, (x + 1, y), self)
        elif direction == 'left':
            new_board[x][y], new_board[x][y - 1] = new_board[x][y - 1], new_board[x][y]
            return PuzzleState(new_board, (x, y - 1), self)
        elif direction == 'right':
            new_board[x][y], new_board[x][y + 1] = new_board[x][y + 1], new_board[x][y]
            return PuzzleState(new_board, (x, y + 1), self)

def dfs(initial_state, goal_state):
    stack = [initial_state]
    visited = set()

    while stack:
        current_state = stack.pop()
        if current_state.is_goal(goal_state):
            return current_state
        visited.add(tuple(map(tuple, current_state.board)))

        for move in current_state.get_possible_moves():
            next_state = current_state.move(move)
            if tuple(map(tuple, next_state.board)) not in visited:
                stack.append(next_state)

    return None