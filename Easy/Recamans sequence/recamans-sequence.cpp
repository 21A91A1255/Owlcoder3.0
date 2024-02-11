//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    vector<int> recamanSequence(int n){
        // code here
        vector<int>v={0};
        unordered_map<int, int> mp;
        for(int i=1;i<n;i++)
        {
            if(mp[v[i-1]-i]==0 && (v[i-1]-i)>0){
                mp[v[i-1]-i]++;
                v.push_back(v[i-1]-i);
            }
            else{
                v.push_back(v[i-1]+i);
                mp[v[i-1]+i]++;
            }
        }
        return v;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        
        Solution ob;
        vector<int> ans = ob.recamanSequence(n);
        for(int i = 0;i < n;i++)
            cout<<ans[i]<<" ";
        cout<<"\n";
    }
    return 0;
}
// } Driver Code Ends