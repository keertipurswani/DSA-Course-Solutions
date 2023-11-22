// https://leetcode.com/problems/generate-parentheses

class Solution {
    public:
        void helper(int o, int c, int n, string curr, vector<string>& res) {
            if(c == n) {
                res.push_back(curr);
                return;
            }
            if(o>c) helper(o, c+1, n, curr + ')', res);
            if(o<n) helper(o+1, c, n, curr + '(', res);
        }

        vector<string> generateParenthesis(int n) {
            vector<string> res;
            helper(0, 0, n, "", res);
            return res;
        }
};