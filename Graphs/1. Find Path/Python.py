# https://leetcode.com/problems/find-if-path-exists-in-graph

# Solution 1 - Adj Matrix and DFS
# Memory Limit Exceeded

class Solution:
    def helper(self, n, graph, src, dest, vis):
        if src == dest:
            return True

        vis[src] = True

        for i in range(n):
            if graph[src][i] == 1 and not vis[i]:
                if self.helper(n, graph, i, dest, vis):
                    return True
        return False
        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[0] * n for _ in range(n)]
        visited = [False] * n

        for u, v in edges:
            graph[u][v] = 1
            graph[v][u] = 1

        return self.helper(n, graph, source, destination, visited)
    

# Solution 2 - Adj List and DFS

class Solution:
    def helper(self, graph, src, dest, vis):
        if src == dest:
            return True

        vis[src] = True

        for neighbor in graph[src]:
            if not vis[neighbor]:
                if self.helper(graph, neighbor, dest, vis):
                    return True
        return False

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)] # list of n empty lists
        visited = [False] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        return self.helper(graph, source, destination, visited)


# Solution 3 - Adj Matrix and BFS
# Memory Limit Exceeded

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[0] * n for _ in range(n)]
        vis = [False] * n

        for u, v in edges:
            graph[u][v] = 1
            graph[v][u] = 1

        q = deque()
        q.append(source)
        vis[source] = True

        while q:
            curr = q.popleft()
            if curr == destination:
                return True

            for i in range(n):
                if graph[curr][i] == 1 and not vis[i]:
                    q.append(i)
                    vis[i] = True

        return False
    
# Solution 4 - Adj List and BFS

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        vis = [False] * n

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque()
        q.append(source)
        vis[source] = True

        while q:
            curr = q.popleft()
            if curr == destination:
                return True

            for neighbor in graph[curr]:
                if not vis[neighbor]:
                    q.append(neighbor)
                    vis[neighbor] = True

        return False

