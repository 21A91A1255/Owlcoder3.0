//{ Driver Code Starts
//Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++

// s : given string to search
// dictionary : vector of available strings

class Solution
{
public:
    int fun(string s, int cur, int cmpind, int n, vector<string>& dic, int m)
    {
        if(cur==m) return 1;
        int si=dic[cmpind].size();
        if((m-cur)<si) return 0;
        if(s.substr(cur, si)!=dic[cmpind]) return 0;
        cur+=si;
        for(int i=0;i<n;i++)
        {
            if(fun(s, cur, i, n, dic, m)) return 1;
        }
        return 0;
    }
    int wordBreak(int n, string s, vector<string> &d) {
        for(int i=0;i<d.size();i++)
        {
            if(fun(s, 0, i, n, d, s.size())) return 1;
        }
        return 0;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<string> dictionary;
        for(int i=0;i<n;i++){
            string S;
            cin>>S;
            dictionary.push_back(S);
        }
        string s;
        cin>>s;
        Solution ob;
        cout<<ob.wordBreak(n, s, dictionary)<<"\n";
    }
}

// } Driver Code Ends