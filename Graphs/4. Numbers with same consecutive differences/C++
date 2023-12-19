// https://leetcode.com/problems/numbers-with-same-consecutive-differences

// Solution 1 - DFS

class Solution {
public:
    void dfs(int num, int n, int k, vector<int>& res) {
        if(n == 0)  {
            res.push_back(num);
            return;
        }
        int x = num % 10;
        if(x+k <= 9) dfs(num * 10 + x+k, n-1, k, res);
        if(k != 0 && x-k >= 0) dfs(num * 10 + x-k, n-1, k, res);
    }

    vector<int> numsSameConsecDiff(int n, int k) {
        vector<int> res;
        for(int i = 1; i<=9; i++)
            dfs(i, n-1, k, res);
        return res;
    }   
};


// Solution 2 - BFS

class Solution {
public:
    vector<int> numsSameConsecDiff(int n, int k) {
        vector<int> res;
        queue<int> q;
        for(int i = 1; i<= 9; i++)
            q.push(i);
        int len = 1; //level
        while(!q.empty() && len < n) {          
            len++;
            int s = q.size();
            for(int i = 0; i<s; i++) {
                int f = q.front();
                q.pop();
                int x = f%10;
                if(x+k <= 9)
                    q.push(f*10 + x+k);
                if(k != 0 && x-k >= 0)
                    q.push(f*10 + x-k);
            }
        }
        while(!q.empty()) {
            res.push_back(q.front());
            q.pop();
        }
        return res;
    }
};