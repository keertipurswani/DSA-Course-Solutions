//https://leetcode.com/problems/n-queens

//Solution 1 - Traverse row wise

class Solution {

    static List<String> construct(char[][] board) {
        List<String> res = new LinkedList<>();
        for (int i = 0; i < board.length; i++) {
            // Create a new string for each row
            res.add(new String(board[i]));
        }
        return res;
    }

    private boolean isValid(int row, int col, char[][] board, int n) {
        // Check vertical
        for (int r = 0; r < row; r++) {
            if (board[r][col] == 'Q') {
                return false;
            }
        }

        // Check left upper diagonal
        for (int r = row, c = col; r >= 0 && c >= 0; r--, c--) {
            if (board[r][c] == 'Q') {
                return false;
            }
        }

        // Check right upper diagonal
        for (int r = row, c = col; r >= 0 && c < n; r--, c++) {
            if (board[r][c] == 'Q') {
                return false;
            }
        }

        return true;
    }

    private void helper(int row, char[][] board, List<List<String>> res, int n) {
        if (row == n) {
            res.add(construct(board));
            return;
        }

        for (int col = 0; col < n; col++) {
            if (isValid(row, col, board, n)) {
                board[row][col] = 'Q';
                helper(row + 1, board, res, n);
                board[row][col] = '.';
            }
        }
    }


    public List < List < String >> solveNQueens(int n) {
        char[][] board = new char[n][n];

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                board[i][j] = '.';

        List<List<String>> res = new ArrayList<List<String>> ();

        helper(0, board, res, n);
        return res;
    }
}

//Solution 2 - Traverse Column Wise

class Solution {

    static List<String> construct(char[][] board) {
        List<String> res = new LinkedList<>();
        for (int i = 0; i < board.length; i++) {
            // Create a new string for each row
            res.add(new String(board[i]));
        }
        return res;
    }

    private boolean isValid(int row, int col, char[][] board, int n) {
        // Check horizontal
        for (int c = 0; c < col; c++) {
            if (board[row][c] == 'Q') {
                return false;
            }
        }

        // Check left upper diagonal
        for (int r = row, c = col; r >= 0 && c >= 0; r--, c--) {
            if (board[r][c] == 'Q') {
                return false;
            }
        }

        // Check left lower diagonal
        for (int r = row, c = col; r <n && c >=0 ; r++, c--) {
            if (board[r][c] == 'Q') {
                return false;
            }
        }

        return true;
    }

    private void helper(int col, char[][] board, List<List<String>> res, int n) {
        if (col == n) {
            res.add(construct(board));
            return;
        }

        for (int row = 0; row < n; row++) {
            if (isValid(row, col, board, n)) {
                board[row][col] = 'Q';
                helper(col + 1, board, res, n);
                board[row][col] = '.';
            }
        }
    }


    public List < List < String >> solveNQueens(int n) {
        char[][] board = new char[n][n];

        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                board[i][j] = '.';

        List<List<String>> res = new ArrayList<List<String>> ();

        helper(0, board, res, n);
        return res;
    }
}