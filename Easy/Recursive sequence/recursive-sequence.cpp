//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution{
public:
    long long mod=1e9+7;
    long long fun(int n)
    {
        if(n==1) return 1;
        int t=(n*(n+1)/2);
        int r=1;
        int c=0;
        for(int j=t;j>=n;j--)
        {
            c+=1;
            r=(r%mod*j%mod)%mod;
            if(c==n)
            {
                break;
            }
        }
        return r%mod;
    }
    long long sequence(int n){
        // code here
        long long res=0;
        for(int i=0;i<=n;i++)
        {
            res=((res%mod)+fun(i)%mod)%mod;
           // cout<<res<<" ";
        }
        return res%mod;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        
        Solution ob;
        cout<<ob.sequence(N)<<endl;
    }
    return 0;
}
// } Driver Code Ends