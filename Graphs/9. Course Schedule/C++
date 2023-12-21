// https://leetcode.com/problems/course-schedule
// Topological Sorting

class Solution {
public:

    bool dfs(int curr, int n, vector<vector<int>>& graph, vector<bool>& visited, vector<bool>& visiting) {
        visiting[curr] = true;

        for(auto neighbor : graph[curr]) {
            if(visiting[neighbor])
                return false;
            if(!visited[neighbor]) {
                if(!dfs(neighbor, n, graph, visited, visiting))
                    return false;
            }
        }

        visiting[curr] = false;
        visited[curr] = true;
        return true;
    }

    bool canFinish(int n, vector<vector<int>>& prerequisites) {
        //form adj list
        vector<vector<int>> graph(n);
        for(auto prerequisite : prerequisites) 
            graph[prerequisite[0]].push_back(prerequisite[1]);
        
        vector<bool> visited(n, false);
        vector<bool> visiting(n, false);

        for(int i = 0; i<n; i++) {
            if(!visited[i]) {
                if(!dfs(i, n, graph, visited, visiting))
                    return false;
            }
        }
        return true;
    }
};