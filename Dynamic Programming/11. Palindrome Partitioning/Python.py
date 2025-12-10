# https://leetcode.com/problems/palindrome-partitioning

# O(2^n) *n => n for inserting into another structure + O(n^2) for gap method

class Solution:
    def helper(self, res, curr, ind, s, dp):
        # if we have reached the end of the string, add current partition
        if ind >= len(s):
            res.append(curr[:])   # append a copy
            return

        # try all possible partitions starting at ind
        for i in range(ind, len(s)):
            if dp[ind][i]:  # s[ind:i+1] is a palindrome
                curr.append(s[ind:i+1])
                self.helper(res, curr, i + 1, s, dp)
                curr.pop()  # backtrack

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        if n == 0:
            return res

        # dp[i][j] = True if s[i..j] is a palindrome
        dp = [[False] * n for _ in range(n)]

        # fill dp using gap/length method
        for l in range(1, n + 1):          # l = length of substring
            for i in range(0, n - l + 1):
                j = i + l - 1
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j] and (j == i + 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True

        self.helper(res, [], 0, s, dp)
        return res