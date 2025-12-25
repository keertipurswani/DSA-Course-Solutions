# https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:

    def cloneUtil(self, node, mp):
        if node is None:
            return None

        # create copy of current node
        new_node = Node(node.val)
        mp[node] = new_node

        # clone neighbors
        for nei in node.neighbors:
            if nei not in mp:
                new_node.neighbors.append(self.cloneUtil(nei, mp))
            else:
                new_node.neighbors.append(mp[nei])

        return new_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp = {}   # maps original node -> cloned node
        return self.cloneUtil(node, mp)