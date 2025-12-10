# https://leetcode.com/problems/palindrome-partitioning-ii

# Solution - TLE

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # dp[i][j] = minimum cuts needed for s[i..j]
        dp = [[0] * n for _ in range(n)]

        # l = length of substring
        for l in range(1, n + 1):
            for i in range(0, n - l + 1):
                j = i + l - 1

                if i == j:
                    dp[i][j] = 0

                elif j == i + 1:
                    dp[i][j] = 0 if s[i] == s[j] else 1

                else:
                    # if s[i..j] itself is a palindrome
                    if s[i] == s[j] and dp[i + 1][j - 1] == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = j - i  # worst case: cut between every character

                        for k in range(i, j):
                            dp[i][j] = min(
                                dp[i][j],
                                1 + dp[i][k] + dp[k + 1][j]
                            )

        return dp[0][n - 1]