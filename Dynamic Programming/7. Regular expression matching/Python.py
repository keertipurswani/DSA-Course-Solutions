# https://leetcode.com/problems/regular-expression-matching

# Solution 1 - Recursion (TLE)
# Time Complexity:  Exponential
# Space Complexity: O(n + m)

class Solution:
    def helper(self, s, p, i, j):
        # both strings finished
        if i < 0 and j < 0:
            return True

        # pattern finished, string not → no match
        if j < 0:
            return False

        # string finished, pattern not
        if i < 0:
            # only possible if pattern has '*' patterns left
            if p[j] == '*':
                return self.helper(s, p, i, j - 2)
            return False

        # normal char match OR '.'
        if s[i] == p[j] or p[j] == '.':
            return self.helper(s, p, i - 1, j - 1)

        # '*' handling
        if p[j] == '*':
            # case 1: '*' = zero occurrences
            if self.helper(s, p, i, j - 2):
                return True
            # case 2: '*' consumes one char in s
            if j > 0 and (s[i] == p[j - 1] or p[j - 1] == '.'):
                return self.helper(s, p, i - 1, j)

        return False

    def isMatch(self, s: str, p: str) -> bool:
        return self.helper(s, p, len(s) - 1, len(p) - 1)


# Solution 2 - Memoization
# Time Complexity:  O(n * m)
# Space Complexity: O(n * m) + O(n + m)

class Solution:
    def helper(self, s, p, i, j, dp):
        if i < 0 and j < 0:
            return True
        if j < 0:
            return False
        if i < 0:
            if p[j] == '*':
                return self.helper(s, p, i, j - 2, dp)
            return False

        if dp[i][j] != -1:
            return dp[i][j]

        # match or '.'
        if s[i] == p[j] or p[j] == '.':
            dp[i][j] = self.helper(s, p, i - 1, j - 1, dp)
            return dp[i][j]

        # '*'
        if p[j] == '*':
            # zero occurrences
            if self.helper(s, p, i, j - 2, dp):
                dp[i][j] = True
                return True

            # one or more occurrences
            if j > 0 and (s[i] == p[j - 1] or p[j - 1] == '.'):
                if self.helper(s, p, i - 1, j, dp):
                    dp[i][j] = True
                    return True

        dp[i][j] = False
        return False

    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[-1] * m for _ in range(n)]
        return self.helper(s, p, n - 1, m - 1, dp)


# Solution 3 - Bottom Up DP
# Time Complexity:  O(n * m)
# Space Complexity: O(n * m)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        # pattern vs empty string
        for j in range(1, m + 1):
            dp[0][j] = (j > 1 and p[j - 1] == '*') and dp[0][j - 2]

        # fill dp
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # character match
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]

                # handling '*'
                elif p[j - 1] == '*' and j > 1:
                    # zero occurrences
                    dp[i][j] = dp[i][j - 2]

                    # one/more occurrences
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

                else:
                    dp[i][j] = False

        return dp[n][m]
