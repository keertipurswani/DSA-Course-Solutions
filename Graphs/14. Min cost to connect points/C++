// https://leetcode.com/problems/min-cost-to-connect-all-points

// Solution 1 - Prim's Algo

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

        vector<vector<pair<int, int>>> graph(points.size(), vector<pair<int, int>>());

        for(int i=0; i< points.size(); i++){
            vector<int> curr = points[i];
            for(int j=0; j< points.size() ; j++){
                if(j==i) continue;
                graph[i].push_back({abs(curr[0]-points[j][0])+abs(curr[1]-points[j][1]), j});
            }
        }

        vector<int> vis(points.size(), 0);
        pq.push({0, 0});
        int res=0;

        while(!pq.empty()){
            int curr = pq.top().second;
            int cost = pq.top().first;
            pq.pop();

            if(vis[curr]) continue;
            vis[curr] = 1;
            res += cost;

            for(auto neighbor : graph[curr]){
                if(!vis[neighbor.second])
                    pq.push(neighbor);
            }
        }

        return res;
    }
};

// Solution 2 - Kruskal's Algo

class DSU {
    vector<int> par;
    public:
        DSU(int n) {
            par = vector<int>(n, -1);
        }

        int findParent(int x) {
            if(par[x] == -1) return x;
            return findParent(par[x]);
        }

        bool unit(int x, int y) {
            int parX = findParent(x), parY = findParent(y);
            if(parX == parY) return false;

            par[parY] = parX;
            return true;
        }
};

class Solution {
public:
    int dist(vector<int>& a, vector<int>& b){
        return abs(a[0]-b[0]) + abs(a[1]-b[1]);
    }

    int minCostConnectPoints(vector<vector<int>>& points) {
        vector<vector<int>> edges;
        int n = points.size();
        int res = 0;
        DSU dsuObj(n);

        for(int i=0 ; i<n ; i++){
            for(int j=i+1 ; j<n ; j++){
                edges.push_back({i,j, dist(points[i],points[j])});
            }
        }

        sort(edges.begin(),edges.end(),[](const vector<int>& v1, const vector<int>& v2) -> bool{
            return v1[2]<v2[2];
        });

        for(int i=0;i<edges.size();i++){
            int u = edges[i][0], v = edges[i][1], w = edges[i][2];
            if(dsuObj.unit(u,v)){
                res += w;
            }
        }

        return res;
    }
};