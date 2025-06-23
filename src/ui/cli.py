# CLI for N-Puzzle Solver

class NPuzzleCLI:
    def __init__(self):
        self.commands = {
            'solve': self.solve_puzzle,
            'exit': self.exit_program
        }

    def display_welcome(self):
        print("Welcome to the N-Puzzle Solver!")
        print("Available commands:")
        print("1. 'solve' - Solve an N-Puzzle")
        print("2. 'exit' - Exit the program")

    def get_user_input(self):
        return input("Enter command: ").strip().lower()

    def solve_puzzle(self):
        initial_state = input("Enter the initial state of the puzzle (e.g., '1 2 3 4 5 6 0 7 8'): ")
        # Here you would parse the input and call the solver
        # For now, we will just print the input
        print(f"Solving puzzle with initial state: {initial_state}")
        # Call the solver function here

    def exit_program(self):
        print("Exiting the N-Puzzle Solver. Goodbye!")
        exit()

    def run(self):
        self.display_welcome()
        while True:
            command = self.get_user_input()
            if command in self.commands:
                self.commands[command]()
            else:
                print("Unknown command. Please try again.")

if __name__ == "__main__":
    cli = NPuzzleCLI()
    cli.run()