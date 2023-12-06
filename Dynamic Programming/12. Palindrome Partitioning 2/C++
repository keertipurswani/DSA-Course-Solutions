// https://leetcode.com/problems/palindrome-partitioning-ii

// Solution - TLE

class Solution {
public:
    int minCut(string s) {
        int n = s.length();
        vector<vector<int>> dp(n, vector<int> (n));

        for(int l = 1; l<=n; l++) {
            for(int i = 0; i<=n-l; i++) {
                int j = i+l-1;
                if(i == j) dp[i][j] = 0;
                else if(j == i+1) dp[i][j] = s[i] == s[j] ? 0 : 1;
                else {
                    //substring i to j is a pal
                    if(s[i] == s[j] && dp[i+1][j-1] == 0) dp[i][j] = 0;
                    else {
                        dp[i][j] = j-i;
                        for(int k = i; k<j; k++) {
                            dp[i][j] = min(dp[i][j], 1+dp[i][k]+dp[k+1][j]);
                        }
                    }
                }
            }
        }

        return dp[0][n-1];
    }
};