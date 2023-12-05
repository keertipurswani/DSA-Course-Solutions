// https://leetcode.com/problems/partition-equal-subset-sum

// Solution 1 - Recursion TLE 

class Solution {
public:
    bool helper(int ind, int target , vector<int>& nums) {
        if(ind >= nums.size()) 
            return target == 0;

        //exc
        if(helper(ind+1, target, nums))
            return true;

        //inc
        if(nums[ind] <= target)
            return helper(ind+1, target - nums[ind], nums);

        return false;
    }

    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for(int num : nums)
            sum += num;
        if(sum % 2 == 1)
            return false;
        return helper(0, sum/2, nums);
    }
};

// Solution 2 - Memoization 

class Solution {
public:
    bool helper(int ind, int target , vector<int>& nums, vector<vector<int>>& dp) {
        if(ind >= nums.size()) 
            return target == 0;

        if(dp[ind][target] != -1) return dp[ind][target];

        //exc
        if(helper(ind+1, target, nums, dp))
            return dp[ind][target] = true;

        //inc
        if(nums[ind] <= target)
            return dp[ind][target] = helper(ind+1, target - nums[ind], nums, dp);

        return dp[ind][target] = false;
    }

    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for(int num : nums)
            sum += num;
        if(sum % 2 == 1)
            return false;
        vector<vector<int>> dp(nums.size(), vector<int> ((sum/2) + 1, -1));
        return helper(0, sum/2, nums, dp);
    }
};

// Solution 3 - Bottom Up DP

class Solution {
public:

    bool canPartition(vector<int>& nums) {

        int sum = 0;
        for(int num : nums)
            sum += num;
        if(sum % 2 == 1)
            return false;

        int n = nums.size(), target = sum/2;
        vector<vector<int>> dp(n + 1, vector<int> ((sum/2) + 1, false));

        //initial conditions
        dp[0][0] = true;
        for(int i = 1; i<=n ; i++)
            dp[i][0] = true;

        for(int i = 1; i<=n ; i++) {
            for(int j = 1; j<= target; j++) {
                //inc
                if(nums[i-1] <= j)
                    dp[i][j] = dp[i-1][j-nums[i-1]];
                //exc
                dp[i][j] = dp[i][j] || dp[i-1][j];
            }
        }

        return dp[n][target];
    }
};

// Solution 4 - Space Optimized Bottom Up DP

class Solution {
public:

    bool canPartition(vector<int>& nums) {

        int sum = 0;
        for(int num : nums)
            sum += num;
        if(sum % 2 == 1)
            return false;

        int n = nums.size(), target = sum/2;
        vector<bool> prev(target + 1, false);
        vector<bool> curr(target + 1, false);

        prev[0] = true; curr[0] = true;

        for(int i = 1; i<=n ; i++) {
            for(int j = 1; j<= target; j++) {
                //inc
                if(nums[i-1] <= j)
                    curr[j] = prev[j-nums[i-1]];
                //exc
                curr[j] = curr[j] || prev[j];
            }
            prev = curr;
        }

        return curr[target];
    }
};