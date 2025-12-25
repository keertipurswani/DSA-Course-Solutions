# https://leetcode.com/problems/is-graph-bipartite

# Solution 1 - DFS

class Solution:
    def dfs(self, graph, vis, curr, color):
        vis[curr] = color

        for neighbor in graph[curr]:
            if vis[neighbor] == -1:
                if not self.dfs(graph, vis, neighbor, 1 - color):
                    return False
            else:
                if vis[neighbor] == color:
                    return False

        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        vis = [-1] * n   # -1 means uncolored

        for i in range(n):
            if vis[i] == -1:
                if not self.dfs(graph, vis, i, 0):
                    return False

        return True
    

# Solution 2 - BFS

class Solution:

    def bfs(self, graph, vis, start, color):
        q = deque()
        vis[start] = color
        q.append(start)

        while q:
            curr = q.popleft()
            for neighbor in graph[curr]:
                if vis[neighbor] == -1:
                    vis[neighbor] = 1 - vis[curr]
                    q.append(neighbor)
                elif vis[neighbor] == vis[curr]:
                    return False

        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        vis = [-1] * n   # -1 means uncolored

        for i in range(n):
            if vis[i] == -1:
                if not self.bfs(graph, vis, i, 0):
                    return False

        return True