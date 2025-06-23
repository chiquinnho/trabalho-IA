# n-puzzle Solver

This project implements a solution for the n-puzzle problem using various search algorithms and heuristics. It provides both a graphical user interface (GUI) and a command-line interface (CLI) for user interaction.

## Overview

The n-puzzle is a classic problem in artificial intelligence and computer science, where the objective is to rearrange a set of numbered tiles on a grid to achieve a specific goal configuration. This project allows users to solve the 8-puzzle (3x3), 15-puzzle (4x4), and 24-puzzle (5x5) using different algorithms.

## Features

- **Multiple Search Algorithms**: Implementations of BFS, DFS, IDS, Greedy Best-First Search, and A* algorithms.
- **Heuristics**: Two heuristics for informed search: number of misplaced tiles and Manhattan distance.
- **User Interfaces**: Both a GUI for visual interaction and a CLI for terminal-based interaction.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/n_puzzle_solver_ui.git
   ```
2. Navigate to the project directory:
   ```
   cd n_puzzle_solver_ui
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Running the GUI

To start the graphical user interface, run the following command:
```
python src/main.py --gui
```

### Running the CLI

To start the command-line interface, run:
```
python src/main.py --cli
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.