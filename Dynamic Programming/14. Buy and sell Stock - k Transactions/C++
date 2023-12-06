// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

// Solution - Recursion TLE 

class Solution {
public:

    int helper(int ind, int k, vector<int>& prices) {
        if(ind < 0 || k<= 0) return 0;
        int exc = helper(ind-1, k, prices);
        int inc = 0;
        for(int m = 0; m<ind; m++) {
            if(prices[m] < prices[ind])
                inc = max(inc, prices[ind] - prices[m] + helper(m, k-1, prices));
        }
        return max(inc, exc);
    }

    int maxProfit(int k, vector<int>& prices) {
        return helper(prices.size() - 1, k, prices);
    }
};

// Recursion with Memoization

class Solution {
public:

    int helper(int ind, int k, vector<int>& prices, vector<vector<int>>& dp) {
        if(ind < 0 || k<= 0) return 0;
        if(dp[k][ind] != -1) return dp[k][ind];
        int exc = helper(ind-1, k, prices, dp);
        int inc = 0;
        for(int m = 0; m<ind; m++) {
            if(prices[m] < prices[ind])
                inc = max(inc, prices[ind] - prices[m] + helper(m, k-1, prices, dp));
        }
        return dp[k][ind] = max(inc, exc);
    }

    int maxProfit(int k, vector<int>& prices) {
        vector<vector<int>> dp(k+1, vector<int> (prices.size(), -1));
        return helper(prices.size() - 1, k, prices, dp);
    }
};

// Solution - Bottom Up

class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        vector<vector<int>> dp(k+1, vector<int> (n, 0));

        for(int i = 1; i<=k; i++) {
            for(int j = 1; j<n; j++) {
                //no transaction on jth day
                dp[i][j] = dp[i][j-1];
                //buy on m and sell on j
                for(int m = 0; m<j; m++) {
                    if(prices[m] < prices[j])
                        dp[i][j] = max(dp[i][j], prices[j] - prices[m] + dp[i-1][m]);
                }
            }
        }
        return dp[k][n-1];
    }
};