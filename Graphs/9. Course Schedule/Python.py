# https://leetcode.com/problems/course-schedule
# Topological Sorting

class Solution:
    def dfs(self, curr, graph, visited, visiting):
        visiting[curr] = True

        for neighbor in graph[curr]:
            if visiting[neighbor]:
                return False
            if not visited[neighbor]:
                if not self.dfs(neighbor, graph, visited, visiting):
                    return False

        visiting[curr] = False
        visited[curr] = True
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacency list: prereq -> course
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = [False] * numCourses
        visiting = [False] * numCourses

        for i in range(numCourses):
            if not visited[i]:
                if not self.dfs(i, graph, visited, visiting):
                    return False

        return True
