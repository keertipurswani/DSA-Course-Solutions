// https://leetcode.com/problems/01-mat

// Solution 1 - BFS

class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int n = mat.size(), m = mat[0].size();
        queue<pair<int,int>> q;

        for(int i = 0; i<n; i++) {
            for(int j = 0; j<m; j++) {
                if(mat[i][j] == 0) {
                    q.push({i, j});
                } else {
                    mat[i][j] = m+n;
                }
            }
        }

        vector<vector<int>> dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while(!q.empty()) {
            int i = q.front().first;
            int j = q.front().second;
            q.pop();
            for(int k = 0; k<4; k++) {
                int newi = i + dir[k][0];
                int newj = j + dir[k][1];
                if(newi >= 0 && newi < n && newj >= 0 && newj < m && mat[newi][newj] > mat[i][j] + 1) {
                    mat[newi][newj] = 1+ mat[i][j];
                    q.push({newi, newj});
                }
            }
        }

        return mat;
    }
};

// Solution 2 - DP

class Solution {
public:
    vector<vector<int>> updatemat(vector<vector<int>>& mat) {
        int n = mat.size(), m = mat[0].size();
        for(int i = 0; i<n; i++) {
            for(int j = 0; j<m; j++) {
                if(mat[i][j] != 0) {
                    mat[i][j] = m+n;
                }
            }
        }

        for(int i = 0; i<n; i++) {
            for(int j = 0; j<m; j++) {
                if(mat[i][j] != 0) {
                    if(i != 0) mat[i][j] = min(mat[i][j], mat[i-1][j] + 1);
                    if(j != 0) mat[i][j] = min(mat[i][j], mat[i][j-1] + 1);
                }
            }
        }
        
        for(int i = n-1; i>=0; i--) {
            for(int j = m-1; j>=0 ; j--) {
                if(mat[i][j] != 0) {
                    if(i != n-1) mat[i][j] = min(mat[i][j], mat[i+1][j] + 1);
                    if(j != m-1) mat[i][j] = min(mat[i][j], mat[i][j+1] + 1);
                }
            }
        }
        
        return mat;
    }
};