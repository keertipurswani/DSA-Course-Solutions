// https://leetcode.com/problems/palindrome-partitioning


class Solution {
public:

        void helper(vector<vector<string>>& res, vector<string>& curr, int ind, string& s,
                vector<vector<bool>>& dp)
        {
            if(ind >= s.length()) {
                res.push_back(curr);
                return;
            }
            for(int i = ind; i<s.length(); i++){
                if(dp[ind][i]) {
                    curr.push_back(s.substr(ind, i-ind+1));
                    helper(res, curr, i+1, s, dp);
                    curr.pop_back();
                }
            }
        }

        vector<vector<string>> partition(string s) {
            int n = s.length();
            vector<vector<string>> res;
            if(n==0)
                return res;
            vector<vector<bool>> dp(n, vector<bool> (n, false));

            for(int l = 1; l<=n; l++){
                for(int i = 0; i<=n-l; i++){
                    int j = i+l-1;
                    if(i == j) dp[i][j] = true;
                    else if(s[i] == s[j] && (j == i+1 || dp[i+1][j-1])) 
                        dp[i][j] = true;
                }
            }

            vector<string> curr;
            helper(res, curr, 0, s, dp);
            return res;
        }
};