class ManhattanHeuristic:
    @staticmethod
    def calculate(state):
        """
        Calculate the Manhattan distance heuristic for the given puzzle state.

        :param state: A 2D list representing the current state of the puzzle.
        :return: The total Manhattan distance for the current state.
        """
        distance = 0
        n = len(state)
        for i in range(n):
            for j in range(n):
                value = state[i][j]
                if value != 0:  # Ignore the empty space
                    target_x = (value - 1) // n
                    target_y = (value - 1) % n
                    distance += abs(target_x - i) + abs(target_y - j)
        return distance