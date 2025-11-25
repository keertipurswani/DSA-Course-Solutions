# https://leetcode.com/problems/house-robber
# (TLE solutions - not the most optimised solutions)

# Solution 1 - 0 to n

class Solution:
    def helper(self, ind, nums):
        if ind >= len(nums):
            return 0
        inc = nums[ind] + self.helper(ind+2, nums)
        exc = self.helper(ind+1, nums)
        return max(inc, exc)

    def rob(self, nums: List[int]) -> int:
        return self.helper(0, nums)

# Solution 2 - n to 0

class Solution:
    def helper(self, ind, nums):
        if ind < 0:
            return 0
        inc = nums[ind] + self.helper(ind-2, nums)
        exc = self.helper(ind-1, nums)
        return max(inc, exc)

    def rob(self, nums: List[int]) -> int:
        return self.helper(len(nums) - 1, nums)
