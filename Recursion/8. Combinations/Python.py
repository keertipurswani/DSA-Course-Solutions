class Solution:
    def helper(self, n, k, i, curr, res):
        if len(curr) == k:
            res.append(curr[:])
            return
        
        if i > n:
            return

        # include i
        curr.append(i)
        self.helper(n, k, i + 1, curr, res)
        curr.pop()

        # exclude i
        self.helper(n, k, i + 1, curr, res)

    def combine(self, n: int, k: int):
        res = []
        self.helper(n, k, 1, [], res)
        return res
