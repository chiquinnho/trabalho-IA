class MisplacedTilesHeuristic:
    def __init__(self, goal_state):
        self.goal_state = goal_state

    def calculate(self, current_state):
        misplaced_tiles = 0
        for i in range(len(current_state)):
            for j in range(len(current_state[i])):
                if current_state[i][j] != self.goal_state[i][j] and current_state[i][j] != 0:
                    misplaced_tiles += 1
        return misplaced_tiles