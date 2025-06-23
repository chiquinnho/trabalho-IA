class PuzzleState:
    def __init__(self, board, empty_tile_pos, moves, depth):
        self.board = board
        self.empty_tile_pos = empty_tile_pos
        self.moves = moves
        self.depth = depth

    def is_goal(self, goal_state):
        return self.board == goal_state

    def get_possible_moves(self):
        possible_moves = []
        x, y = self.empty_tile_pos
        if x > 0:  # Up
            possible_moves.append((x - 1, y))
        if x < len(self.board) - 1:  # Down
            possible_moves.append((x + 1, y))
        if y > 0:  # Left
            possible_moves.append((x, y - 1))
        if y < len(self.board) - 1:  # Right
            possible_moves.append((x, y + 1))
        return possible_moves

    def move_tile(self, new_empty_tile_pos):
        new_board = [row[:] for row in self.board]
        x, y = self.empty_tile_pos
        new_x, new_y = new_empty_tile_pos
        new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
        return PuzzleState(new_board, new_empty_tile_pos, self.moves + [new_empty_tile_pos], self.depth + 1)

def bfs(initial_state, goal_state):
    from collections import deque
    queue = deque([initial_state])
    visited = set()
    visited.add(tuple(map(tuple, initial_state.board)))

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal(goal_state):
            return current_state.moves, current_state.depth

        for move in current_state.get_possible_moves():
            new_state = current_state.move_tile(move)
            if tuple(map(tuple, new_state.board)) not in visited:
                visited.add(tuple(map(tuple, new_state.board)))
                queue.append(new_state)

    return None, None  # No solution found