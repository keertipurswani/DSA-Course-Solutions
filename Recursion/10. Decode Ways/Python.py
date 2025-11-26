# https://leetcode.com/problems/decode-ways

# Solution 1 - n to 0

class Solution:
    def helper(self, s, ind, n):
        if ind <= 0:
            return 1
        count = 0
        # Single Digit
        if s[ind] != '0':
            count = self.helper(s, ind-1, n)

        # Double digit => ind-1 and ind 
        if (s[ind-1] == '1' or (s[ind-1] == '2' and '0' <= s[ind] <= '6')):
            count += self.helper(s, ind-2, n)

        return count

    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        return self.helper(s, n-1, n)

# Solution 2 - 0 to n

class Solution:
    def helper(self, s, ind, n):
        if ind == n:
            return 1

        if s[ind] == '0':
            return 0

        res = 0

        # Case 1: Single digit decode
        res = self.helper(s, ind + 1, n)

        # Case 2: Two-digit decode
        if ((ind < n-1) and ((s[ind] == '1') or (s[ind] == '2' and '0' <= s[ind+1] <= '6'))):
            res += self.helper(s, ind + 2, n)

        return res

    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        return self.helper(s, 0, n)

