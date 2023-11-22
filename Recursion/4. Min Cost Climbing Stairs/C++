// https://leetcode.com/problems/min-cost-climbing-stairs
// (TLE solutions - not the most optimised solutions)

//Solution 1

class Solution {
public:

    int helper(int ind, vector<int>& cost) {
        if(ind <= 1) return cost[ind];
        return ((ind == cost.size() ? 0 : cost[ind]) + min(helper(ind-1, cost), helper(ind-2, cost))); 
    }

    int minCostClimbingStairs(vector<int>& cost) {
        return helper(cost.size() , cost);
    }
};

//Solution 2

class Solution {
public:

    int helper(int ind, vector<int>& cost) {
        if(ind <= 1) return cost[ind];
        return (cost[ind] + min(helper(ind-1, cost), helper(ind-2, cost))); 
    }

    int minCostClimbingStairs(vector<int>& cost) {
        return min(helper(cost.size() - 1 , cost), helper(cost.size() - 2, cost));
    }
};

//Solution 3 - From 0 to n

class Solution {
public:
    int helper(vector<int>& cost, int ind) {
        if(ind >= cost.size()) return 0;
        return cost[ind] + min(helper(cost, ind+1), helper(cost, ind+2));
    }

    int minCostClimbingStairs(vector<int>& cost) {
        return min(helper(cost, 0), helper(cost, 1));
    }
};
