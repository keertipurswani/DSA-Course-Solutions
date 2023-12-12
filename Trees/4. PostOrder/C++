// https://leetcode.com/problems/binary-tree-postorder-traversal

class Solution {
public:
    void helper(TreeNode* root, vector<int>& res) {
        if(root == NULL) return;
        helper(root->left, res);
        helper(root->right, res);
        res.push_back(root->val);
    }

    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        helper(root, res);
        return res;
    }
};

// Iterative Solution 

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        if(root == NULL) return res;

        stack<TreeNode*> st;

        while (root != NULL || !st.empty()) {
            if (root != NULL) {
                st.push(root);
                root = root -> left;
            } else {
                TreeNode* temp = st.top()->right;
                if (temp == NULL) {
                    temp = st.top();
                    st.pop();
                    res.push_back(temp->val);
                    while (!st.empty() && temp == st.top()->right) {
                        temp = st.top();
                        st.pop();
                        res.push_back(temp->val);
                    }
                } else root = temp;
            }
        }
        return res;
    }
};