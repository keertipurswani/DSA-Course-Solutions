# https://leetcode.com/problems/palindromic-substrings

# Time Complexity:  O(n^3)
# Space Complexity: O(n)

class Solution:
    def isPalindrome(self, s, i, j):
        # check if s[i..j] is palindrome using recursion
        if i >= j:          # 0 or 1 char
            return True
        if s[i] != s[j]:
            return False
        return self.isPalindrome(s, i + 1, j - 1)

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            for j in range(i, n):
                if self.isPalindrome(s, i, j):
                    res += 1

        return res

# Recursion with Memoization
# Time Complexity:  O(n^2)
# Space Complexity: O(n^2)

class Solution1:
    def helper(self, i, j, s, dp):
        if j < i:
            return False
        
        if i == j:
            dp[i][j] = True
            return True
        
        if dp[i][j] != -1:
            return dp[i][j]

        # move boundaries to fill dp table
        self.helper(i + 1, j, s, dp)
        self.helper(i, j - 1, s, dp)

        if s[i] == s[j] and (j == i + 1 or self.helper(i + 1, j - 1, s, dp)):
            dp[i][j] = True
        else:
            dp[i][j] = False

        return dp[i][j]

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        
        self.helper(0, n - 1, s, dp)

        res = 0
        for row in dp:
            for val in row:
                if val == True:
                    res += 1
        return res

# Recursion with Memoization (count during recursion)
# Time Complexity:  O(n^2)
# Space Complexity: O(n^2)

class Solution2:
    def helper(self, i, j, s, dp):
        if j < i:
            return False

        if i == j:
            if dp[i][j] == -1:
                self.res += 1
            dp[i][j] = True
            return True

        if dp[i][j] != -1:
            return dp[i][j]

        # expand search range
        self.helper(i + 1, j, s, dp)
        self.helper(i, j - 1, s, dp)

        if s[i] == s[j] and (j == i + 1 or self.helper(i + 1, j - 1, s, dp)):
            dp[i][j] = True
            self.res += 1
        else:
            dp[i][j] = False

        return dp[i][j]

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        self.res = 0
        self.helper(0, n - 1, s, dp)
        return self.res
    
# Bottom Up DP
# Time Complexity:  O(n^2)
# Space Complexity: O(n^2)

class Solution3:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [[False] * n for _ in range(n)]

        # l = length of substring
        for l in range(1, n + 1):
            for i in range(0, n - l + 1):
                j = i + l - 1

                if i == j:  # single character
                    dp[i][j] = True
                elif j == i + 1:  # two characters
                    dp[i][j] = (s[i] == s[j])
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j]:
                    res += 1

        return res

