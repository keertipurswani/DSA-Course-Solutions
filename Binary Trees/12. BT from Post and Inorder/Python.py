# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, inorder, in_st, in_end, postorder, post_st, post_end, index_map):
        # base case
        if in_st > in_end or post_st > post_end:
            return None

        # last element in postorder is the root
        root_val = postorder[post_end]
        root = TreeNode(root_val)

        # index of root in inorder
        in_root_idx = index_map[root_val]

        # number of nodes in left subtree
        num_left = in_root_idx - in_st

        # build left subtree
        root.left = self.helper(
            inorder,
            in_st,
            in_root_idx - 1,
            postorder,
            post_st,
            post_st + num_left - 1,
            index_map
        )

        # build right subtree
        root.right = self.helper(
            inorder,
            in_root_idx + 1,
            in_end,
            postorder,
            post_st + num_left,
            post_end - 1,
            index_map
        )

        return root

    def buildTree(self, inorder, postorder):
        n = len(inorder)

        # value -> index mapping for inorder
        index_map = {}
        for i in range(n):
            index_map[inorder[i]] = i

        return self.helper(inorder, 0, n - 1, postorder, 0, n - 1, index_map)
