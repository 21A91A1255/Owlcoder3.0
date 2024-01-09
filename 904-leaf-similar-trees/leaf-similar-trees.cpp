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
    void list1(TreeNode* root1,vector<int>&v)
    {
        if (root1==NULL) return ;
        list1(root1->left,v);
        if(root1->left==NULL and root1->right==NULL)
        {
            v.push_back(root1->val);
        }
        list1(root1->right,v);
    }
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int>a,b;
        list1(root1,a);
        list1(root2,b);
        if(a==b)
        {
            return true;
        }
        return false;
    }
};