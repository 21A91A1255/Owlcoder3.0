//{ Driver Code Starts

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends


class Solution {
public:
    int prime(int n){
        int c=0;
        while(n%2==0)
        {
            c+=1;
            n=n/2;
        }
        for(int i=3;int(i<sqrt(n)+1);i++)
        {
            while(n%i==0)
            {
                c+=1;
                n=n/i;
            }
        }
        if(n>2)
        {
            c+=1;
        }
        return c;
    }
	int sumOfPowers(int a, int b){
	    // Code here
	    int ans=0;
	    for(int i=a;i<=b;i++){
	        int p=prime(i);
	        ans+=p;
	    }
	    return ans;
	    
	}
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int a, b;
		cin >>  a >> b;
		Solution obj;
		int ans = obj.sumOfPowers(a, b);
		cout << ans <<"\n";
	}
	return 0;
}
// } Driver Code Ends