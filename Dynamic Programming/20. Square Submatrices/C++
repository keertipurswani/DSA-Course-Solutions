// https://leetcode.com/problems/count-square-submatrices-with-all-ones

class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        int res = 0;
        vector<vector<int>> dp(n, vector<int> (m));
        for(int i = 0; i<n; i++) {
            dp[i][0] = matrix[i][0];
            if(dp[i][0] == 1) res++;
        }
        
        for(int j = 0; j<m; j++) {
            dp[0][j] = matrix[0][j];
            if(dp[0][j] == 1 && j != 0) res++;
        }
        
        for(int i = 1; i<n; i++) {
            for(int j = 1; j<m; j++) {
                if(matrix[i][j] == 1) {
                    res++;
                    dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]));
                    if(dp[i][j] > 1) {
                        res += (dp[i][j] - 1);
                    }
                } else {
                    dp[i][j] = 0;
                }
            }
        }
        return res;
    }
};

// Solution 2 

class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        int res = 0;
         for(int i = 0; i<matrix.size(); i++)
        {
            for(int j = 0; j<matrix[0].size(); j++)
            {
                if(i > 0 && j > 0 && matrix[i][j]>0)
                    matrix[i][j] = min({matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]}) + 1;
                
                res += matrix[i][j];               
            }
        }
        return res;
    }
};