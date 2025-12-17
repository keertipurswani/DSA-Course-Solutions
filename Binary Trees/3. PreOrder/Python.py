# https://leetcode.com/problems/binary-tree-preorder-traversal

# Time Complexity - O(N)
# Space Complexity - O(N)

# Solution 1 - Add check in function

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
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res
    
# Solution 2 - Add checks before calls

class Solution:
    def helper(self, root, res) -> None:
        res.append(root.val)
        if root.left:
            self.helper(root.left, res)
        if root.right:
            self.helper(root.right, res)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            self.helper(root, res)
        return res