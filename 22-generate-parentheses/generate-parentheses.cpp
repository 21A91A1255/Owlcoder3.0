class Solution {
public:
    void fun(int oc,int cc,int n,string s,vector<string> &ans)
    {
        if(oc==n && cc==n)
        {
            ans.push_back(s);
            return ;
        }
        if(oc<=n)
        {
            s.push_back('(');
            fun(oc+1,cc,n,s,ans);
            s.pop_back();
        }
        if(cc<oc)
        {
            s.push_back(')');
            fun(oc,cc+1,n,s,ans);
            s.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string>ans;
        string s;
        fun(0,0,n,s,ans);
        return ans;
    }
};