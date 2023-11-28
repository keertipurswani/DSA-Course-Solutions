// https://leetcode.com/problems/edit-distance

// Solution 1 - Recursion TLE - indices 0 to n
// Time Complexity - O(3^(n+m)) - exponential
// Space Complexity -  O(n+m) - linear

class Solution {
public:
    int helper(string& s1, string& s2, int ind1, int ind2) {
        if(ind1 >= s1.size())
            return s2.size() - ind2;
        if(ind2 >= s2.size())
            return s1.size() - ind1;
        if(s1[ind1] == s2[ind2])
            return helper(s1, s2, ind1+1, ind2+1);
        return 1+min({helper(s1, s2, ind1, ind2+1), helper(s1, s2, ind1+1, ind2), helper(s1, s2, ind1+1, ind2+1)});
    }

    int minDistance(string word1, string word2) {
        return helper(word1, word2, 0, 0);
    }
};

// Solution 2 - Memoization
// Time Complexity - O(nm) - no of unique function calls
// Space Complexity -  O(n+m) + O(nm) (recursive stack space + 2d array)

class Solution {
public:
    int helper(string& s1, string& s2, int ind1, int ind2, vector<vector<int>>& dp) {
        if(ind1 >= s1.size())
            return s2.size() - ind2;
        if(ind2 >= s2.size())
            return s1.size() - ind1;
        if(dp[ind1][ind2] != -1)
            return dp[ind1][ind2];
        if(s1[ind1] == s2[ind2])
            return dp[ind1][ind2] = helper(s1, s2, ind1+1, ind2+1, dp);
        return dp[ind1][ind2] = 1+min({helper(s1, s2, ind1, ind2+1, dp), 
                        helper(s1, s2, ind1+1, ind2, dp), helper(s1, s2, ind1+1, ind2+1, dp)});
    }

    int minDistance(string word1, string word2) {
        vector<vector<int>> dp(word1.size(), vector<int> (word2.size(), -1));
        return helper(word1, word2, 0, 0, dp);
    }
};

// Solution 3 - Bottom Up DP
// Time Complexity - O(nm) 
// Space Complexity -  O(nm) 

class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size(), m = word2.size();
        vector<vector<int>> dp(n+1, vector<int> (m+1, 0));

        for(int i = 1; i<=n; i++)
            dp[i][0] = i;
        for(int j = 1; j<=m; j++)
            dp[0][j] = j;

        for(int i = 1; i<=n; i++) {
            for(int j = 1; j<=m ; j++) {
                if(word1[i-1] == word2[j-1])
                    dp[i][j] = dp[i-1][j-1];
                else dp[i][j] = 1 + min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]});
            }
        }

        return dp[n][m];
    }
};

//Solution 4 - Space Optimised Bottom Up DP
// Time Complexity - O(nm) 
// Space Complexity -  O(m) 

class Solution {
public:
    int minDistance(string word1, string word2) {
        int n = word1.size(), m = word2.size();
        vector<int> prev(m+1, 0);
        vector<int> curr(m+1, 0);

        for(int j = 1; j<=m; j++)
            prev[j] = j;

        for(int i = 1; i<=n; i++) {
            curr[0] = i;
            for(int j = 1; j<=m ; j++) {
                if(word1[i-1] == word2[j-1])
                    curr[j] = prev[j-1];
                else curr[j] = 1 + min({prev[j], curr[j-1], prev[j-1]});
            }
            prev = curr;
        }

        return prev[m]; //to handle n = 0 case
    }
};