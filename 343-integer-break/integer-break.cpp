class Solution {
public:
    vector<vector<int>>ans;
    void fun(int ind,int n,int a[],vector<int>&ds,int s)
    {
        if(ind==s)
        {
            if(n==0)
            {
                ans.push_back(ds);
            }
            return;
        }
        if(a[ind]<=n)
        {
            ds.push_back(a[ind]);
            n=n-a[ind];
            fun(ind,n,a,ds,s);
            n=n+a[ind];
            ds.pop_back();
        }
        fun(ind+1,n,a,ds,s);
    }
    int integerBreak(int n) {
        vector<int>ds;
        int a[n];
        int m=0;
        for(int i=0;i<n;i++)
        {
            a[i]=i+1;
        }
        int s=n;
        fun(0,n,a,ds,s);
        for (auto r : ans) {
            int p = 1;
            for (auto i : r) {
                p *= i;
            }
            if(p>m && r.size()>=2)
            {
                m=p;
            }
        }
        return m;
    }
};