# https://leetcode.com/problems/longest-palindromic-subsequence

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        # dp[i][j] = LPS length in s[i..j]
        dp = [[0] * n for _ in range(n)]

        # l = length of substring
        for l in range(1, n + 1):
            for i in range(0, n - l + 1):
                j = i + l - 1

                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


# Solution 2 - LCS of String, Reverse(String)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        n = len(s)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][n]
