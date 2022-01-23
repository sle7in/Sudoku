

class SudokuSolver:
    def __init__(self, board):

        self.sqrt = int(pow(len(board), 0.5))

        self.columns = []
        self.rows = []
        self.grids = []

        self._possible( board )


    def _possible(self, board):
        "use sets of possible numbers"

        # ================ check row for n =========================
        for i in range(len(board)):
            h = set( range(1, 10) )
            for j in range(len(board)):
                if board[i][j] in h:
                    h.remove(board[i][j])
            self.rows.append(h)

        # ================ check col position for n ================
        for i in range(len(board)):
            h = set( range(1, 10) )
            for j in range(len(board)):
                if board[j][i] in h:
                    h.remove(board[j][i])
            self.columns.append(h)

        # ================ group the rows/cols by grid ==============
        for i in range(0, len(board), self.sqrt):
            for j in range(0, len(board), self.sqrt):
                h = set( range(1, 10) )
                for x in range(i, i + self.sqrt):
                    for y in range(j, j + self.sqrt):
                        if board[x][y] in h:
                            h.remove(board[x][y])
                self.grids.append(h)


    def solve(self, row=0, col=0 ):
        """
        Try number 1-9 in each square in the board to see if possible.
        return first solved board.

        Create set of possible numbers for each row and col and grid.
        Modify board in-place with recursive helper.
        Unsuccessful combination forces backtrack.
        """

        if row == 9 and col == 0:
            return True

        nx_row = row + (col + 1) // len(board)
        nx_col = (col + 1) % len(board)
        if board[row][col] != 0:
            return self.solve(nx_row, nx_col)

        # grid number calculation
        grid = (row // self.sqrt) * self.sqrt + col // self.sqrt
        valid_set = self.rows[row].intersection(self.columns[col].intersection(self.grids[grid]))

        # no solution, return false
        if not valid_set:
            return False

        for num in valid_set:
            # set board position to first number
            board[row][col] = num

            self.rows[row].remove(num)
            self.columns[col].remove(num)
            self.grids[grid].remove(num)

            # if valid set on all recursions, return True, else backtrack
            if self.solve(nx_row, nx_col):
                return True

            self.rows[row].add(num)
            self.columns[col].add(num)
            self.grids[grid].add(num)

        # if it gets this far none of valid_set work. Backtrack.
        board[row][col] = 0
        return False


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