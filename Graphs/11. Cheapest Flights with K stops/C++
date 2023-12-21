// https://leetcode.com/problems/cheapest-flights-within-k-stops
// Bellman Ford

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<int> cost(n, 100000000);
        cost[src] = 0;

        for(int i = 0; i<=k; i++) {
            vector<int> temp = cost;
            for(auto flight : flights) {
                int flight_src = flight[0];
                int flight_dest = flight[1];
                int flight_cost = flight[2];
                temp[flight_dest] = min(temp[flight_dest], cost[flight_src] + flight_cost);
            }
            cost = temp;
        }
        return cost[dst] == 100000000 ? -1 : cost[dst];
    }
};