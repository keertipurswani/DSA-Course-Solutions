# https://leetcode.com/problems/01-mat

# Solution 1 - BFS
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        q = deque()

        # initialize queue with all 0s, set others to large value
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = n + m   # large number

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            i, j = q.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    if mat[ni][nj] > mat[i][j] + 1:
                        mat[ni][nj] = mat[i][j] + 1
                        q.append((ni, nj))

        return mat
    
# Solution 2 - DP

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        INF = n + m

        # initialize non-zero cells
        for i in range(n):
            for j in range(m):
                if mat[i][j] != 0:
                    mat[i][j] = INF

        # top-left to bottom-right
        for i in range(n):
            for j in range(m):
                if mat[i][j] != 0:
                    if i > 0:
                        mat[i][j] = min(mat[i][j], mat[i-1][j] + 1)
                    if j > 0:
                        mat[i][j] = min(mat[i][j], mat[i][j-1] + 1)

        # bottom-right to top-left
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if mat[i][j] != 0:
                    if i < n - 1:
                        mat[i][j] = min(mat[i][j], mat[i+1][j] + 1)
                    if j < m - 1:
                        mat[i][j] = min(mat[i][j], mat[i][j+1] + 1)

        return mat
    

