# https://leetcode.com/problems/house-robber/description/

# Top-down DP(memoization)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        return self.robHouse(n-1,nums,dp)
    def robHouse(self,index,nums:List[int],dp:List[int])->int:
        if index<0:
            return 0
        if dp[index]!=-1:
            return dp[index]
        include=nums[index]+self.robHouse(index-2,nums,dp)
        exclude=self.robHouse(index-1,nums,dp)
        dp[index]=max(include,exclude)
        return dp[index]

# Bottom-up DP(tabulation)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3:
            return max(nums)
        dp=[-1]*n
        dp[0]=nums[0]
        for index in range(1,n):
            include=nums[index]
            if index>1:
                include+=dp[index-2]
            exclude=dp[index-1]
            dp[index]=max(include,exclude)
        return dp[n-1]

# Space optimization
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3:
            return max(nums)
        prev_robbed,prev_robbed_exc=nums[0],0

        for index in range(1,n):
            include=nums[index]
            if index>1:
                include+=prev_robbed_exc
            exclude=prev_robbed
            curr_robbed=max(include,exclude)
            prev_robbed_exc=prev_robbed
            prev_robbed=curr_robbed
        return prev_robbed