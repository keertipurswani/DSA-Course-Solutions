# https://leetcode.com/problems/subsets

# C++

# Solution 1 

class Solution:
    def helper(self, nums, ind, curr, res):
        if ind == len(nums):
            res.append(curr[:])
            return

        #exc
        self.helper(nums, ind+1, curr, res)

        #inc
        curr.append(nums[ind])
        self.helper(nums, ind+1, curr, res)
        curr.pop() # lists in Python are mutable and are passed by reference

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, 0, [], res)
        return res

# Solution 2

class Solution:
    def helper(self, nums, ind, curr, res):
        if ind == -1:
            res.append(curr[:])
            return

        #exc
        self.helper(nums, ind-1, curr, res)

        #inc
        curr.append(nums[ind])
        self.helper(nums, ind-1, curr, res)
        curr.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, len(nums)-1, [], res)
        return res