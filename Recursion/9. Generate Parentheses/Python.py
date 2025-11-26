# https://leetcode.com/problems/generate-parentheses

class Solution:
    def helper(self, noOfOpen, noOfClosed, n, curr, res):
        if noOfClosed == n:
            res.append(curr)
            return

        if noOfOpen < n:
            self.helper(noOfOpen + 1, noOfClosed, n, curr + '(', res)

        if noOfOpen > noOfClosed:
            self.helper(noOfOpen, noOfClosed + 1, n, curr + ')', res)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(0, 0, n, "", res)
        return res