// https://leetcode.com/problems/house-robber
// (TLE solutions - not the most optimised solutions)

// Solution 1 - 0 to n

class Solution {

    public int helper(int[] nums, int ind, int n) {
        if(ind >= n) return 0;
        int inc = nums[ind] + helper(nums, ind+2, n);
        int exc = helper(nums, ind+1, n);
        return Math.max(inc, exc);
    }

    public int rob(int[] nums) {
        return helper(nums, 0, nums.length);
    }
}

// Solution 2 - n to 0

class Solution {
    public int helper(int[] nums, int ind) {
        if(ind < 0) return 0;
        int inc = nums[ind] + helper(nums, ind-2);
        int exc = helper(nums, ind-1);
        return Math.max(inc, exc);
    }

    public int rob(int[] nums) {
        return helper(nums, nums.length - 1);
    }
}