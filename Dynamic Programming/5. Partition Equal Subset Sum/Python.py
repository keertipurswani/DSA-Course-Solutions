# https://leetcode.com/problems/partition-equal-subset-sum

# Solution 1 - Recursion (TLE)
# Time Complexity:  O(2^n)
# Space Complexity: O(n)

class Solution1:
    def helper(self, ind, target, nums):
        if ind >= len(nums):
            return target == 0

        # exclude
        if self.helper(ind + 1, target, nums):
            return True

        # include
        if nums[ind] <= target:
            if self.helper(ind + 1, target - nums[ind], nums):
                return True

        return False

    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 == 1:
            return False
        return self.helper(0, total // 2, nums)


# Solution 2 - Memoization
# Time Complexity:  O(n * target)
# Space Complexity: O(n * target) + O(n)

class Solution2:
    def helper(self, ind, target, nums, dp):
        if ind >= len(nums):
            return target == 0

        if dp[ind][target] != -1:
            return dp[ind][target]

        # exclude
        if self.helper(ind + 1, target, nums, dp):
            dp[ind][target] = True
            return True

        # include
        if nums[ind] <= target:
            if self.helper(ind + 1, target - nums[ind], nums, dp):
                dp[ind][target] = True
                return True

        dp[ind][target] = False
        return False

    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        n = len(nums)

        dp = [[-1] * (target + 1) for _ in range(n)]
        return self.helper(0, target, nums, dp)


# Solution 3 - Bottom Up DP
# Time Complexity:  O(n * target)
# Space Complexity: O(n * target)

class Solution3:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 == 1:
            return False

        n = len(nums)
        target = total // 2

        # dp[i][j] = can sum j be made using first i nums?
        dp = [[False] * (target + 1) for _ in range(n + 1)]

        # sum 0 is always possible
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                # include nums[i-1]
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]]
                # exclude nums[i-1]
                dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[n][target]


# Solution 4 - Space Optimized Bottom Up DP
# Time Complexity:  O(n * target)
# Space Complexity: O(target)

class Solution4:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 == 1:
            return False

        n = len(nums)
        target = total // 2

        prev = [False] * (target + 1)
        curr = [False] * (target + 1)

        prev[0] = True
        curr[0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                # include
                if nums[i - 1] <= j:
                    curr[j] = prev[j - nums[i - 1]]
                # exclude
                curr[j] = curr[j] or prev[j]

            prev = curr[:]   # copy

        return prev[target]
