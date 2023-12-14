// https://leetcode.com/problems/unique-binary-search-trees

// Solution 1

class Solution {
public:
    int numTrees(int n) {
        vector<int> dp(n+1, 0);
        dp[0] = dp[1] = 1;
        for(int i = 2; i <= n; i++) {
            for(int root = 1; root <= i; root++) 
                dp[i] += dp[root-1] * dp[i-root];
        }
        return dp[n];
    }
};

// Solution 2

class Solution {
public:
    int numTrees(int n) {
        vector<int> dp(n+1, 0);
        dp[0] = dp[1] = 1;
        for(int i = 2; i <= n; i++) {
            for(int root = 1; root <= i/2; root++) 
                dp[i] += dp[root-1] * dp[i-root];
            dp[i] = dp[i]*2;
            if(i%2 == 1)
                dp[i] += dp[i/2] * dp[i/2];
        }
        return dp[n];
    }
};