# https://leetcode.com/problems/fibonacci-number
# not the most optimised solutions

# Actual problem: find fibonacci of the nth number
# Sub-problem: find fibonacci of (n-1) and (n-2)
# Recurrence relation: f(n)=f(n-1)+f(n-2)

class Solution:
    def fib(self, n: int) -> int:
        if n<=1:  # base case
            return n
        return self.fib(n-1)+self.fib(n-2)   