# https://leetcode.com/problems/n-queens

class Solution:
    def isValid(self, row: int, col: int, board: List[List[str]], n: int) -> bool:
        # check left horizontal
        for c in range(col):
            if board[row][c] == 'Q':
                return False

        # check left upper diagonal
        r, c = row, col
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # check left lower diagonal
        r, c = row, col
        while r < n and c >= 0:
            if board[r][c] == 'Q':
                return False
            r += 1
            c -= 1

        return True

    def helper(self, col: int, board: List[List[str]], res: List[List[str]], n: int) -> None:
        if col == n:
            # convert each row (list of chars) back to string
            res.append(["".join(row) for row in board])
            return

        for row in range(n):
            if self.isValid(row, col, board, n):
                board[row][col] = 'Q'
                self.helper(col + 1, board, res, n)
                board[row][col] = '.'   # backtrack

    def solveNQueens(self, n: int) -> List[List[str]]:
        res: List[List[str]] = []
        # board as list of lists so we can do board[row][col] = 'Q'
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.helper(0, board, res, n)
        return res
