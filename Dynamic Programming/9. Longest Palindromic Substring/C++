// https://leetcode.com/problems/longest-palindromic-substring

// Recursion TLE

class Solution {
public:

    bool helper(int i, int j, string& s, string& res) {
        if(j<i) return false;
        bool isPal = false;

        if(i == j) isPal = true;
        else if(s[i] == s[j] && (j == i+1 || helper(i+1, j-1, s, res)))
            isPal = true;

        if(isPal) {
            if(j-i+1 > res.length())
                res = s.substr(i, j-i+1);
        } else {
            helper(i+1, j, s, res);
            helper(i, j-1, s, res);
        }
        return isPal;
    }

    string longestPalindrome(string s) {
        string res = "";
        helper(0, s.length() - 1, s, res);
        return res;
    }
};



// Bottom Up DP

class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();
        vector<vector<bool>> dp(n, vector<bool> (n, false));
        string res = s.substr(0, 1);
        for(int l = 1; l<=n ; l++) {
            for(int i = 0; i<=n-l ; i++) {
                int j = i+l-1;
                if(i == j) dp[i][j] = true;
                else if(s[i] == s[j] && (j == i+1 || dp[i+1][j-1])) {
                    dp[i][j] = true;
                    res = s.substr(i, l);
                }
            }
        }
        return res;
    }
};