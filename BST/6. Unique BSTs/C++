// https://leetcode.com/problems/unique-binary-search-trees-ii

class Solution {
public:
    vector<TreeNode*> helper(int start, int end) {
        vector<TreeNode*> res;

        if(start > end) {
            res.push_back(NULL);
            return res;
        }

        if(start == end) {
            res.push_back(new TreeNode(start));
            return res;
        }

        vector<TreeNode*> left, right;
        TreeNode* root;

        for(int i = start; i <=end; i++) {
            left = helper(start, i-1);
            right = helper(i+1, end);
            for(auto lnode : left) {
                for(auto rnode : right) {
                    root = new TreeNode(i);
                    root->left = lnode;
                    root->right = rnode;
                    res.push_back(root);
                }
            }
        }

        return res;
    }

    vector<TreeNode*> generateTrees(int n) {
        vector<TreeNode*> res;
        return helper(1, n);
    }
};