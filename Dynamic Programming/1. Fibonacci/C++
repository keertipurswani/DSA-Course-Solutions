// https://leetcode.com/problems/fibonacci-number

// Solution 1 - Recursion - TLE
// Time Complexity - O(2^n)
// Space Complexity - O(n) (Recursive Stack Space)

class Solution {
public:
    int fib(int n) {
        if(n <= 1) return n;
        return fib(n-1) + fib(n-2);
    }
};

// Solution 2 - Memoization - Top Down
// Time Complexity - O(n)
// Space Complexity - O(n) (n for recursive stack and n for dp array - O(n) + O(n))

class Solution {
public:
    int helper(int n, vector<int>& dp) {
        if(dp[n] != -1)
            return dp[n];

        if(n <= 1) return dp[n] = n;

        return dp[n] = helper(n-1, dp) + helper(n-2, dp);
    }

    int fib(int n) {
        vector<int> dp(n+1, -1);
        helper(n, dp);
        return dp[n];
    }
};

// Solution 3 - Bottom Up DP - Tabulation
// Time Complexity - O(n)
// Space Complexity - O(n) (n for dp array - no recursive stack space)

class Solution {
public:
    int fib(int n) {
        if(n<=1) return n;

        vector<int> dp(n+1);
        dp[0] = 0; dp[1] = 1;

        for(int i = 2; i<=n; i++)
            dp[i] = dp[i-1] + dp[i-2];

        return dp[n];
    }
};

//Solution 4 - Space optimized bottom up DP
// Time Complexity - O(n)
// Space Complexity - O(1)

class Solution {
public:
    int fib(int n) {
        if(n<=1) return n;
        int seclast = 0, last = 1;
        int ans;

        for(int i = 2; i<=n; i++) {
            ans = seclast + last;
            seclast = last;
            last = ans;
        }

        return ans;
    }
};