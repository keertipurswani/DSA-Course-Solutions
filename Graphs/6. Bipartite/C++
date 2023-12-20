// https://leetcode.com/problems/is-graph-bipartite

// Solution 1 - DFS

class Solution {
public:
    bool dfs(vector<vector<int>>& graph, vector<int>& vis, int curr, int color) {
        vis[curr] = color;
        for(int neighbor : graph[curr]) {
            if(vis[neighbor] == -1) {
                if(dfs(graph, vis, neighbor, !color) == false)
                    return false;
            } else {
                if(vis[neighbor] == color)
                    return false;
            }
        } 
        
        return true;
    }

    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> vis(n, -1); // means not colored

        for(int i = 0; i<n; i++) {
            if(vis[i] == -1 && !dfs(graph, vis, i, 0)) // can pass 1 also
                return false;
        }
        return true;
    }
};

// Solution 2 - BFS

class Solution {
public:
    bool bfs(vector<vector<int>>& graph, vector<int>& vis, int start, int color) {
        vis[start] = color;
        queue<int> q;
        q.push(start);
        while(!q.empty()) {
            int curr = q.front();
            q.pop();
            for(int neighbor : graph[curr]) {
                if(vis[neighbor] == -1) {
                    vis[neighbor] = 1-vis[curr]; //or !vis[curr]
                    q.push(neighbor);
                } else if(vis[neighbor] == vis[curr])
                    return false;
            }
        }
        return true;
    }

    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> vis(n, -1); // means not colored

        for(int i = 0; i<n; i++) {
            if(vis[i] == -1 && !bfs(graph, vis, i, 0))
                return false;
        }
        return true;
    }
};