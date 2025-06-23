from tkinter import Tk, Frame, Button, Label, StringVar, messagebox
from solver.puzzle import Puzzle  # Assuming Puzzle class is defined in puzzle.py
from solver.algorithms.bfs import bfs  # Assuming BFS algorithm is defined in bfs.py
from solver.algorithms.dfs import dfs  # Assuming DFS algorithm is defined in dfs.py
from solver.algorithms.ids import ids  # Assuming IDS algorithm is defined in ids.py
from solver.algorithms.greedy import greedy  # Assuming Greedy algorithm is defined in greedy.py
from solver.algorithms.astar import astar  # Assuming A* algorithm is defined in astar.py

class NPuzzleSolverGUI:
    def __init__(self, master):
        self.master = master
        master.title("N-Puzzle Solver")

        self.frame = Frame(master)
        self.frame.pack()

        self.label = Label(self.frame, text="Enter Puzzle Configuration:")
        self.label.pack()

        self.puzzle_input = StringVar()
        self.entry = Entry(self.frame, textvariable=self.puzzle_input)
        self.entry.pack()

        self.solve_button = Button(self.frame, text="Solve", command=self.solve_puzzle)
        self.solve_button.pack()

        self.result_label = Label(self.frame, text="")
        self.result_label.pack()

    def solve_puzzle(self):
        puzzle_str = self.puzzle_input.get()
        try:
            puzzle = self.parse_puzzle_input(puzzle_str)
            solution = self.run_solver(puzzle)
            self.result_label.config(text=f"Solution: {solution}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def parse_puzzle_input(self, puzzle_str):
        # Convert input string to a Puzzle object
        # Example input: "1 2 3 4 5 6 7 0 8"
        tiles = list(map(int, puzzle_str.split()))
        size = int(len(tiles) ** 0.5)
        return Puzzle(tiles, size)

    def run_solver(self, puzzle):
        # Example of running BFS, can be modified to choose different algorithms
        return bfs(puzzle)

if __name__ == "__main__":
    root = Tk()
    gui = NPuzzleSolverGUI(root)
    root.mainloop()