import numpy as np



def possible(y,x,n):
    """Brute force checker.
    checks n's row, col, and box for itself, if n is not present, return True.
    Parameters:
        y is the grid row position
        x is the grid col position
        n is the number to check
        """
    
    # ================ check col position for n ================
    for col in range(9):
        if grid[y][col] == n:
            return False
    # ================ check row for n =========================

    for row in range(9):
        if grid[row][x] == n:
            return False

    # ================ group the rows/cols by box ==============
    # find start index for the box
    box_start_col = (x//3)*3
    box_start_row = (y//3)*3
    for box_row in range(3):
        for box_col in range(3):
            if grid[box_start_row + box_row][box_start_col + box_col] == n:
                return False

    return True 

## Solve function, recursive function that tries one square at a time, if the number is possible it is set as the value
## if the number is not possible the value is placed at zero
## built to solve more than one solution 
def solve(grid):
    """Try number 1-9 in each square in the grid to see if possible.
    return first solved grid."""
    
    for row in range(9):
        for col in range(9):

            min_empty = 5
            # if position is empty
            # num empty rows < min_empty
            # num empty cols < min_empty
            # num empty cells in box < min_empty

            if grid[row][col] == 0 and \
                (grid[row].count(0) < min_empty or \
                [grid[row][col] for col in range(len(grid[row]))].count(0) < min_empty or \
                ([grid[row//3*3 + r][col] for r in range(len(grid[row])//3)] + 
                [grid[row][col//3*3 + c] for c in range(len(grid[row])//3)]).count(0) < min_empty):

                for n in range(1,10):
                    if possible(row, col, n):
                        # set value to n and solve again
                        grid[row][col] = n
                        grid = solve(grid)
                        grid[row][col] = 0

                return grid
    
    # "recursive" function is actually just printing solutions as they come
    # need to optimize to have end point rather than just "every possiblity tried".
    print(np.matrix(grid))
    return grid
    
def solve2(grid):
    """Try number 1-9 in each square in the grid to see if possible.
    return first solved grid."""
    
    for row in range(9):
        for col in range(9):

            min_empty = 9
            # if position is empty
            # num empty rows < min_empty
            # num empty cols < min_empty
            # num empty cells in box < min_empty

            if grid[row][col] == 0 and \
                (grid[row].count(0) < min_empty or \
                [grid[row][col] for col in range(len(grid[row]))].count(0) < min_empty or \
                ([grid[row//3*3 + r][col] for r in range(len(grid[row])//3)] + 
                [grid[row][col//3*3 + c] for c in range(len(grid[row])//3)]).count(0) < min_empty):

                for n in range(1,10):
                    if possible(row, col, n):
                        # set value to n and solve again
                        grid[row][col] = n
                        grid = solve(grid)
                        grid[row][col] = 0

                return grid
    
    # "recursive" function is actually just printing solutions as they come
    # need to optimize to have end point rather than just "every possiblity tried".
    print(np.matrix(grid))
    return grid

# def find_last_n(grid_subset):
#     "find last possible int n from grid_subset. (each subset is a set)"
#     all_n = set(range(len(grid_subset)))
#     return set(grid_subset) - all_n

# def eliminate(grid):
#     """recursive solve for X by X grid.
#     grid must be at least 1x1"""

#     for row in range(len(grid)):
        
#         # recursive fallback
#         # check each row, col, and box for final digit
#         full_row = grid[row]
#         if full_row.count(0) == 1:
#             full_row.index(0) == find_last_n(full_row)

#         # check each col and box as progress though rows
#         full_col = [grid[row][col] for col in range(len(grid))]
#         if full_col.count(0) == 1:
#             full_col.index(0) == find_last_n(full_col)

#         for col in range(len(grid[0])):





if __name__ == "__main__":

    # define the grid layout which is the puzzle, uses numpy library 
    # 0 represents an empty grid
    grid =[[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,0]]

    grid1 =[[0,0,9,0,3,2,0,0,0],
        [0,0,0,7,0,0,0,0,0],
        [1,6,2,0,0,0,0,0,0],
        [0,1,0,0,2,0,5,6,0],
        [0,0,0,9,0,0,0,0,0],
        [0,5,0,0,0,0,1,0,7],
        [0,0,0,0,0,0,4,0,3],
        [0,2,6,0,0,9,0,0,0],
        [0,0,5,8,7,0,0,0,0]]

    print("Sudoku Puzzle:\n", np.matrix(grid))

    # solve(grid)
    import timeit
    print(timeit.timeit('solve(grid)', 'from __main__ import solve, grid'), number = 5)
    print(timeit.timeit('solve2(grid)', 'from __main__ import solve, grid'), number = 5)