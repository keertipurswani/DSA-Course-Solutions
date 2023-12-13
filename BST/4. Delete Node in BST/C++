// https://leetcode.com/problems/delete-node-in-a-bst

class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if(root == NULL) return NULL;
        if(root->val > key) {
            root->left = deleteNode(root->left, key);
        } else if(root->val < key) {
            root->right = deleteNode(root->right, key);
        } else {
            if(root->left == NULL) {
                TreeNode* temp = root->right;
                delete(root);
                return temp;
            } else if(root->right == NULL) {
                TreeNode* temp = root->left;
                delete(root);
                return temp;
            } else {
                TreeNode* successor = root->right;
                while(successor && successor->left)
                    successor = successor->left;

                root->val = successor->val;
                root->right = deleteNode(root->right, successor->val);
            }
        }
        return root;
    }
};