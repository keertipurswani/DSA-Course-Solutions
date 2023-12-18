// https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

int knapSack(int W, int wt[], int val[], int n) 
    { 
        vector<vector<int>> dp(n, vector<int> (W+1, 0));
        
        for (int j = wt[0]; j <= W; j++) {
            dp[0][j] = val[0];
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j <= W; j++) {
               
                int exc = dp[i - 1][j];
                int inc = INT_MIN;
                if (wt[i] <= j) 
                    inc = val[i] + dp[i - 1][j - wt[i]];
    
                dp[i][j] = max(inc, exc);
            }
        }
        
        return dp[n - 1][W];
    }