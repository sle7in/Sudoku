// This file is Sudoku.cpp

#include "Sudoku.hpp"

#include <vector>
#include <cassert>
#include <math.h>


using namespace std;


bool SudokuSolver::isLegal(vector<vector<char>>& board, int row, int col, char ch) {

    // board.size() must be perfect square
    int grid = pow( board.size(), 0.5);

    // check row
    for (int i=0; i<board.size(); i++) {

        if (board[i][col] == ch) {

            return false;
        }
    }

    // check  column
    for (int j=0; j<board.size(); j++) {

        if (board[row][j] == ch) {

            return false;
        }
    }
    
    // check grid
    // can use while loop and skip row/col that have already been checked.
    // performance at high board size
    for (int k= row/grid * grid; k < row/grid*grid + grid; k++) {

        for (int l= col/grid * grid; l < col/grid*grid + grid; l++) {

            if (board[k][l] == ch) {

                return false;
            }
        }
    }

    return true;
};


bool SudokuSolver::solve(vector<vector<char>>& board) {

    // //board size is not a perfect square
    // assert(board.size() / pow(board.size(), 0.5) == pow(board.size(), 0.5));


    for (int row=0; row< board.size(); row++) {

        for (int col=0; col< board.size(); col++) {

            if (board[row][col] == '0') {

                for (char ch='1'; ch<='9'; ch++) {

                    if (isLegal(board, row, col, ch)) {

                        board[row][col] = ch;

                        if (solve( board )) {

                            return true;

                        } else {
                            
                            board[row][col] = '0';
                        }
                    }
                }
            return false;
            }
        }
    }

    return true;
};


// #include "Sudoku.hpp"


// int add(int x, int y)
// {
//     return x * y;
// }


