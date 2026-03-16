# https://leetcode.com/problems/fibonacci-number/description/

# recursion solution
# Time complexity: O(2^n)
# Space Complexity: O(n)

class Solution:
    def fib(self, n: int) -> int:
        if n<=1:  # base case
            return n
    return self.fib(n-1)+self.fib(n-2)

# Top down approach using memoization
# Time complexity: O(n), as we calculate fibonacci of a number only once
# Space cpmplexity: O(n), we'll use an array to store answer of overlapping sub-problems
#  and stack space of recursive call

class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        dp=[]
        return dp[n]
    
    def findFib(self,n:int,dp:List[int])->int:
        if n<=1:  #base case
            return n
        if dp[n]!=-1:
            return dp[n]
        dp[n]= self.findFib(n-1,dp)+self.findFib(n-2,dp)
        return dp[n]