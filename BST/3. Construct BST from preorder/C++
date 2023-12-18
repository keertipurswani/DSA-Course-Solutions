// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal

class Solution {
public:
    TreeNode* helper(vector<int> preorder, int st, int end) {
        if(st > end) return NULL;

        TreeNode* root = new TreeNode(preorder[st]);

        int idx = (upper_bound(preorder.begin()+st, preorder.end(), preorder[st]) - preorder.begin());
        
        root->left = helper(preorder, st+1, idx-1);
        root->right = helper(preorder, idx, end);
    
        return root;
    }

    TreeNode* bstFromPreorder(vector<int>& preorder) {
        return helper(preorder, 0, preorder.size() - 1);
    }
};