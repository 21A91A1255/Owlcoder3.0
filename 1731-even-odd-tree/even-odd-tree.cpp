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
    int c=-1,m=0,m1=0; 
    void fun(TreeNode* root)
    {
        if(root==NULL) return;
        queue<TreeNode*>q;
        q.push(root);
        while(!q.empty())
        {
            int r=q.size();
            c+=1;
            vector<int>k;
            for(int i=0;i<r;i++)
            {
                TreeNode* node=q.front();
                k.push_back(node->val);
                q.pop();
                if(node->left!=NULL)
                {
                    q.push(node->left);
                }
                if(node->right!=NULL)
                {
                    q.push(node->right);
                }
            }
            vector<int>p=k;
            sort(k.begin(),k.end());
            vector<int>d=k;
            reverse(k.begin(),k.end());
            vector<int>s=k;
            int x=0,v=0,h=0,x1=0;
            for(int i=0;i<p.size();i++)
            {
                if(p[i]%2==0)
                {
                    v+=1;
                }
                if(p[i]%2!=0)
                {
                    h+=1;
                }
            }
            for(int i=0;i<p.size()-1;i++)
            {
                if(p[i]>p[i+1])
                {
                    x+=1;
                }
            }
            for(int i=0;i<p.size()-1;i++)
            {
                if(p[i]<p[i+1])
                {
                    x1+=1;
                }
            }
            if(x==(p.size()-1) and v==(p.size()))
            {
                if(c%2!=0 and p==s)
                {
                    m+=1;
                }
            }
            if(x1==(p.size()-1) and h==(p.size()))
            {
                if(c%2==0 and p==d)
                {
                    m1+=1;
                }
            }
        }
    }
    bool isEvenOddTree(TreeNode* root) {
        fun(root);
        if((m+m1)==c+1)
        {
            return true;
        }
        return false;
    }
};