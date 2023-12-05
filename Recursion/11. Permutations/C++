// https://leetcode.com/problems/permutations

//Solution 1 -> 0 to n


class Solution {
public:

    void helper(vector<vector<int>>& res, vector<int>& nums, int ind, int n) {
        if(ind == n) {res.push_back(nums); return;}
        
        for(int i = ind; i<n; i++) {
            swap(nums[i], nums[ind]);
            helper(res, nums, ind+1, n);
            swap(nums[i], nums[ind]);
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> curr;
        helper(res, nums, 0, nums.size());
        return res;
    }
};

//Solution 2 -> n-1 to 0

class Solution {
public:

    void helper(vector<vector<int>>& res, vector<int>& nums, int ind, int n) {
        if(ind == 0) {res.push_back(nums); return;}
        for(int i = ind; i>=0; i--) {
            swap(nums[i], nums[ind]);
            helper(res, nums, ind-1, n);
            swap(nums[i], nums[ind]);
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> curr;
        helper(res, nums, nums.size()-1, nums.size());
        return res;
    }
};