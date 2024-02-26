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
    void preorder(TreeNode* p,vector<int>&l)
    {
        if(p==NULL) 
        {
            l.push_back('a');
            return;
        }
        l.push_back(p->val);
        preorder(p->left,l);
        preorder(p->right,l);
    }
    bool isSameTree(TreeNode* p, TreeNode* q) {
        vector<int>l;
        vector<int>m;
        preorder(p,l);
        preorder(q,m);
        if(l==m) return true;
        return false;
    }
};