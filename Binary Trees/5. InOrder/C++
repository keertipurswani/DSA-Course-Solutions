// https://leetcode.com/problems/binary-tree-inorder-traversal

class Solution {
public:
    void helper(TreeNode* root, vector<int>& res) {
        if(root == NULL) return;
        helper(root->left, res);
        res.push_back(root->val);
        helper(root->right, res);
    }

    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        helper(root, res);
        return res;
    }
};

// Iterative Solution 

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        if(!root) return res;

        stack<TreeNode*> st;
        while(true) {
            if (root) {
                st.push(root);
                root = root->left;
            } else {
                if (st.empty()) break;
                root = st.top();
                res.push_back(root->val);
                st.pop();
                root = root->right;
            }
        }

        return res;
    }
};