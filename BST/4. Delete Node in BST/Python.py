# https://leetcode.com/problems/delete-node-in-a-bst

# Solution 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # case 1: no left child
            if root.left is None:
                return root.right

            # case 2: no right child
            if root.right is None:
                return root.left

            # case 3: two children
            # find inorder successor (smallest in right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left

            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root
    

# Solution 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # case 1: no right child
            if root.right is None:
                return root.left

            # case 2: no left child
            if root.left is None:
                return root.right

            # case 3: two children
            # find inorder predecessor (largest in left subtree)
            predecessor = root.left
            while predecessor.right:
                predecessor = predecessor.right

            # replace value
            root.val = predecessor.val

            # delete predecessor from left subtree
            root.left = self.deleteNode(root.left, predecessor.val)

        return root