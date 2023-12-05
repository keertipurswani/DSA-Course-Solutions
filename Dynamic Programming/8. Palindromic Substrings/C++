// https://leetcode.com/problems/palindromic-substrings

// Solution - Recursion with Memoization

class Solution {
public:

    bool helper(int i, int j, string& s, vector<vector<int>>& dp) {
        if(j<i) return false;
        if(i == j) return dp[i][j] = true;
        if(dp[i][j] != -1) return dp[i][j];

        helper(i+1, j, s, dp);
        helper(i, j-1, s, dp);

        if(s[i] == s[j] && (j == i+1 || helper(i+1, j-1, s, dp)))
            dp[i][j] = true;
        else dp[i][j] = false;

        return dp[i][j];
    }

    int countSubstrings(string s) {
        int n = s.size();
        vector<vector<int>> dp(n, vector<int> (n, -1));
        helper(0, n-1, s, dp);
        int res = 0;
        for(auto row : dp) {
            for(auto ele : row)
                res += (ele == 1);
        }
        return res;
    }
};

// Solution - Recursion with Memoization - Passing res as reference

class Solution {
public:

    bool helper(int i, int j, string& s, vector<vector<int>>& dp, int& res) {
        if(j<i) return false;
        if(i == j) {
            if(dp[i][j] == -1) res++; 
            return dp[i][j] = true; 
        }
        if(dp[i][j] != -1) return dp[i][j];

        helper(i+1, j, s, dp, res);
        helper(i, j-1, s, dp, res);

        if(s[i] == s[j] && (j == i+1 || helper(i+1, j-1, s, dp, res))) {
            res++; dp[i][j] = true;
        }
        else dp[i][j] = false;

        return dp[i][j];
    }

    int countSubstrings(string s) {
        int n = s.size();
        vector<vector<int>> dp(n, vector<int> (n, -1));
        int res = 0;
        helper(0, n-1, s, dp, res);
        return res;
    }
};

// Solution - Bottom Up DP

class Solution {
public:
    int countSubstrings(string s) {
        int n = s.length();
        int res = 0;
        vector<vector<bool>> dp(n, vector<bool> (n));

        for(int l = 1; l<=n; l++) {
            for(int i = 0; i<=n-l; i++) {
                int j = i+l-1;
                if(i == j) dp[i][j] = true;
                else if(j == i+1) dp[i][j] = s[i] == s[j];
                else if(s[i] == s[j]) dp[i][j] = dp[i+1][j-1];
                if(dp[i][j]) res++;
            }
        }
        return res;
    }
};