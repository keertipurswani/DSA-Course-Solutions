# https://leetcode.com/problems/house-robber
# (TLE solutions - not the most optimised solutions)

# Actual problem: rob houses, but don't rob adjacent houses
# Sub-problem: If we rob nth house then we either rob n+2 house. If we don't rob nth then we rob n+1 or n+3
# Top-down approach(n to 0)
# Reccurence relation: f(n)=max(num[n]+n-2,n-1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.robHouse(nums,len(nums)-1)
    def robHouse(self,nums:List[int],index: int)->int:
        if index<0:  # base condition
            return 0
        include= nums[index]+self.robHouse(nums,index-2)
        exclude=self.robHouse(nums,index-1)
        return max(include,exclude)

# Bottom-up approach(0 to n)
# Recurrence relation: f(n)=max(num[n])+n+2,n+1)

class Solution:
    def rob(self,nums:List[int])-> int:
        return self.robHouse(nums,0,len(nums))
    def robHouse(self, nums: List[int],index: int,n: int)-> int:
        if index>=n:  # base condition
            return 0
        include=nums[index]+self.robHouse(nums,index+2,n)
        exclude=self.robHouse(nums,index+1,n)
        return max(include,exclude)