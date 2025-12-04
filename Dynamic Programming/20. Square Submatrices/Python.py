# https://leetcode.com/problems/count-square-submatrices-with-all-ones

# Solution 1 - DP table + counting
# Time Complexity:  O(n * m)
# Space Complexity: O(n * m)

class Solution:
    def countSquares(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * m for _ in range(n)]
        res = 0

        # first column
        for i in range(n):
            dp[i][0] = matrix[i][0]
            if dp[i][0] == 1:
                res += 1

        # first row
        for j in range(m):
            dp[0][j] = matrix[0][j]
            if dp[0][j] == 1 and j != 0:
                res += 1

        # fill the dp table
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j - 1],
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )

                    # dp[i][j] is the size of the biggest square ending at (i, j)
                    res += dp[i][j]     # this automatically adds dp[i][j] squares
                else:
                    dp[i][j] = 0

        return res
    

# Solution 2 - In-place DP (Optimized)
# Time Complexity:  O(n * m)
# Space Complexity: O(1)

class Solution2:
    def countSquares(self, matrix):
        res = 0
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if i > 0 and j > 0 and matrix[i][j] == 1:
                    matrix[i][j] = 1 + min(
                        matrix[i - 1][j],
                        matrix[i][j - 1],
                        matrix[i - 1][j - 1]
                    )
                
                # every cell contributes matrix[i][j] squares
                res += matrix[i][j]

        return res

