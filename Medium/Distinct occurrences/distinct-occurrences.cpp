//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;
 

// } Driver Code Ends
/*You are required to complete this method*/

class Solution
{
    public:
    int dp[1001][1001];
    int mod=1000000007;
    int fun(string s,int i,int j,string t)
    {
        if(j==t.size())
        {
            return 1;
        }
        if(i==s.size()) return 0;
        if(dp[i][j]!=-1) return dp[i][j];
        
        int a=0,b=0;
        if(s[i]==t[j])
        {
            a=fun(s,i+1,j+1,t);
        }
        b=fun(s,i+1,j,t);
        return dp[i][j]=((a%mod)+(b%mod)%mod);
    }
    int subsequenceCount(string s, string t)
    {
      memset(dp,-1,sizeof(dp));
      int d=fun(s,0,0,t);
      return d%mod;
    }
};
 


//{ Driver Code Starts. 

//  Driver code to check above method
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		string s;
		string tt;
		cin>>s;
		cin>>tt;
		
		Solution ob;
		cout<<ob.subsequenceCount(s,tt)<<endl;
		
		
	}
  
}
// } Driver Code Ends