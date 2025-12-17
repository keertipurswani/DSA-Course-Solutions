# https://leetcode.com/problems/binary-tree-postorder-traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, res) -> None:
        if root is None:
            return
        self.helper(root.left, res)
        self.helper(root.right, res)
        res.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res