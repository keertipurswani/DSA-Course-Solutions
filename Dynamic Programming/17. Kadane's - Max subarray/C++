// https://leetcode.com/problems/maximum-subarray

// Brute force 
// Time Complexity -  O(N^3)
// Space Complexity - O(1)

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int res = nums[0]; // or INT_MIN
        for(int i = 0; i<n; i++) {
            for(int j = 0; j<=i; j++) {
                int sum = 0;
                for(int k = j; k<=i; k++)
                    sum += nums[k];
                if(sum > res) res = sum;
            }
        }
        return res;
    }
};

// Kadane's Algo
// Time Complexity -  O(N)
// Space Complexity - O(1)

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int res = nums[0];
        int sum = 0;
        for(int i = 0; i<n; i++) {
          sum += nums[i];
          if(sum > res) res = sum;
          if(sum < 0) sum = 0;
        }
        return res;
    }
};