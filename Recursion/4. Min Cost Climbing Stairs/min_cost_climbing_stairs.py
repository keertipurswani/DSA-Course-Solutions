# https://leetcode.com/problems/min-cost-climbing-stairs
# (TLE solutions - not the most optimised solutions)

# Bottom up approach
# Actual problem: Find min cost to reach top of stairs
# Sub problem: find min cost to reach n+1 or n+2 steps
# Recurrence relation: f(n)=min(cost[n]+f(n+1),cost[n+1]+f(n+2))
# Time Complexity: O(2^n)
# Space Complexity: O(n)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.costToClimbStairs(0,cost),self.costToClimbStairs(1,cost))  # since we can start from either step 0 or step 1
    def costToClimbStairs(self,currentStep: int,cost: List[int])-> int:
        if currentStep>= len(cost):  # base condition
            return 0
        return cost[currentStep]+min(self.costToClimbStairs(currentStep+1,cost),self.costToClimbStairs(currentStep+2,cost))




# Top down approach
# Recurrence relation: f(n)=min(cost[n]+f(n-1),cost[n-1]+f(n-2))
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.costToClimbStairs(len(cost)-1,cost),self.costToClimbStairs(len(cost)-2,cost)) 
    def costToClimbStairs(self,currentStep: int,cost: List[int])-> int:
        if currentStep<=1:  # base condition
            return cost[currentStep]
        return cost[currentStep]+min(self.costToClimbStairs(currentStep-1,cost),self.costToClimbStairs(currentStep-2,cost))