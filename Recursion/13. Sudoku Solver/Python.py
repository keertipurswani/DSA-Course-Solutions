# https://leetcode.com/problems/sudoku-solver

# Time Complexity - 9 power n square
#                 - 9 power no of empty spaces
# Space Complexity - O(no of empty spaces)

class Solution:
    def isValid(self, row: int, col: int, board: List[List[str]], ch: str) -> bool:
        for i in range(9):
            # check row
            if board[row][i] == ch:
                return False
            # check col
            if board[i][col] == ch:
                return False
            # check 3x3 box
            if board[3 * (row // 3) + (i // 3)][3 * (col // 3) + (i % 3)] == ch:
                return False
        return True

    def helper(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for ch in map(str, range(1, 10)):  # '1' to '9'
                        if self.isValid(i, j, board, ch):
                            board[i][j] = ch
                            if self.helper(board):
                                return True
                            board[i][j] = '.'
                    return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.helper(board)
