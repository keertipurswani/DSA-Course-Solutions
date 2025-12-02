# https://leetcode.com/problems/longest-common-subsequence

# Solution 1 - Recursion (indices from n-1, m-1 to 0)
# Time Complexity:  O(2^(n+m))  - exponential
# Space Complexity: O(n + m)    - recursion stack depth

class Solution1:
    def helper(self, text1: str, text2: str, i: int, j: int) -> int:
        # Base case: if either index goes out of bounds (before start of string)
        if i < 0 or j < 0:
            return 0

        # If characters match, take 1 + LCS of remaining prefixes
        if text1[i] == text2[j]:
            return 1 + self.helper(text1, text2, i - 1, j - 1)

        # Else, either skip char from text1 or from text2
        return max(
            self.helper(text1, text2, i - 1, j),
            self.helper(text1, text2, i, j - 1),
        )

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.helper(text1, text2, len(text1) - 1, len(text2) - 1)
    

# Solution 2 - Memoization (indices from n-1, m-1 to 0)
# Time Complexity:  O(n * m)      - number of unique (i, j) states
# Space Complexity: O(n + m) + O(n * m)
#   - recursion stack + 2D dp array

class Solution2:
    def helper(self, text1: str, text2: str, i: int, j: int, dp) -> int:
        # Base case: out of bounds
        if i < 0 or j < 0:
            return 0

        # If already computed, return stored value
        if dp[i][j] != -1:
            return dp[i][j]

        if text1[i] == text2[j]:
            dp[i][j] = 1 + self.helper(text1, text2, i - 1, j - 1, dp)
        else:
            dp[i][j] = max(
                self.helper(text1, text2, i - 1, j, dp),
                self.helper(text1, text2, i, j - 1, dp),
            )
        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        # dp[i][j] will store LCS of text1[0..i] and text2[0..j]
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        return self.helper(text1, text2, n - 1, m - 1, dp)

# Solution 3 - Recursion (indices from 0 to n-1, m-1)
# Time Complexity:  O(2^(n+m)) - exponential
# Space Complexity: O(n + m)   - recursion stack

class Solution3:
    def helper(self, text1: str, text2: str, i: int, j: int) -> int:
        # Base case: if we go past the end of either string
        if i >= len(text1) or j >= len(text2):
            return 0

        if text1[i] == text2[j]:
            # Characters match: 1 + LCS of remaining suffixes
            return 1 + self.helper(text1, text2, i + 1, j + 1)

        # Else skip from text1 or from text2
        return max(
            self.helper(text1, text2, i + 1, j),
            self.helper(text1, text2, i, j + 1),
        )

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.helper(text1, text2, 0, 0)
    

# Solution 4 - Memoization (indices from 0 to n-1, m-1)
# Time Complexity:  O(n * m)
# Space Complexity: O(n + m) + O(n * m)

class Solution4:
    def helper(self, text1: str, text2: str, i: int, j: int, dp) -> int:
        # Base case: reached end of either string
        if i >= len(text1) or j >= len(text2):
            return 0

        # If already computed, return stored result
        if dp[i][j] != -1:
            return dp[i][j]

        if text1[i] == text2[j]:
            dp[i][j] = 1 + self.helper(text1, text2, i + 1, j + 1, dp)
        else:
            dp[i][j] = max(
                self.helper(text1, text2, i + 1, j, dp),
                self.helper(text1, text2, i, j + 1, dp),
            )
        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        return self.helper(text1, text2, 0, 0, dp)

# Solution 5 - Bottom-Up DP (Tabulation)
# Time Complexity:  O(n * m)
# Space Complexity: O(n * m)

class Solution5:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        # dp[i][j] = LCS length of text1[0..i-1], text2[0..j-1]
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        # Build the table bottom-up
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    # If characters match, take diagonal + 1
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # Otherwise, max of left and top
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]
    

# Solution 6 - Space Optimised Bottom-Up DP
# Time Complexity:  O(n * m)
# Space Complexity: O(m)  (only two rows at a time)

class Solution6:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        # prev[j] = dp for previous row (i-1)
        # curr[j] = dp for current row (i)
        prev = [0] * (m + 1)

        for i in range(1, n + 1):
            curr = [0] * (m + 1)  # fresh row for this i
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr  # move current row to previous

        return prev[m]


