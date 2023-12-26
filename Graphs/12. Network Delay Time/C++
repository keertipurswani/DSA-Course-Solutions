// https://leetcode.com/problems/network-delay-time

// Solution 1 - Bellman Ford 
// Time Complexity - O(V.E) = O(V^3)

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<int> dist(n+1, INT_MAX);
        dist[k] = 0;
        
         for(int i=1; i<n; i++){
            for(auto edge: times){
                int u = edge[0];
                int v = edge[1];
                int w = edge[2];
                
                if(dist[u]!=INT_MAX and dist[u] + w < dist[v])
                    dist[v] = dist[u] + w;
            }
         }
        int res = -1;
        for(int i=1; i<=n; i++){
            res = max(res, dist[i]);
        }
        return res == INT_MAX ? -1 : res;
    }
};


// Solution 2 - Dijkstra Algo - Priority Queue
// Time Complexity - O(V + ElogV)

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int,int>>> graph(n+1, vector<pair<int,int>>());

        for(auto time : times)
            graph[time[0]].push_back({time[1], time[2]});

        vector<int> dist(n+1, INT_MAX);
        dist[k] = 0;
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

        pq.push({0, k});

        while(!pq.empty()) {
            int node = pq.top().second;
            int nodedist = pq.top().first;
            pq.pop();

            for(auto neighbor : graph[node]) {
                int adjnode = neighbor.first;
                int adjnodedist = neighbor.second;

                if(dist[adjnode] > nodedist + adjnodedist) {
                    dist[adjnode] = nodedist + adjnodedist;
                    pq.push({dist[adjnode], adjnode});
                }
            }
        }

        int res = -1;
        for(int i = 1; i<=n; i++) {
            res = max(res, dist[i]);
        }
        if(res == INT_MAX) return -1; // return res == INT_MAX ? -1 : res;
        return res;
    }
};

// Solution 3 - Floyd Warshall

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<int>> dist(n, vector<int> (n, INT_MAX));

        for(auto time : times)
            dist[time[0] - 1][time[1] - 1] = time[2];
        
        for(int i = 0; i<n; i++)
            dist[i][i] = 0;

        for(int k = 0; k<n; k++) {
            for(int i = 0; i<n; i++) {
                for(int j = 0; j<n; j++) {
                    if(dist[i][k] != INT_MAX && dist[k][j] != INT_MAX)
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }

        int res = INT_MIN;
        for (int i = 0; i < n; ++i) {
            if (dist[k - 1][i] == INT_MAX) {
                return -1;
            }
            res = max(res, dist[k - 1][i]);
        }
        return res;

    }
};