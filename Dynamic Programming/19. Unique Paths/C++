// https://leetcode.com/problems/unique-paths

// Solution 1

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int> (n));
        for(int i = 0; i<m; i++) {
            for(int j = 0; j<n; j++) {
                if(i == 0 || j == 0) dp[i][j] = 1;
                else dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};

// Solution 2

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> prev(n);
        vector<int> curr(n);
        
        for(int j = 0; j<n; j++)
          prev[j] = 1;
        curr[0] = 1;

        for(int i = 1; i<m; i++) {
            for(int j = 1; j<n; j++) {
                curr[j] = prev[j] + curr[j-1];
            }
            prev = curr;
        }
        return prev[n-1];
    }
};