# https://leetcode.com/problems/wildcard-matching

# Solution 1 - Recursion (TLE)
# Time Complexity:  O(2^(n+m))
# Space Complexity: O(n+m)

class Solution1:
    def helper(self, s, p, i, j):
        # both ended
        if i >= len(s) and j >= len(p):
            return True

        # pattern ended but string not
        if j >= len(p):
            return False

        # string ended but pattern may have '*' left
        if i >= len(s):
            if p[j] == '*':
                return self.helper(s, p, i, j + 1)
            return False

        # match or '?'
        if s[i] == p[j] or p[j] == '?':
            return self.helper(s, p, i + 1, j + 1)

        # '*'
        if p[j] == '*':
            return (self.helper(s, p, i, j + 1) or    # '*' = empty
                    self.helper(s, p, i + 1, j))      # '*' = consume 1 char

        return False

    def isMatch(self, s: str, p: str) -> bool:
        return self.helper(s, p, 0, 0)

# Solution 3 - Recursion n→0 (TLE)
# Time Complexity:  O(2^(n+m))
# Space Complexity: O(n+m)

class Solution3:
    def helper(self, s, p, i, j):
        if i < 0 and j < 0:
            return True

        if j < 0:
            return False

        if i < 0:
            if p[j] == '*':
                return self.helper(s, p, i, j - 1)
            return False

        if s[i] == p[j] or p[j] == '?':
            return self.helper(s, p, i - 1, j - 1)

        if p[j] == '*':
            return (self.helper(s, p, i, j - 1) or
                    self.helper(s, p, i - 1, j))

        return False

    def isMatch(self, s: str, p: str) -> bool:
        return self.helper(s, p, len(s) - 1, len(p) - 1)


# Solution 3 - Recursion n→0 (TLE)
# Time Complexity:  O(2^(n+m))
# Space Complexity: O(n+m)

class Solution3:
    def helper(self, s, p, i, j):
        if i < 0 and j < 0:
            return True

        if j < 0:
            return False

        if i < 0:
            if p[j] == '*':
                return self.helper(s, p, i, j - 1)
            return False

        if s[i] == p[j] or p[j] == '?':
            return self.helper(s, p, i - 1, j - 1)

        if p[j] == '*':
            return (self.helper(s, p, i, j - 1) or
                    self.helper(s, p, i - 1, j))

        return False

    def isMatch(self, s: str, p: str) -> bool:
        return self.helper(s, p, len(s) - 1, len(p) - 1)

# Solution 4 - Memoization n→0
# Time Complexity:  O(n*m)
# Space Complexity: O(n*m) + O(n+m)

class Solution4:
    def helper(self, s, p, i, j, dp):
        if i < 0 and j < 0:
            return True
        if j < 0:
            return False
        if i < 0:
            if p[j] == '*':
                return self.helper(s, p, i, j - 1, dp)
            return False

        if dp[i][j] != -1:
            return dp[i][j]

        if s[i] == p[j] or p[j] == '?':
            dp[i][j] = self.helper(s, p, i - 1, j - 1, dp)
            return dp[i][j]

        if p[j] == '*':
            dp[i][j] = (self.helper(s, p, i, j - 1, dp) or
                        self.helper(s, p, i - 1, j, dp))
            return dp[i][j]

        dp[i][j] = False
        return False

    def isMatch(self, s: str, p: str) -> bool:
        dp = [[-1] * len(p) for _ in range(len(s))]
        return self.helper(s, p, len(s) - 1, len(p) - 1, dp)

# Solution 5 - Bottom Up DP
# Time Complexity:  O(n*m)
# Space Complexity: O(n*m)

class Solution5:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        # pattern prefix can match empty if all '*'
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = False

        return dp[n][m]

# Solution 6 - Space Optimised
# Time Complexity:  O(n*m)
# Space Complexity: O(m)

class Solution6:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)

        prev = [False] * (m + 1)
        curr = [False] * (m + 1)

        prev[0] = True

        # handle leading '*' in pattern
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 1]

        for i in range(1, n + 1):
            curr = [False] * (m + 1)
            for j in range(1, m + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    curr[j] = prev[j - 1]
                elif p[j - 1] == '*':
                    curr[j] = prev[j] or curr[j - 1]
                else:
                    curr[j] = False

            prev = curr

        return prev[m]
