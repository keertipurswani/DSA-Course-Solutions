// https://leetcode.com/problems/house-robber-ii
// (TLE solutions - not the most optimised solutions)

class Solution {
    
    public int helper(int[] nums, int ind, int n) {
        if(ind >= n) return 0;
        int inc = nums[ind] + helper(nums, ind+2, n);
        int exc = helper(nums, ind+1, n);
        return Math.max(inc, exc);
    }

    public int rob(int[] nums) {
        if(nums.length == 1) return nums[0];
        return Math.max( helper(nums, 0, nums.length-1), helper(nums, 1, nums.length) );
    }

}