# https://leetcode.com/problems/coin-change/description/

# Solution 1 - Recursion TLE 

class Solution:
    def helper(self, coins, amount, ind):
        if amount == 0:
            return 0
        if amount < 0 or ind >= len(coins):
            return math.inf

        # exclude coin
        res = self.helper(coins, amount, ind + 1)

        # include coin
        if coins[ind] <= amount:
            res = min(res, 1 + self.helper(coins, amount - coins[ind], ind))

        return res

    def coinChange(self, coins: List[int], amount: int) -> int:
        res = self.helper(coins, amount, 0)
        return -1 if res >= math.inf else res


# Solution 2 - Memoization 

class Solution:
    def helper(self, coins, amount, ind, dp):
        if amount == 0:
            return 0
        if amount < 0 or ind >= len(coins):
            return math.inf

        if dp[ind][amount] != -1:
            return dp[ind][amount]

        # exclude coin
        res = self.helper(coins, amount, ind + 1, dp)

        # include coin
        if coins[ind] <= amount:
            res = min(res, 1 + self.helper(coins, amount - coins[ind], ind, dp))

        dp[ind][amount] = res
        return res

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        res = self.helper(coins, amount, 0, dp)
        return -1 if res >= math.inf else res


# Solution 3 - Bottom Up DP

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        # dp[i][j] = min coins to make sum j using first i coins
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # first row: 0 coins → impossible for all positive j
        for j in range(1, amount + 1):
            dp[0][j] = math.inf

        # build table
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j],            # exclude
                        1 + dp[i][j - coins[i-1]]  # include
                    )

        return -1 if dp[n][amount] >= math.inf else dp[n][amount]




