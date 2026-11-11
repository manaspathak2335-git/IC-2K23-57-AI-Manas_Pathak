def print_board(board):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("-" * 21)
        for c in range(9):
            if c % 3 == 0 and c != 0:
                print("|", end=" ")
            val = board[r][c]
            print(val if val != 0 else ".", end=" ")
        print()


def get_valid_numbers(board, row, col):
    used = set()

    for i in range(9):
        used.add(board[row][i])
        used.add(board[i][col])

    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3
    for r in range(box_start_row, box_start_row + 3):
        for c in range(box_start_col, box_start_col + 3):
            used.add(board[r][c])

    return set(range(1, 10)) - used


def find_best_empty_cell(board):
    best_cell = None
    best_options = None
    min_count = 10  

    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                options = get_valid_numbers(board, r, c)

                if len(options) == 0:
                    return r, c, set()

                if len(options) < min_count:
                    min_count = len(options)
                    best_cell = (r, c)
                    best_options = options

                    if min_count == 1:
                        return r, c, best_options

    if best_cell is None:
        return None, None, None  

    return best_cell[0], best_cell[1], best_options


def is_initial_board_valid(board):
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val != 0:
                board[r][c] = 0 
                if val not in get_valid_numbers(board, r, c):
                    board[r][c] = val
                    return False
                board[r][c] = val
    return True


def solve_sudoku(board):
    row, col, options = find_best_empty_cell(board)

    if row is None:
        return True

    for num in options:
        board[row][col] = num  

        if solve_sudoku(board):  
            return True

        board[row][col] = 0  

    return False  


def get_user_input():
    print("Enter your Sudoku puzzle row by row (9 rows total).")
    print(
        "Use '0' or '.' for empty cells. You can enter digits with or without spaces."
    )
    print(
        "(Or press Enter on the first line to run a sample puzzle):\n"
    )

    board = []
    for i in range(9):
        while True:
            raw = input(f"Row {i + 1}: ").strip()

            if i == 0 and raw == "":
                print("\nLoading sample Sudoku puzzle...")
                return [
                    [5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9],
                ]

            cleaned = [
                int(ch) for ch in raw.replace(".", "0") if ch.isdigit()
            ]

            if len(cleaned) == 9:
                board.append(cleaned)
                break
            else:
                print(
                    "  Invalid row! Please enter exactly 9 digits (0-9)."
                )

    return board


if __name__ == "__main__":
    sudoku_board = get_user_input()

    print("\nInitial Sudoku Board:")
    print_board(sudoku_board)

    if not is_initial_board_valid(sudoku_board):
        print(
            "\nError: The input board violates Sudoku rules (duplicate numbers in a row, column, or box)."
        )
    elif solve_sudoku(sudoku_board):
        print("\nSolved Sudoku Board:")
        print_board(sudoku_board)
    else:
        print("\nNo valid solution exists for this Sudoku puzzle.")
