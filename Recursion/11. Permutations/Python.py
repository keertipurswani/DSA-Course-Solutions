# https://leetcode.com/problems/permutations

# Time Complexity - O(n × n!)
# Space Complexity - O(n) + O(n × n!)

# Solution 1 - Extra curr

class Solution:
    def helper(self, nums, curr, used, res):
        if len(curr) == len(nums):
            res.append(curr[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            used[i] = True
            curr.append(nums[i])

            self.helper(nums, curr, used, res)

            curr.pop()
            used[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        self.helper(nums, [], used, res)
        return res


# Solution 2 -> 0 to n

class Solution:
    def helper(self, res, nums, ind, n):
        if ind == n:
            res.append(nums[:])   # append a copy
            return

        for i in range(ind, n):
            nums[i], nums[ind] = nums[ind], nums[i]   # swap
            self.helper(res, nums, ind + 1, n)
            nums[i], nums[ind] = nums[ind], nums[i]   # swap back (backtrack)

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(res, nums, 0, len(nums))
        return res
    
# Solution 3 -> n-1 to 0

class Solution:

    def helper(self, nums, ind, res):
        if ind == 0:
            res.append(nums[:])
            return

        for i in range(0, ind+1):
            nums[i], nums[ind] = nums[ind], nums[i]   # swap
            self.helper(nums, ind-1, res)
            nums[i], nums[ind] = nums[ind], nums[i]   # swap back (backtrack)


    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, len(nums) - 1, res)
        return res