// https://leetcode.com/problems/sudoku-solver

class Solution {
public:

    bool isValid(int row, int col, vector<vector<char>>& board, char c) {
        for(int i = 0; i<9; i++) {
            //check row
            if(board[row][i] == c) return false;
            //check col
            if(board[i][col] == c) return false;
            //check box
            if(board[3*(row/3) + (i/3)][3*(col/3) + (i%3)] == c) return false;
        }
        return true;
    }

    bool helper(vector<vector<char>>& board) {
        for(int i = 0; i<9; i++) {
            for(int j = 0; j<9; j++) {
                if(board[i][j] == '.') {
                    for(char c = '1'; c <= '9'; c++) {
                        if(isValid(i, j, board, c)) {
                            board[i][j] = c;
                            if(helper(board)) return true;
                            board[i][j] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    void solveSudoku(vector<vector<char>>& board) {
        helper(board);
    }
};