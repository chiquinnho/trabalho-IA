def print_board(board):
    for row in board:
        print(" ".join(str(tile) if tile != 0 else " " for tile in row))
    print()

def is_solvable(board):
    flat_board = [tile for row in board for tile in row]
    inversions = sum(
        1 for i in range(len(flat_board)) for j in range(i + 1, len(flat_board))
        if flat_board[i] != 0 and flat_board[j] != 0 and flat_board[i] > flat_board[j]
    )
    return inversions % 2 == 0

def find_empty_tile(board):
    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            if tile == 0:
                return i, j
    return None

def get_possible_moves(board):
    moves = []
    empty_row, empty_col = find_empty_tile(board)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dr, dc in directions:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
            moves.append((new_row, new_col))

    return moves

def make_move(board, move):
    empty_row, empty_col = find_empty_tile(board)
    new_row, new_col = move
    new_board = [row[:] for row in board]  # Create a copy of the board
    new_board[empty_row][empty_col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[empty_row][empty_col]
    return new_board

def board_to_tuple(board):
    return tuple(tuple(row) for row in board)