//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

class Solution{
    public:
    vector<string>ress;
    void rec(vector<vector<int>>&v,int i,int j,int n,string s){
        if(i<0 || j<0 || i>=n || j>=n)return;
        if(i==n-1 && j==n-1 && v[n-1][n-1]==1){
            ress.push_back(s);
            return;
        }
        if(v[i][j]==0 || v[i][j]==2)return;
        int t=v[i][j];
        v[i][j]=2;
        rec(v,i-1,j,n,s+'U');
        rec(v,i,j-1,n,s+'L');
        rec(v,i+1,j,n,s+'D');
        rec(v,i,j+1,n,s+'R');
        v[i][j]=t;
    }
    vector<string> findPath(vector<vector<int>> &m, int n) {
        // Your code goes here
        string s;
        rec(m,0,0,n,s);
        return ress;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<int>> m(n, vector<int> (n,0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> m[i][j];
            }
        }
        Solution obj;
        vector<string> result = obj.findPath(m, n);
        sort(result.begin(), result.end());
        if (result.size() == 0)
            cout << -1;
        else
            for (int i = 0; i < result.size(); i++) cout << result[i] << " ";
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends