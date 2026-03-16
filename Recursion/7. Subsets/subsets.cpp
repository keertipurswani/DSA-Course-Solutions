// https://leetcode.com/problems/subsets

// C++

//Solution 1 

class Solution {
public:

    void helper(vector<int>& nums, int ind, vector<int>& curr, vector<vector<int>>& res) {
        if(ind == nums.size()) {
            res.push_back(curr);
            return;
        }

        //inc
        curr.push_back(nums[ind]);
        helper(nums, ind+1, curr, res);
        curr.pop_back();

        //exc
        helper(nums, ind+1, curr, res);
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> curr;
        vector<vector<int>> res;

        helper(nums, 0, curr, res);

        return res;
    }
};

//Solution 2 - Passing curr by value and not popping back

class Solution {
public:

    void helper(vector<int>& nums, int ind, vector<int> curr, vector<vector<int>>& res) {
        if(ind == nums.size()) {
            res.push_back(curr);
            return;
        }

        //exc
        helper(nums, ind+1, curr, res);

        //inc
        curr.push_back(nums[ind]);
        helper(nums, ind+1, curr, res);
        //curr.pop_back();
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> curr;
        vector<vector<int>> res;

        helper(nums, 0, curr, res);

        return res;
    }
};
