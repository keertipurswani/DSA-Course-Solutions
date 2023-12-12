// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector<vector<int>> res;
        if(root == NULL) return res;

        //hdist - vdist, val
        map<int, vector<pair<int,int>>> mp;
        //node-vdist, hdist
        queue<pair<TreeNode*, pair<int, int>>> q;  

        q.push({root, {0,0}});

        while(!q.empty()) {
            int s = q.size();
            for(int i = 0; i<s; i++) {
                TreeNode* front = q.front().first;
                int vdist = q.front().second.first;
                int hdist = q.front().second.second;
                mp[hdist].push_back({vdist , front->val});
                q.pop();
                if(front->left)
                    q.push({front->left, {vdist+1, hdist-1}});
                if(front->right)
                    q.push({front->right, {vdist+1, hdist+1}});
            }
        }

        for(auto itr : mp) {
            vector<pair<int,int>> temp = itr.second;
            sort(temp.begin(), temp.end());
            vector<int> curr;
            for(auto itr2: temp)
                curr.push_back(itr2.second);
            res.push_back(curr);
        }

        return res;
    }
};