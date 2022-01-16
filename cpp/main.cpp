
// #include "Sudoku.hpp"
#include "Sudoku.cpp"
#include <vector>
#include <iostream>

using namespace std;


void printBoard(vector<vector<char>>& board) {
    // print board

    for (int row=0; row< board.size(); row++) {

        for (int col=0; col < board.size(); col++) {

            cout << board[row][col] << ", ";
        }
        cout << endl;
    }
}

void printBoard(vector<vector<char>>& board, vector<vector<char>>& ansBoard) {
    // overload to print two puzzles intermixed (ie char:char2), to compare

    for (int row=0; row< board.size(); row++) {

        for (int col=0; col < board.size(); col++) {
            
            cout << board[row][col] << ':' << ansBoard[row][col] << ' ';

        }
        cout << endl;
    }
}


int main() {
    cout << "hello" << endl;
    vector<vector<char>> board1 ={{'5','3','0','0','7','0','0','0','0'},
                                {'6','0','0','1','9','5','0','0','0'},
                                {'0','9','8','0','0','0','0','6','0'},
                                {'8','0','0','0','6','0','0','0','3'},
                                {'4','0','0','8','0','3','0','0','1'},
                                {'7','0','0','0','2','0','0','0','6'},
                                {'0','6','0','0','0','0','2','8','0'},
                                {'0','0','0','4','1','9','0','0','5'},
                                {'0','0','0','0','8','0','0','0','0'}};

    vector<vector<char>> board2 ={{'0','0','9','0','3','2','0','0','0'},
                                {'0','0','0','7','0','0','0','0','0'},
                                {'1','6','2','0','0','0','0','0','0'},
                                {'0','1','0','0','2','0','5','6','0'},
                                {'0','0','0','9','0','0','0','0','0'},
                                {'0','5','0','0','0','0','1','0','7'},
                                {'0','0','0','0','0','0','4','0','3'},
                                {'0','2','6','0','0','9','0','0','0'},
                                {'0','0','5','8','7','0','0','0','0'}};


    SudokuSolver solver = SudokuSolver();
    vector<vector<char>> unchangedBoard1 = board1;
    
    solver.solve( board1 );

    printBoard( unchangedBoard1, board1  );
    cout << endl << endl;


    solver.solve( board2 );
    
    return 0;
}


// #include "Sudoku.hpp"
// #include <iostream>

// int main()
// {
//     std::cout << "The sum of 3 and 4 is " << add(3, 4) << '\n';
//     return 0;
// }