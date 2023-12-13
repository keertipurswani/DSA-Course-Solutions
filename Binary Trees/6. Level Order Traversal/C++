// https://leetcode.com/problems/binary-tree-level-order-traversal

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
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
        
        return res;
    }
};