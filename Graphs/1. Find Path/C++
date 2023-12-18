// https://leetcode.com/problems/find-if-path-exists-in-graph

// Solution 1 - Adj Matrix and DFS
// Memory Limit Exceeded

class Solution {
public:
    bool helper(int n, vector<vector<int>> &graph, int src, int dest, vector<bool>& vis) {
        if(src == dest) return true;
        vis[src] = true;
        for(int i = 0; i<n; i++) {
            if(graph[src][i] && !vis[i]) {
                if(helper(n, graph, i, dest, vis))
                    return true;
            }
        }
        return false;
    }

    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        vector<vector<int>> graph(n, vector<int>(n, 0)); // can keep of bool as well
        vector<bool> visited(n, false);
        for(auto edge : edges) {
            int u = edge[0], v = edge[1];
            graph[u][v] = 1;
            graph[v][u] = 1;
        }
        return helper(n, graph, source, destination, visited);
    }
};

// Solution 2 - Adj List and DFS

class Solution {
public:

    bool helper(vector<vector<int>> &graph, int src, int dest, vector<bool>& vis) {
        if(src == dest) return true;
        vis[src] = true;
        for(auto neighbor : graph[src]) {
            //can merge into one if condition - this is for clarity
            if(!vis[neighbor]) {
                if(helper(graph, neighbor, dest, vis))
                    return true;
            }
        }
        return false;
    }

    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        vector<vector<int>> graph(n, vector<int>());
        vector<bool> visited(n, false);
        for(auto edge : edges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        return helper(graph, source, destination, visited);
    }
};

// Solution 3 - Adj Matrix and BFS
// Memory Limit Exceeded

class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        vector<vector<int>> graph(n, vector<int>(n, 0)); // can keep of bool as well
        vector<bool> vis(n, false);
        for(auto edge : edges) {
            int u = edge[0], v = edge[1];
            graph[u][v] = 1;
            graph[v][u] = 1;
        }

        queue<int> q;
        q.push(source);
        vis[source] = true;

        while(!q.empty()) {
            int curr = q.front();
            q.pop();
            if(curr == destination)
                return true;
            for(int i = 0; i<n; i++) {
                if(graph[curr][i] && !vis[i]) {
                    q.push(i);
                    vis[i] = true;
                }
            }
        }

        return false;
    }
};

// Solution 4 - Adj List and BFS

class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        vector<vector<int>> graph(n, vector<int>());
        vector<bool> vis(n, false);
        for(auto edge : edges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        queue<int> q;
        q.push(source);
        vis[source] = true;

        while(!q.empty()) {
            int curr = q.front();
            q.pop();
            if(curr == destination)
                return true;
            for(auto neighbor : graph[curr]) {
                if(!vis[neighbor]) {
                    q.push(neighbor);
                    vis[neighbor] = true;
                }
            }
        }

        return false;
    }
};