//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    string removeKdigits(string s, int k) {
        stack<char>st;
        st.push(s[0]);
        int i=1,n=s.size();
        while(i<n){
            while(!st.empty() && (int)s[i]<(int)st.top() && k>0)
            {
                st.pop();
                k--;
            }
            if(st.empty() && s[i]=='0')
            {
                i++;
                continue;
            }
            else{
                st.push(s[i]);
                i++;
            }
        }
        while(!st.empty() && k>0)
        {
            st.pop();
            k--;
        }
        string res=" ";
        while(!st.empty())
        {
            res+=st.top();
            st.pop();
        }
        reverse(res.begin(),res.end());
        if(res==" ")
        {
            return "0";
        }
        return res;
    }
    
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        string S;
        cin >> S;
        int K;
        cin >> K;
        Solution obj;
        cout << obj.removeKdigits(S, K) << endl;
    }
    return 0;
}

// } Driver Code Ends