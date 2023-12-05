// https://leetcode.com/problems/wildcard-matching

// Solution 1 - Recursion TLE - indices 0,0 to n, m
// Time Complexity - O(2^(n+m)) - exponential
// Space Complexity -  O(n+m) - linear

class Solution {
public:

    bool helper(string s, string p, int ind1, int ind2) {

        //both ended together
        if(ind1 >= s.length() && ind2 >= p.length())
            return true;

        //pattern ended but string didnt
        if(ind2 >= p.length()) return false;

        //string ended but pattern didnt. pattern can be all * and can point to empty sequence
        if(ind1 >= s.length()) {
            if(p[ind2] == '*') return helper(s, p, ind1, ind2+1);
            return false;
        } 

        if(s[ind1] == p[ind2] || p[ind2] == '?')
            return helper(s, p, ind1+1, ind2+1);
        
        else if(p[ind2] == '*')
            return helper(s, p, ind1, ind2+1) || helper(s, p, ind1+1, ind2);

        return false;
    }

    bool isMatch(string s, string p) {
        return helper(s, p, 0, 0);
    }
};


// Solution 2 - Memoization (indices from n, m to 0)
// Time Complexity - O(nm) - no of unique function calls
// Space Complexity -  O(n+m) + O(nm) (recursive stack space + 2d array)

class Solution {
public:

    bool helper(string s, string p, int ind1, int ind2, vector<vector<int>>& dp) {

        //both ended together
        if(ind1 >= s.length() && ind2 >= p.length())
            return 1;

        //pattern ended but string didnt
        if(ind2 >= p.length()) return 0;

        //string ended but pattern didnt. pattern can be all * and can point to empty sequence
        if(ind1 >= s.length()) {
            if(p[ind2] == '*') return helper(s, p, ind1, ind2+1, dp);
            return 0;
        } 

        if(dp[ind1][ind2] != -1) return dp[ind1][ind2];

        if(s[ind1] == p[ind2] || p[ind2] == '?')
            return dp[ind1][ind2] = helper(s, p, ind1+1, ind2+1, dp);
        
        else if(p[ind2] == '*')
            return dp[ind1][ind2] = helper(s, p, ind1, ind2+1, dp) || helper(s, p, ind1+1, ind2, dp);

        return dp[ind1][ind2] = 0;
    }

    bool isMatch(string s, string p) {
        vector<vector<int>> dp(s.length(), vector<int> (p.length(), -1));
        return helper(s, p, 0, 0, dp);
    }
};


// Solution 3 - Recursion TLE - indices n,m to 0,0
// Time Complexity - O(2^(n+m)) - exponential
// Space Complexity -  O(n+m) - linear

class Solution {
public:
    bool helper(string s, string p, int ind1, int ind2) {

        //both ended together
        if(ind1 < 0 && ind2 < 0)
            return true;

        //pattern ended but string didnt
        if(ind2 < 0) return false;

        //string ended but pattern didnt. pattern can be all * and can point to empty sequence
        if(ind1 < 0) {
            if(p[ind2] == '*') return helper(s, p, ind1, ind2-1);
            return false;
        } 

        if(s[ind1] == p[ind2] || p[ind2] == '?')
            return helper(s, p, ind1-1, ind2-1);
        
        else if(p[ind2] == '*')
            return helper(s, p, ind1, ind2-1) || helper(s, p, ind1-1, ind2);

        return false;
    }

    bool isMatch(string s, string p) {
        return helper(s, p, s.length() - 1, p.length() - 1);
    }
};

// Solution 4 - Recursion TLE - indices n, m to 0,0
// Time Complexity - O(2^(n+m)) - exponential
// Space Complexity -  O(n+m) - linear

class Solution {
public:
    bool helper(string& s, string& p, int ind1, int ind2, vector<vector<int>>& dp) {

        //both ended together
        if(ind1 < 0 && ind2 < 0)
            return true;

        //pattern ended but string didnt
        if(ind2 < 0) return false;

        //string ended but pattern didnt. pattern can be all * and can point to empty sequence
        if(ind1 < 0) {
            if(p[ind2] == '*') return helper(s, p, ind1, ind2-1, dp);
            return false;
        } 

        if(dp[ind1][ind2] != -1) return dp[ind1][ind2];

        if(s[ind1] == p[ind2] || p[ind2] == '?')
            return dp[ind1][ind2] = helper(s, p, ind1-1, ind2-1, dp);
        
        else if(p[ind2] == '*')
            return dp[ind1][ind2] = helper(s, p, ind1, ind2-1, dp) || helper(s, p, ind1-1, ind2, dp);

        return dp[ind1][ind2] = false;
    }

    bool isMatch(string s, string p) {
        vector<vector<int>> dp(s.length(), vector<int> (p.length(), -1));
        return helper(s, p, s.length() - 1, p.length() - 1, dp);
    }
};

// Solution 5 - Bottom Up DP
// Time Complexity - O(nm) 
// Space Complexity -  O(nm) 

class Solution {
public:
    bool isMatch(string s, string p) {
        int n = s.length(), m = p.length();

        vector<vector<bool>> dp(n+1, vector<bool> (m+1, false));

        dp[0][0] = true;

        for(int j = 1; j<=m; j++)
            if(p[j-1] == '*') 
                dp[0][j] = dp[0][j-1];

        for(int i = 1; i<=n ; i++) {
            for(int j = 1; j<=m; j++) {
                if(s[i-1] == p[j-1] || p[j-1] == '?')
                    dp[i][j] = dp[i-1][j-1];
                else if(p[j-1] == '*')
                    dp[i][j] = dp[i-1][j] || dp[i][j-1];
            }
        }

        return dp[n][m];
    }
};

// Solution 6 - Space Optimised
// Time Complexity - O(nm) 
// Space Complexity -  O(m) 

class Solution {
public:
    bool isMatch(string s, string p) {
        int n = s.length(), m = p.length();

        vector<bool> prev(m+1, false);
        vector<bool> curr(m+1, false);

        prev[0] = true;

        for(int j = 1; j<=m; j++)
            if(p[j-1] == '*') 
                prev[j] = prev[j-1];

        for(int i = 1; i<=n ; i++) {
            for(int j = 1; j<=m; j++) {
                if(s[i-1] == p[j-1] || p[j-1] == '?')
                    curr[j] = prev[j-1];
                else if(p[j-1] == '*')
                    curr[j] = prev[j] || curr[j-1];
                else curr[j] = false; // important for space optimised solution
            }
            prev = curr;
        }

        return prev[m];
    }
};