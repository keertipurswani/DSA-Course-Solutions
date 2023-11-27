# https://leetcode.com/problems/n-queens

# Actual problem: can we place queens at n rows/cols
# sub-problem: can we place a queen at n-1 row/col

# Column traversal approach

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result,board=[],[["."]*n for i in range(n)]    
        self.placeQueen(0,n,board,result)
        return result

    def placeQueen(self,col: int,n:int,board: List[str], result:List[List[str]]):
        if col==n:
            copy=["".join(row) for row in board]
            result.append(copy)
            return
        for row in range(0,n):
            if self.isValid(row,col,n,board):
                board[row][col]='Q'                
                self.placeQueen(col+1,n,board,result)
                board[row][col]='.'

    def isValid(self,row:int,col:int,n:int,board:List[str])->bool:
        for c in range(0,col):
            if board[row][c]=='Q':
                return False
        r,c=row,col
        while r>=0 and c>=0:
            if board[r][c]=='Q':
                return False
            r-=1
            c-=1
        r,c=row,col
        while r<n and c>=0:
            if board[r][c]=='Q':
                return False
            r+=1
            c-=1        
        return True

# Row traversal
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
            result,board=[],[["."]*n for i in range(n)]    
            self.placeQueen(0,n,board,result)
            return result

    def placeQueen(self,row: int,n:int,board: List[str], result:List[List[str]]):
            if row==n:
                copy=["".join(col) for col in board]
                result.append(copy)
                return
            for col in range(0,n):
                if self.isValid(row,col,n,board):
                    board[row][col]='Q'                
                    self.placeQueen(row+1,n,board,result)
                    board[row][col]='.'

    def isValid(self,row:int,col:int,n:int,board:List[str])->bool:
            for r in range(0,row):
                if board[r][col]=='Q':
                    return False
            r,c=row,col
            while r>=0 and c>=0:
                if board[r][c]=='Q':
                    return False
                r-=1
                c-=1
            r,c=row,col
            while r>=0 and c<n:
                if board[r][c]=='Q':
                    return False
                r-=1
                c+=1        
            return True