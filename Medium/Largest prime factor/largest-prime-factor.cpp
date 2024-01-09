//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std;

// } Driver Code Ends
class Solution{
public: 
    long long int prime_fact(int n)
    {
        int maxi=2;
        while(n%2==0)
        {
            n/=2;
        }
        for(int i=3;i*i<=n;i+=2)
        {
            while(n%i==0)
            {
                if(maxi<i)maxi=i;
                n/=i;
            }
        }
        if(n>2 and maxi<n) maxi=n; 
        return maxi;
    }
    long long int largestPrimeFactor(int n){
        // code here
        return prime_fact(n);
    }
};

//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int N;
        cin>>N;
        Solution ob;
        cout << ob.largestPrimeFactor(N) << endl;
    }
    return 0; 
}
// } Driver Code Ends