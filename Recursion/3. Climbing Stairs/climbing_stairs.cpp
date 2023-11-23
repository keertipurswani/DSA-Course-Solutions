// https://leetcode.com/problems/climbing-stairs
// (TLE solutions - not the most optimised solutions)

class Solution {
public:
    int climbStairs(int n) {
        if(n<=2) return n;
        return climbStairs(n-1) + climbStairs(n-2);
    }
};
