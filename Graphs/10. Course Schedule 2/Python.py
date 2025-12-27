# https://leetcode.com/problems/course-schedule-ii
# Topological Sorting

class Solution:
    def dfs(self, curr, graph, visited, visiting, res):
        visiting[curr] = True

        for neighbor in graph[curr]:
            if visiting[neighbor]:
                return False
            if not visited[neighbor]:
                if not self.dfs(neighbor, graph, visited, visiting, res):
                    return False

        visiting[curr] = False
        visited[curr] = True
        res.append(curr) 
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjacency list: prereq -> course
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = [False] * numCourses
        visiting = [False] * numCourses
        res = []

        for i in range(numCourses):
            if not visited[i]:
                if not self.dfs(i, graph, visited, visiting, res):
                    return []

        return res[::-1]   # reverse to get correct topological order
