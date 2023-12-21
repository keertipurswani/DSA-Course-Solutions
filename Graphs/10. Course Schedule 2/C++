// https://leetcode.com/problems/course-schedule-ii
// Topological Sorting

class Solution {
public:
    bool dfs(int curr, int n, vector<vector<int>>& graph, vector<bool>& visited, vector<bool>& visiting, vector<int>& res) {
        visiting[curr] = true;

        for(int neighbor : graph[curr]) {
            if(visiting[neighbor])
                return false;
            if(!visited[neighbor]) {
                if(!dfs(neighbor, n, graph, visited, visiting, res))
                    return false;
            }
        }

        visited[curr] = true;
        visiting[curr] = false;
        res.push_back(curr);
        return true;
    }

    vector<int> findOrder(int n, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(n);
        for(auto prerequisite : prerequisites) 
            graph[prerequisite[0]].push_back(prerequisite[1]);

        vector<bool> visited(n, false);
        vector<bool> visiting(n, false);
        vector<int> res;

        for(int i = 0; i<n; i++) {
            if(!visited[i]) {
                if(!dfs(i, n, graph, visited, visiting, res))
                    return {};
            }
        }
        return res;
    }
};