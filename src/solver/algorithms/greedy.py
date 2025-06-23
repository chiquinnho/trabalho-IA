class GreedySearch:
    def __init__(self, puzzle, heuristic):
        self.puzzle = puzzle
        self.heuristic = heuristic
        self.open_set = []
        self.closed_set = set()

    def search(self):
        self.open_set.append(self.puzzle)
        while self.open_set:
            current = self.get_best_node()
            if current.is_goal():
                return self.reconstruct_path(current)
            self.open_set.remove(current)
            self.closed_set.add(current)
            for neighbor in current.get_neighbors():
                if neighbor in self.closed_set:
                    continue
                if neighbor not in self.open_set:
                    self.open_set.append(neighbor)
        return None

    def get_best_node(self):
        return min(self.open_set, key=lambda node: self.heuristic(node))

    def reconstruct_path(self, current):
        path = []
        while current:
            path.append(current)
            current = current.parent
        return path[::-1]  # Return reversed path

def misplaced_tiles(puzzle):
    return sum(1 for i in range(len(puzzle)) for j in range(len(puzzle[i])) if puzzle[i][j] != 0 and puzzle[i][j] != goal[i][j])

def manhattan_distance(puzzle):
    distance = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] != 0:
                goal_x, goal_y = divmod(puzzle[i][j] - 1, len(puzzle))
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Example goal state for 8-puzzle