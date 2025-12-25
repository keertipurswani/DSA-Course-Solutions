# https://leetcode.com/problems/numbers-with-same-consecutive-differences

# Solution 1 - DFS

class Solution:
    def dfs(self, num, n, k, res):
        if n == 0:
            res.append(num)
            return

        x = num % 10

        if x + k <= 9:
            self.dfs(num * 10 + x + k, n - 1, k, res)

        if k != 0 and x - k >= 0:
            self.dfs(num * 10 + x - k, n - 1, k, res)

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        for i in range(1, 10):
            self.dfs(i, n - 1, k, res)
        return res
    

# Solution 2

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        q = deque()

        for i in range(1, 10):
            q.append(i)

        length = 1

        while q and length < n:
            length += 1
            size = len(q)

            for _ in range(size):
                f = q.popleft()
                x = f % 10

                if x + k <= 9:
                    q.append(f * 10 + x + k)

                if k != 0 and x - k >= 0:
                    q.append(f * 10 + x - k)

        return list(q)