// https://leetcode.com/problems/binary-tree-preorder-traversal

//Time Complexity - O(N)
//Space Complexity - O(N)

// Solution 1 - Add checks before calls

class Solution {
public:
    void helper(TreeNode* root, vector<int>& res) {
        res.push_back(root->val);
        if(root->left) helper(root->left, res);
        if(root->right) helper(root->right, res);
    }

    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        if(root)
            helper(root, res);
        return res;
    }
};

// Solution 2 - Add check in function

class Solution {
public:
    void helper(TreeNode* root, vector<int>& res) {
        if(root == NULL) return;
        res.push_back(root->val);
        helper(root->left, res);
        helper(root->right, res);
    }

    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        helper(root, res);
        return res;
    }
};

// Iterative Solution

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        if(!root) return res;

        stack<TreeNode*> st;
        st.push(root);

        while(!st.empty()) {
            TreeNode* topNode = st.top();
            res.push_back(topNode->val);
            st.pop();

            if (topNode->right != NULL)
                st.push(topNode->right);
            if (topNode -> left != NULL)
                st.push(topNode -> left);
            
        }

        return res;
    }
};