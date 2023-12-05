// https://leetcode.com/problems/n-queens

//Solution 1 - traverse column wise

class Solution {
public:

    bool isValid(int row, int col, vector<string>& board, int n) {
        //check left horizontal
        for(int c = 0; c < col ; c++)
            if(board[row][c] == 'Q') return 0;
        //check left upper diagonal
        for(int r = row, c = col; r >=0 && c >=0 ; r--, c--)
            if(board[r][c] == 'Q') return 0;
        //check left lower diagonal
        for(int r = row, c = col; r < n && c >= 0; r++, c--)
            if(board[r][c] == 'Q') return 0;
        return 1; 
    }

    void helper(int col, vector<string>& board, vector<vector<string>>& res, int n) {
        if(col == n) {
            res.push_back(board);
            return;
        }

        for(int row = 0; row<n; row++) {
            if(isValid(row, col, board, n)) {
                board[row][col] = 'Q';
                helper(col+1, board, res, n);
                board[row][col] = '.';
            }
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        vector<string> board(n);
        string s(n, '.');
        for(int i = 0; i<n; i++) 
            board[i] = s;
        helper(0, board, res, n);
        return res;
    }
};

//Solution 2 - traverse row wise

class Solution {
public:

    bool isValid(int row, int col, vector<string>& board, int n) {
        //check vertical
        for(int r = 0; r<row; r++)
            if(board[r][col] == 'Q') return false;
        //check left upper diagonal
        for(int r = row, c = col; r>=0 && c>=0; r--, c--)
            if(board[r][c] == 'Q') return false;
        //check right upper diagonal
        for(int r = row, c = col; r>=0 && c<n; r--, c++)
            if(board[r][c] == 'Q') return false;
        return true;
    }

    void helper(int row, vector<string>& board, vector<vector<string>>& res, int n) {
        if(row == n) {
            res.push_back(board);
            return;
        }

        for(int col = 0; col <n; col++) {
            if(isValid(row, col, board, n)) {
                board[row][col] = 'Q';
                helper(row+1, board, res, n);
                board[row][col] = '.';
            }
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        vector<string> board(n);
        string s(n, '.');
        for(int i = 0; i<n; i++)
            board[i] = s;
        helper(0, board, res, n);
        return res;
    }
};