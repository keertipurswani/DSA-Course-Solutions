# https://leetcode.com/problems/word-break


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)   

        # dp[i][j] = True if s[i..j] can be segmented using wordDict
        dp = [[False] * n for _ in range(n)]

        # l = length of substring
        for l in range(1, n + 1):
            for i in range(0, n - l + 1):
                j = i + l - 1

                # direct dictionary match
                if s[i:j+1] in wordSet:
                    dp[i][j] = True
                else:
                    # try all possible partitions
                    for k in range(i, j):
                        dp[i][j] = dp[i][j] or (dp[i][k] and dp[k + 1][j])

        return dp[0][n - 1]
