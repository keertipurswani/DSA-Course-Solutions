# https://leetcode.com/problems/sudoku-solver

# Actual problem: Place numbers(1 to 9) at 'E' places
# Sub-problem: Place numbers(1 to 9) at 1,2,....E-1,E places

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.placeNumberOnBoard(board)
    def placeNumberOnBoard(self,board: List[List[str]])->bool:
        for row in range(9):
            for col in range(9):
                if board[row][col]==".":
                    for c in range(1,10):
                        c=str(c)
                        if self.isValid(row,col,board,c):
                            board[row][col]=c
                            if self.placeNumberOnBoard(board):
                                return True
                            board[row][col]="."
                    return False
        return True
    
    def isValid(self,row:int,col:int,board: List[List[str]], c:str)->bool:
        for i in range(9):
            if board[row][i]==c:
                return False
            if board[i][col]==c:
                return False
            if board[3*(row//3)+i//3][3*(col//3)+i%3]==c:
                return False
        return True