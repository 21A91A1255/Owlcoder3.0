//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends


class Solution {
  public:
    string decodedString(string &s) {
        // code here
        stack<char>st;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]!=']'){
                st.push(s[i]);
            }
            else{
                string word;
                while(!st.empty() && st.top()!='[')
                {
                    word+=st.top();
                    st.pop();
                }
                if(st.top()=='[')
                {
                    st.pop();
                }
                reverse(word.begin(),word.end());
                string d;
                while(!st.empty() && isdigit(st.top()))
                {
                    d+=st.top();
                    st.pop();
                }
                reverse(d.begin(),d.end());
                int k=stoi(d);
                string a;
                for(int i=0;i<k;i++){
                    a+=word;
                }
                for(char c:a) st.push(c);

            }
        }
        string ans;
        while(!st.empty())
        {
            ans.push_back(st.top());
            st.pop();
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;

        Solution ob;
        cout << ob.decodedString(s) << "\n";

        cout << "~"
             << "\n";
    }
    return 0;
}
// } Driver Code Ends