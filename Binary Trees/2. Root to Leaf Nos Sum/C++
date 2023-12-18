// https://leetcode.com/problems/sum-root-to-leaf-numbers

class Solution {
public:
    int helper(TreeNode* root, int sum = 0) {
        if(root == NULL) return 0;
        if(root->left || root->right)
            return helper(root->left, sum*10 + root->val) + helper(root->right, sum*10 + root->val);
        else return sum*10 + root->val;
    }

    int sumNumbers(TreeNode* root) {
       return helper(root, 0);
    }
};

// Add default parameter to the same function

int sumNumbers(TreeNode* root, int sum = 0) {
    if(root == NULL) return 0;
    if(root->left || root->right)
        return sumNumbers(root->left, sum*10 + root->val) + sumNumbers(root->right, sum*10 + root->val);
    else return sum*10 + root->val;
}