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
    int lst=0;
    void fun(TreeNode* root)
    {
        if(root==NULL) return;
        queue<TreeNode*>q;
        q.push(root);
        while(!q.empty())
        {
            int r=q.size();
            vector<int>k;
            for(int i=0;i<r;i++)
            {
                TreeNode* node=q.front();
                q.pop();
                if(i==0)
                {
                    lst=node->val;
                }
                if(node->left!=NULL)
                {
                    q.push(node->left);
                }
                if(node->right!=NULL)
                {
                    q.push(node->right);
                }
            }
        }
    } 
    int findBottomLeftValue(TreeNode* root) {
        fun(root);
        return lst;
    }
};