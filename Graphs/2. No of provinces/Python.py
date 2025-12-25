# https://leetcode.com/problems/number-of-provinces

class Solution:
    def dfs(self, isConnected, n, curr, vis):
        for i in range(n):
            if isConnected[curr][i] == 1 and not vis[i]:
                vis[i] = True
                self.dfs(isConnected, n, i, vis)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [False] * n
        cnt = 0

        for i in range(n):
            if not vis[i]:
                cnt += 1
                vis[i] = True
                self.dfs(isConnected, n, i, vis)

        return cnt