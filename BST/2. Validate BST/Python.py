# https://leetcode.com/problems/validate-binary-search-tree

# Another Approach - check if inorder traversal is sorted or not

# Solution 1

class Solution:
    def helper(self, root, min_val, max_val):
        if root is None:
            return True

        if root.val <= min_val or root.val >= max_val:
            return False

        return (
            self.helper(root.left, min_val, root.val) and
            self.helper(root.right, root.val, max_val)
        )

    def isValidBST(self, root):
        return self.helper(root, float('-inf'), float('inf'))


# Solution 2

class Solution:
    def helper(self, root, min_node, max_node):
        if root is None:
            return True

        if (min_node is not None and root.val <= min_node.val) or \
           (max_node is not None and root.val >= max_node.val):
            return False

        return (
            self.helper(root.left, min_node, root) and
            self.helper(root.right, root, max_node)
        )

    def isValidBST(self, root):
        return self.helper(root, None, None)



