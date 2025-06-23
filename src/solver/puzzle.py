class Puzzle:
    def __init__(self, state):
        self.state = state
        self.empty_tile = self.find_empty_tile()
        self.size = len(state)

    def find_empty_tile(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.state[i][j] == 0:
                    return (i, j)

    def move(self, direction):
        x, y = self.empty_tile
        if direction == 'up' and x > 0:
            self.state[x][y], self.state[x - 1][y] = self.state[x - 1][y], self.state[x][y]
            self.empty_tile = (x - 1, y)
        elif direction == 'down' and x < self.size - 1:
            self.state[x][y], self.state[x + 1][y] = self.state[x + 1][y], self.state[x][y]
            self.empty_tile = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.state[x][y], self.state[x][y - 1] = self.state[x][y - 1], self.state[x][y]
            self.empty_tile = (x, y - 1)
        elif direction == 'right' and y < self.size - 1:
            self.state[x][y], self.state[x][y + 1] = self.state[x][y + 1], self.state[x][y]
            self.empty_tile = (x, y + 1)

    def is_solved(self):
        goal_state = list(range(1, self.size * self.size)) + [0]
        return self.state == [goal_state[i:i + self.size] for i in range(0, len(goal_state), self.size)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.state])