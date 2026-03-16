//https://leetcode.com/problems/combinations

class Solution {
public:
    void helper(int n, int k, int i, vector<int>& curr, vector<vector<int>>& res) {
        if(curr.size() == k) {
            res.push_back(curr);
            return;
        }
        if(i > n) return;

        //inc
        curr.push_back(i);
        helper(n, k, i+1, curr, res);
        curr.pop_back();

        //exc
        helper(n, k, i+1, curr, res);
    }

    vector<vector<int>> combine(int n, int k) {
        vector<int> curr;
        vector<vector<int>> res;

        helper(n, k, 1, curr, res);
        return res;
    }
};
