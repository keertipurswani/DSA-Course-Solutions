# https://leetcode.com/problems/number-of-islands

class Solution:
    def isSafe(self, i, j, n, m):
        return 0 <= i < n and 0 <= j < m

    def dfs(self, grid, vis, i, j, n, m):
        vis[i][j] = True
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if self.isSafe(ni, nj, n, m) and grid[ni][nj] == '1' and not vis[ni][nj]:
                self.dfs(grid, vis, ni, nj, n, m)

    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])

        vis = [[False] * m for _ in range(n)]
        res = 0

        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j] == '1':
                    self.dfs(grid, vis, i, j, n, m)
                    res += 1

        return res
