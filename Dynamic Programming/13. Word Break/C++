// https://leetcode.com/problems/word-break

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.length();
        vector<vector<bool>> dp(n, vector<bool>(n, false));

        for(int l = 1; l<=n; l++) {
            for(int i = 0; i<=n-l; i++) {
                int j = i+l-1;
                if(find(wordDict.begin(), wordDict.end(), s.substr(i, l)) != wordDict.end())
                    dp[i][j] = true;
                else {
                    for(int k = i; k<j; k++)
                        dp[i][j] = dp[i][j] || (dp[i][k] && dp[k+1][j]);
                }
            }
        }
        return dp[0][n-1];
    }
};