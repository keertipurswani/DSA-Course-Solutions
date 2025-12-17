# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, preorder, st, end):
        if st > end:
            return None

        root = TreeNode(preorder[st])

        # first index where element > root.val
        idx = bisect_right(preorder, preorder[st], st + 1, end + 1)

        root.left = self.helper(preorder, st + 1, idx - 1)
        root.right = self.helper(preorder, idx, end)

        return root

    def bstFromPreorder(self, preorder):
        return self.helper(preorder, 0, len(preorder) - 1)
    
# Solution 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, preorder, st, end):
        if st > end:
            return None

        root = TreeNode(preorder[st])

        # find first element greater than root.val
        idx = st
        while idx <= end:
            if preorder[idx] > preorder[st]:
                break
            idx += 1

        root.left = self.helper(preorder, st + 1, idx - 1)
        root.right = self.helper(preorder, idx, end)

        return root

    def bstFromPreorder(self, preorder):
        return self.helper(preorder, 0, len(preorder) - 1)

        
        