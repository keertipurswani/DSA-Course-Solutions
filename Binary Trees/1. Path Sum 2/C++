// https://leetcode.com/problems/path-sum-ii

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

    void helper(TreeNode* root, int sum, vector<vector<int>>& res, vector<int>& curr) {
        if(root == nullptr) return;
        curr.push_back(root->val);

        if(root->left == nullptr && root->right == nullptr && sum == root->val) {
            res.push_back(curr); 
        }

        helper(root->left, sum-root->val, res, curr);
        helper(root->right, sum-root->val, res, curr);
        
        curr.pop_back();
    }

    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> res;
        vector<int> curr;
        helper(root, sum, res, curr);
        return res;
    }
};