#ifndef SUDOKU_hpp
#define SUDOKU_hpp

#include <vector>

using namespace std;

class SudokuSolver {
    public:

        bool isLegal(vector<vector<char>>& , int , int , char );

        bool solve(vector<vector<char>>& );
};






#endif

// int addr(int x, int y); 

// int add(int x, int y)
// {
//     return x + y;
// }
