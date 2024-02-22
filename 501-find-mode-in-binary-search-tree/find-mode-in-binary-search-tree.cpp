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
    void preorder(TreeNode* root,vector<int>&v)
    {
        if(root==NULL) return;
        v.push_back(root->val);
        preorder(root->left,v);
        preorder(root->right,v);
    }
    vector<int> findMode(TreeNode* root) {
        vector<int>v;
        preorder(root,v);
        map<int,int>mpp;
        int m=0;
        for(int i=0;i<v.size();i++)
        {
            mpp[v[i]]++;
            if(mpp[v[i]]>m)
            {
                m=mpp[v[i]];
            }
        }
        vector<int>r;
        for(auto i:mpp)
        {
            if(i.second==m)
            {
                r.push_back(i.first);
            }
        }
        return r;

    }
};