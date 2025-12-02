# https://leetcode.com/problems/fibonacci-number

# Solution 1 - Recursion - TLE
# Time Complexity - O(2^n)
# Space Complexity - O(n) (Recursive Stack Space)

class Solution(object):
    def fib(self, n):
        if n<=1:
            return n
        return self.fib(n-1) + self.fib(n-2)


# Solution 2 - Memoization - Top Down
# Time Complexity - O(n)
# Space Complexity - O(n) (n for recursive stack and n for dp array - O(n) + O(n))

class Solution:
    def helper(self, i, dp):
        if dp[i] != -1:
            return dp[i]
        
        if i<=1:
            dp[i] = i
            return dp[i]

        dp[i] = self.helper(i-1, dp) + self.helper(i-2, dp)
        return dp[i]

    def fib(self, n: int) -> int:
        dp = [-1] * (n+1)
        self.helper(n, dp)
        return dp[n]
    


#Solution 3 - Bottom Up DP - Tabulation
#Time Complexity - O(n)
#Space Complexity - O(n) (n for dp array - no recursive stack space)

class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n

        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

#Solution 4 - Space optimized bottom up DP
#Time Complexity - O(n)
#Space Complexity - O(1)

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        seclast = 0
        last = 1

        for i in range(2, n+1):
            ans = seclast + last
            seclast = last
            last = ans

        return ans