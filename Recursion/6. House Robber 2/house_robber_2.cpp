// https://leetcode.com/problems/house-robber-ii
// (TLE solutions - not the most optimised solutions)

class Solution {
public:
    int helper(vector<int>& nums, int ind, int n) {
        if(ind >= n) return 0;
        int inc = nums[ind] + helper(nums, ind+2, n);
        int exc = helper(nums, ind+1, n);
        return max(inc, exc);
    }

    int rob(vector<int>& nums) {
        if(nums.size() == 1) return nums[0];
        return max( helper(nums, 0, nums.size()-1), helper(nums, 1, nums.size()));
    }
};