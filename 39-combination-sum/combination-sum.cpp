class Solution {
public:vector<vector<int>> ans;
    
    void combination(int ind,vector<int>&candidates,int n,int k,vector<int>&ds)
    {
        if(ind==n)
        {
            if(k==0)
            {
                vector<int>v;
                for(auto it:ds)
                {
                    v.push_back(it);
                }
                ans.push_back(v);
            }
            return ;
        }
        if(candidates[ind]<=k)
        {
            ds.push_back(candidates[ind]);
            k=k-candidates[ind];
            combination(ind,candidates,n,k,ds);
            k=k+candidates[ind];
            ds.pop_back();
        }
        combination(ind+1,candidates,n,k,ds);
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int k) {
        vector<int>ds;
        int n=candidates.size();
        combination(0,candidates,n,k,ds);
        return ans;
    }
};