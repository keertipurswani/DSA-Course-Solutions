# https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self, root, curr_sum):
        if root is None:
            return 0

        curr_sum = curr_sum * 10 + root.val

        # if leaf node
        if root.left is None and root.right is None:
            return curr_sum

        return (
            self.helper(root.left, curr_sum) +
            self.helper(root.right, curr_sum)
        )

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)
    

# Solution 2 with Default Parameter

class Solution:
    def sumNumbers(self, root, curr_sum=0):
        if root is None:
            return 0

        curr_sum = curr_sum * 10 + root.val

        # leaf node
        if root.left is None and root.right is None:
            return curr_sum

        return (
            self.sumNumbers(root.left, curr_sum) +
            self.sumNumbers(root.right, curr_sum)
        )
        