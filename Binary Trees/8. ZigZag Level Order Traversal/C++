// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res;
        
        if(root == nullptr) return res;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while(!q.empty())
        {
            vector<int> temp;
            int s = q.size();
            
            for(int i = 0; i<s; i++) {
                TreeNode* front = q.front();
                q.pop();
                
                if(front->left) q.push(front->left);
                if(front->right) q.push(front->right);
                
                temp.push_back(front->val);
            }
            if(res.size() % 2 == 1) reverse(temp.begin(), temp.end());
            res.push_back(temp);
        }
        return res;
    }
};