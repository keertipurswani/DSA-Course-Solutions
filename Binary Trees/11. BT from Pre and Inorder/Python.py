# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self, preorder, pre_st, pre_end, inorder, in_st, in_end, index_map):
        if pre_st > pre_end or in_st > in_end:
            return None

        root_val = preorder[pre_st]
        root = TreeNode(root_val)

        in_root_idx = index_map[root_val]
        num_left = in_root_idx - in_st

        root.left = self.helper(
            preorder,
            pre_st + 1,
            pre_st + num_left,
            inorder,
            in_st,
            in_root_idx - 1,
            index_map
        )

        root.right = self.helper(
            preorder,
            pre_st + num_left + 1,
            pre_end,
            inorder,
            in_root_idx + 1,
            in_end,
            index_map
        )

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        index_map = {}
        for i in range(n):
            index_map[inorder[i]] = i

        return self.helper(preorder, 0, n - 1, inorder, 0, n - 1, index_map)
        