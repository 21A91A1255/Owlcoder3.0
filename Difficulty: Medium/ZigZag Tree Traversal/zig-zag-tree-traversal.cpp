class Solution {
  public:
    vector<int> zigZagTraversal(Node* root) {
        // code here
        if (!root) return {};
        
        queue<Node*> q;
        q.push(root);
        int c = 0;
        vector<int> ans;
        
        while (!q.empty()) {
            int n = q.size();
            vector<int> temp;
            c += 1;
            
            for (int i = 0; i < n; i++) {
                Node* node = q.front();
                q.pop();
                temp.push_back(node->data);
                
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            
            if (c % 2 == 0) {
                for (int i = n - 1; i >= 0; i--)
                    ans.push_back(temp[i]);
            } else {
                for (int i = 0; i < n; i++)
                    ans.push_back(temp[i]);
            }
        }
        
        return ans;
    }
};
