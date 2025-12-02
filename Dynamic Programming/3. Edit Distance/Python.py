# https://leetcode.com/problems/edit-distance

# Solution 1 - Recursion (TLE)
# Time Complexity:  O(3^(n+m))  - exponential
# Space Complexity: O(n + m)    - due to recursion depth

class Solution:

    def helper(self, word1, word2, i, j):
        if i >= len(word1):
            return len(word2) - j

        if j >= len(word2):
            return len(word1) - i

        if word1[i] == word2[j]:
            return self.helper(word1, word2, i+1, j+1)

        return 1 + min(
            self.helper(word1, word2, i, j + 1),
            self.helper(word1, word2, i + 1, j),
            self.helper(word1, word2, i + 1, j + 1)
        )

    def minDistance(self, word1: str, word2: str) -> int:
        return self.helper(word1, word2, 0, 0)
    
    
# Solution 2 - Memoization
# Time Complexity:  O(n * m)
# Space Complexity: O(n + m) + O(n * m)

class Solution:

    def helper(self, word1, word2, i, j, dp):
        if i >= len(word1):
            return len(word2) - j

        if j >= len(word2):
            return len(word1) - i

        if dp[i][j] != -1:
            return dp[i][j]

        if word1[i] == word2[j]:
            dp[i][j] = self.helper(word1, word2, i+1, j+1, dp)
            return dp[i][j]

        dp[i][j] = 1 + min(
            self.helper(word1, word2, i, j + 1, dp),
            self.helper(word1, word2, i + 1, j, dp),
            self.helper(word1, word2, i + 1, j + 1, dp)
        )
        return dp[i][j]

    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[-1] * m for _ in range(n)] # n*m list
        return self.helper(word1, word2, 0, 0, dp)
    

# Solution 3 - Bottom-Up DP
# Time Complexity:  O(n * m)
# Space Complexity: O(n * m)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        dp = [[0] * (m+1) for _ in range(n+1)] # (n+1) × (m+1)

        for i in range(1, n+1):
            dp[i][0] = i
        for j in range(1, m+1):
            dp[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                
        return dp[n][m]
    

# Solution 4 - Space Optimised Bottom-Up DP
# Time Complexity:  O(n * m)
# Space Complexity: O(m)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        prev = [0] * (m+1)

        for j in range(1, m+1):
            prev[j] = j

        for i in range(1, n+1):

            curr = [0] * (m+1)
            curr[0] = i

            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(prev[j], prev[j-1], curr[j-1])

            prev = curr
                
        return prev[m]
