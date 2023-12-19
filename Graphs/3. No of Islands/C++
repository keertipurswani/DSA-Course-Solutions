// https://leetcode.com/problems/number-of-islands

// Solution 1 - DFS

class Solution {
public:
    bool isSafe(int i, int j, int n, int m) {
        return (i>=0 && i<n && j>=0 && j<m);
    }

    void dfs(vector<vector<char>>& grid, vector<vector<bool>>& vis, int i, int j, int n, int m) {
        vis[i][j] = true;
        vector<vector<int>> dir = {{0, -1}, {0, 1}, {1, 0}, {-1, 0}};
        for(int k = 0; k<4; k++) {
            int newi = i + dir[k][0];
            int newj = j + dir[k][1];
            if(isSafe(newi, newj, n, m) && grid[newi][newj] == '1' && !vis[newi][newj]) 
                dfs(grid, vis, newi, newj, n, m);
        }
    }

    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int res = 0;
        vector<vector<bool>> vis(n, vector<bool> (m, false));
        for(int i = 0; i<n; i++) {
            for(int j = 0; j<m; j++) {
                if(!vis[i][j] && grid[i][j] == '1') {
                    dfs(grid, vis, i, j, n, m);
                    res++;
                }
            }
        }
        return res;
    }
};