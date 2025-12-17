# https://leetcode.com/problems/path-sum-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root: Optional[TreeNode], targetSum: int,
               res: List[List[int]], curr: List[int]) -> None:
        if root is None:
            return

        # choose
        curr.append(root.val)

        # check if it's a leaf and sum matches
        if root.left is None and root.right is None and targetSum == root.val:
            res.append(curr[:])   # append a copy

        # explore
        self.helper(root.left, targetSum - root.val, res, curr)
        self.helper(root.right, targetSum - root.val, res, curr)

        # un-choose (backtrack)
        curr.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res: List[List[int]] = []
        curr: List[int] = []
        self.helper(root, targetSum, res, curr)
        return res
