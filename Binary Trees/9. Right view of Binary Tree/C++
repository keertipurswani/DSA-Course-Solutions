// https://leetcode.com/problems/binary-tree-right-side-view

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if(root == NULL) return res;
        queue<TreeNode*> q;
        q.push(root);

        while(!q.empty()) {
            int s = q.size();
            int last;
            for(int i = 0; i<s; i++) {
                TreeNode* front = q.front();
                if(front->left) q.push(front->left);
                if(front->right) q.push(front->right);
                last = front->val;
                q.pop();
            }
            res.push_back(last);
        }
        return res;
    }
};