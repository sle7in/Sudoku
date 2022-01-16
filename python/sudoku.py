

class SudokuSolver():
    
    def possible(self, board, y, x, n):
        """Brute force checker.
        checks n's row, col, and box for itself, if n is not present, return True.
        Parameters:
            y is the board row position
            x is the board col position
            n is the number to check
            """
        
        # ================ check col position for n ================
        for col in range(9):
            if board[y][col] == n:
                return False
        # ================ check row for n =========================

        for row in range(9):
            if board[row][x] == n:
                return False

        # ================ group the rows/cols by box ==============
        # find start index for the box
        box_start_col = (x//3)*3
        box_start_row = (y//3)*3
        for box_row in range(3):
            for box_col in range(3):
                if board[box_start_row + box_row][box_start_col + box_col] == n:
                    return False

        return True 

    
    def solve(self, board):
        """Try number 1-9 in each square in the board to see if possible.
        return first solved board.

        recursive function that tries one square at a time, if the number is possible it is set as the value
        if the number is not possible the value is placed at zero
        built to solve more than one solution 
        """
        
        for row in range(9):
            for col in range(9):

                min_empty = 5
                # if position is empty
                # num empty rows < min_empty
                # num empty cols < min_empty
                # num empty cells in box < min_empty

                if board[row][col] == 0 and \
                    (board[row].count(0) < min_empty or \
                    [board[row][col] for col in range(len(board[row]))].count(0) < min_empty or \
                    ([board[row//3*3 + r][col] for r in range(len(board[row])//3)] + 
                    [board[row][col//3*3 + c] for c in range(len(board[row])//3)]).count(0) < min_empty):

                    for n in range(1,10):
                        if self.possible(board, row, col, n):
                            # set value to n and solve again
                            board[row][col] = n
                            board = self.solve(board)
                            board[row][col] = 0

                    return board
        
        # "recursive" function is actually just printing solutions as they come
        # need to optimize to have end point rather than just "every possiblity tried".
        print(board)
        return board



if __name__ == "__main__":

    # define the board layout which is the puzzle, uses numpy library 
    # 0 represents an empty board
    board =[[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,0]]

    board2 =[[0,0,9,0,3,2,0,0,0],
        [0,0,0,7,0,0,0,0,0],
        [1,6,2,0,0,0,0,0,0],
        [0,1,0,0,2,0,5,6,0],
        [0,0,0,9,0,0,0,0,0],
        [0,5,0,0,0,0,1,0,7],
        [0,0,0,0,0,0,4,0,3],
        [0,2,6,0,0,9,0,0,0],
        [0,0,5,8,7,0,0,0,0]]

    s = SudokuSolver()
    s.solve(board)
    print("Sudoku Puzzle:\n", board)

    # solve(board)
    import timeit
    print(timeit.timeit('s.solve(board)', 'from __main__ import SudokuSolver, board;s=SudokuSolver()', number=4))