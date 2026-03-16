# https://leetcode.com/problems/climbing-stairs
# (TLE solutions - not the most optimised solutions)

# Actual problem: find distinct ways to reach top floor(n)
# Sub-problem: since we can take 1 or 2 steps each time: if we can find distinct ways to reach n-1 and n-2 steps
#  then we can find distinct ways to reach nth step
# Recurrence relation: f(n)=f(n-1)+f(n-2)
# Time Complexity: O(2^n)
# Space complexity: O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 0
        return self.climbStairs(n-1)+self.climbStairs(n-2)

