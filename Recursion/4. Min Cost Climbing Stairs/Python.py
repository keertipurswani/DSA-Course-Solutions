# https://leetcode.com/problems/min-cost-climbing-stairs
# (TLE solutions - not the most optimised solutions)

# Solution 1

class Solution:
    def helper(self, ind, cost):
        if ind <= 1:
            return cost[ind]
        if ind == len(cost):
            curr_cost = 0
        else:
            curr_cost = cost[ind]

        return curr_cost + min(self.helper(ind - 1, cost), self.helper(ind - 2, cost))


    def minCostClimbingStairs(self, cost):
        return self.helper(len(cost), cost)


# Solution 2

class Solution:
    def helper(self, ind, cost):
        if ind <= 1:
            return cost[ind]
        return cost[ind] + min(self.helper(ind - 1, cost), self.helper(ind - 2, cost))


    def minCostClimbingStairs(self, cost):
        return min(self.helper(len(cost)-1, cost), self.helper(len(cost)-2, cost))


# Solution 3 - From 0 to n

class Solution:
    def helper(self, ind, cost):
        if ind >= len(cost):
            return 0
        return cost[ind] + min(self.helper(ind + 1, cost), self.helper(ind + 2, cost))


    def minCostClimbingStairs(self, cost):
        return min(self.helper(0, cost), self.helper(1, cost))

