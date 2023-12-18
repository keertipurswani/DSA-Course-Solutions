// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

// Solution 1

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root->val < p->val && root->val < q->val) 
            return lowestCommonAncestor(root->right, p, q);
        else if(root->val > p->val && root->val > q->val) 
            return lowestCommonAncestor(root->left, p, q);
        return root;
    }
};

// Solution 2

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if((root->val <= p->val && root->val >= q->val) || (root->val >= p->val && root->val <= q->val))
            return root;
        else if(root->val < p->val && root->val < q->val) 
            return lowestCommonAncestor(root->right, p, q);
        else return lowestCommonAncestor(root->left, p, q);
    }
};