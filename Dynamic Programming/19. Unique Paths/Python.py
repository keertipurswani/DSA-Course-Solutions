# https://leetcode.com/problems/unique-paths

# Solution 1 - Bottom Up DP (2D table)
# Time Complexity:  O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


# Solution 2

# Solution 2 - Space Optimised DP (1D)
# Time Complexity:  O(m * n)
# Space Complexity: O(n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n     # first row is all 1s
        curr = [1] + [0] * (n - 1)

        for i in range(1, m):
            for j in range(1, n):
                curr[j] = prev[j] + curr[j - 1]
            prev = curr[:]   # copy

        return prev[n - 1]
