// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

class Solution {
public:
    TreeNode* helper(vector<int>& preorder, int pre_st, int pre_end, vector<int>& inorder, int in_st, int in_end) {
        if(pre_st > pre_end || in_st > in_end) return NULL;

        TreeNode* root = new TreeNode(preorder[pre_st]);
        int in_root_idx = find(inorder.begin() + in_st, inorder.end() + in_end+1, preorder[pre_st]) - inorder.begin();
        int num_in_left = in_root_idx - in_st;
        root->left = helper(preorder, pre_st+1, pre_st + num_in_left, inorder, in_st, in_root_idx - 1);
        root->right = helper(preorder, pre_st + num_in_left + 1, pre_end, inorder, in_root_idx+1, in_end);
        return root;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int s = preorder.size();
        // don't need to check s == 0 because of contraints
        return helper(preorder, 0, s-1, inorder, 0, s-1);
    }
};

// Solution 2

class Solution {
public:
    TreeNode* helper(vector<int>& preorder, int pre_st, int pre_end, vector<int>& inorder, int in_st, int in_end, unordered_map<int, int>& mp) {
        if(pre_st > pre_end || in_st > in_end) return NULL;

        TreeNode* root = new TreeNode(preorder[pre_st]);
        int in_root_idx = mp[preorder[pre_st]];
        int num_in_left = in_root_idx - in_st;
        root->left = helper(preorder, pre_st+1, pre_st + num_in_left, inorder, in_st, in_root_idx - 1, mp);
        root->right = helper(preorder, pre_st + num_in_left + 1, pre_end, inorder, in_root_idx+1, in_end, mp);
        return root;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int s = preorder.size();
        unordered_map<int, int> mp;

        for(int i = 0; i<s; i++)
            mp[inorder[i]] = i;

        // don't need to check s == 0 because of contraints
        return helper(preorder, 0, s-1, inorder, 0, s-1, mp);
    }
};

// Solution 3 - Adding checks before calling the function

class Solution {
public:
    TreeNode* helper(vector<int>& preorder, int pre_st, int pre_end, vector<int>& inorder, int in_st, int in_end) {
        TreeNode* root = new TreeNode(preorder[pre_st]);
        int in_root_idx = find(inorder.begin() + in_st, inorder.end() + in_end+1, preorder[pre_st]) - inorder.begin();
        int num_in_left = in_root_idx - in_st;

        if(in_st != in_end) {
            if(num_in_left > 0)
                root->left = helper(preorder, pre_st+1, pre_st + num_in_left, inorder, in_st, in_root_idx - 1);
            if(in_root_idx < in_end) 
                root->right = helper(preorder, pre_st + num_in_left + 1, pre_end, inorder, in_root_idx+1, in_end);
        }
        return root;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int s = preorder.size();
        // don't need to check s == 0 because of contraints
        return helper(preorder, 0, s-1, inorder, 0, s-1);
    }
};