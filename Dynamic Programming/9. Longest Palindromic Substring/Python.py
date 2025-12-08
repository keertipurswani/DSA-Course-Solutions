# https://leetcode.com/problems/longest-palindromic-substring

# Solution 1 - Recursion (TLE)
# Time Complexity:  Exponential
# Space Complexity: Linear

class Solution:
    def helper(self, i, j, s):
        isPal = False
        if i == j:
            isPal = True
        elif s[i] == s[j] and (j == i + 1 or self.helper(i + 1, j - 1, s)):
            isPal = True

        if isPal:
            # update result if longer palindrome found
            if j - i + 1 > len(self.res):
                self.res = s[i:j + 1]
        else:
            # try shrinking from both ends
            self.helper(i + 1, j, s)
            self.helper(i, j - 1, s)

        return isPal

    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        self.helper(0, len(s) - 1, s)
        return self.res
    
# Solution 2 - Bottom Up DP
# Time Complexity:  O(n^2)
# Space Complexity: O(n^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        res = s[0]  # at least 1 character is always a palindrome

        # l = length of substring
        for l in range(1, n + 1):
            for i in range(0, n - l + 1):
                j = i + l - 1

                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j] and (j == i + 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res = s[i:j + 1]

        return res

