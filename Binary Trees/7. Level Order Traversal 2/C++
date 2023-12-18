// https://leetcode.com/problems/binary-tree-level-order-traversal-ii

class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> res;
        if(root == nullptr) 
            return res;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while(!q.empty()) {
            vector<int> temp;            
            int s = q.size();
            for(int i = 0; i<s; i++) {
                TreeNode* f = q.front();
                q.pop();
                temp.push_back(f->val);
                if(f->left)
                    q.push(f->left);
                if(f->right)
                    q.push(f->right);
            }
            res.push_back(temp);
        }
        reverse(res.begin(), res.end());

        return res;
    }
};