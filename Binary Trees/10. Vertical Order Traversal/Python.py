# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        # hdist -> list of (vdist, value)
        mp = defaultdict(list)

        # queue stores (node, vdist, hdist)
        q = deque()
        q.append((root, 0, 0))   # root at (vdist=0, hdist=0)

        while q:
            node, vdist, hdist = q.popleft()
            mp[hdist].append((vdist, node.val))

            if node.left:
                q.append((node.left, vdist + 1, hdist - 1))
            if node.right:
                q.append((node.right, vdist + 1, hdist + 1))

        res = []

        # process columns from left to right
        for hdist in sorted(mp.keys()):
            temp = mp[hdist]

            # sort by vdist first, then value
            temp.sort()

            curr = []
            for _, val in temp:
                curr.append(val)

            res.append(curr)

        return res