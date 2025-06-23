class PuzzleState:
    def __init__(self, puzzle, empty_tile_pos, depth=0, parent=None):
        self.puzzle = puzzle
        self.empty_tile_pos = empty_tile_pos
        self.depth = depth
        self.parent = parent

    def is_goal(self, goal_state):
        return self.puzzle == goal_state

    def get_possible_moves(self):
        moves = []
        x, y = self.empty_tile_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(self.puzzle) and 0 <= new_y < len(self.puzzle[0]):
                new_puzzle = [row[:] for row in self.puzzle]
                new_puzzle[x][y], new_puzzle[new_x][new_y] = new_puzzle[new_x][new_y], new_puzzle[x][y]
                moves.append((new_puzzle, (new_x, new_y)))

        return moves

def iterative_deepening_search(initial_state, goal_state):
    depth = 0
    while True:
        result = depth_limited_search(initial_state, goal_state, depth)
        if result is not None:
            return result
        depth += 1

def depth_limited_search(state, goal_state, limit):
    if state.is_goal(goal_state):
        return state
    if state.depth == limit:
        return None

    for new_puzzle, new_empty_tile_pos in state.get_possible_moves():
        new_state = PuzzleState(new_puzzle, new_empty_tile_pos, state.depth + 1, state)
        result = depth_limited_search(new_state, goal_state, limit)
        if result is not None:
            return result

    return None