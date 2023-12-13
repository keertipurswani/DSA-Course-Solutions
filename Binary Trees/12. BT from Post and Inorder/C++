// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

class Solution {
public:
    TreeNode* helper(vector<int>& inorder, int in_st, int in_end, vector<int>& postorder, int post_st, int post_end, unordered_map<int, int>& mp) {
        if(in_st > in_end || post_st > post_end) return NULL;
        TreeNode* root = new TreeNode(postorder[post_end]);
        int in_root_idx = mp[postorder[post_end]];
        int num_in_left = in_root_idx - in_st;
        root->left = helper(inorder, in_st, in_root_idx-1, postorder, post_st, post_st+num_in_left-1, mp);
        root->right = helper(inorder, in_root_idx + 1, in_end, postorder, post_st+num_in_left, post_end-1, mp);
        return root;
    }

    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int s = inorder.size();
        unordered_map<int, int> mp;
        for(int i = 0; i<s; i++)
            mp[inorder[i]] = i;
        return helper(inorder, 0, s-1, postorder, 0, s-1, mp);
    }
};