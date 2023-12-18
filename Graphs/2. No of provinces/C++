// https://leetcode.com/problems/number-of-provinces

class Solution {
public:
    void dfs(vector<vector<int>>& isConnected, int n, int curr, vector<bool>& vis) {
        for(int i = 0; i<n; i++) {
            if(isConnected[curr][i] == 1 && !vis[i]) {
                vis[i] = true;
                dfs(isConnected, n, i, vis);
            }
        }
    }

    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<bool> vis(n, false);
        int cnt = 0;

        for(int i = 0; i<n; i++) {
            if(!vis[i]) {
                cnt++;
                dfs(isConnected, n, i, vis);
            }
        }
        return cnt;
    }
};