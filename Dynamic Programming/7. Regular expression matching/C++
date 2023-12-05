//https://leetcode.com/problems/regular-expression-matching

// Solution - Recursion

class Solution {
public:
    bool helper(string s, string p, int ind1, int ind2) {
        if(ind1 < 0 && ind2 < 0) return true;
        //pattern is empty, string is not
        if(ind2 < 0) return false;
        //string is empty, pattern is not
        if(ind1 < 0) {
            if(p[ind2] == '*') return helper(s, p, ind1, ind2-2);
            else return false;
        }

        if(s[ind1] == p[ind2] || p[ind2] == '.')
            return helper(s, p, ind1-1, ind2-1);
        if(p[ind2] == '*') {
            //* represents zero of the preceding element
            if(helper(s, p, ind1, ind2-2)) return true;
            //s[ind1] is part of the sequence represented by *
            if(ind2>0 && (s[ind1] == p[ind2-1] || p[ind2-1] == '.'))
                return helper(s, p, ind1-1, ind2);
        }
        return false;
    }

    bool isMatch(string s, string p) {
        return helper(s, p, s.length() - 1, p.length() - 1);
    }
};

//Solution - Recursion with Memoization

class Solution {
public:
    bool helper(string s, string p, int ind1, int ind2, vector<vector<int>>& dp) {
        if(ind1 < 0 && ind2 < 0) return true;
        //pattern is empty, string is not
        if(ind2 < 0) return false;
        //string is empty, pattern is not
        if(ind1 < 0) {
            if(p[ind2] == '*') return helper(s, p, ind1, ind2-2, dp);
            else return false;
        }

        if(dp[ind1][ind2] != -1) return dp[ind1][ind2];

        if(s[ind1] == p[ind2] || p[ind2] == '.')
            return dp[ind1][ind2] = helper(s, p, ind1-1, ind2-1, dp);
        if(p[ind2] == '*') {
            //* represents zero of the preceding element
            if(helper(s, p, ind1, ind2-2, dp)) return dp[ind1][ind2] = true;
            //s[ind1] is part of the sequence represented by *
            if(ind2>0 && (s[ind1] == p[ind2-1] || p[ind2-1] == '.'))
                return dp[ind1][ind2] = helper(s, p, ind1-1, ind2, dp);
        }
        return dp[ind1][ind2] = false;
    }

    bool isMatch(string s, string p) {
        vector<vector<int>> dp(s.size(), vector<int> (p.size(), -1));
        helper(s, p, s.length() - 1, p.length() - 1, dp);
        return dp[s.size() - 1][p.size() - 1];
    }
};

//Solution - Bottom Up DP

class Solution {
public:
    bool isMatch(string s, string p) {
        int n = s.size(), m = p.size();
        bool dp[n+1][m+1];
        dp[0][0] = true;

        for(int i = 1; i<=n ; i++)
            dp[i][0] = false;
        for(int j = 1; j<=m ; j++)
            dp[0][j] = (j>1 && p[j-1] == '*') ? dp[0][j-2] : false;

        for(int i = 1; i<=n ; i++) {
            for(int j = 1; j<=m ; j++) {
                if(s[i-1] == p[j-1] || p[j-1] == '.')  
                    dp[i][j] = dp[i-1][j-1];
                else if(p[j-1] == '*' && j>1) {
                    dp[i][j] = dp[i][j-2];
                    if(s[i-1] == p[j-2] || p[j-2] == '.')
                        dp[i][j] = dp[i][j] || dp[i-1][j];
                } else dp[i][j] = false;
            }
        }
        return dp[n][m];
    }
};