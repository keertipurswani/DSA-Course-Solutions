#  https://leetcode.com/problems/n-th-tribonacci-number
#  (TLE solutions - not the most optimised solutions)

# Actual problem: find tribonacci of nth number
# Sub-problem: if we can find the tribonacci of f(n-1), f(n-2) and f(n-3) then we can find the tribonacci of f(n).
# Recurrence relation: f(n)=f(n-1)+f(n-2)+f(n-3)

class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n<=2:
            return 1
        return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)