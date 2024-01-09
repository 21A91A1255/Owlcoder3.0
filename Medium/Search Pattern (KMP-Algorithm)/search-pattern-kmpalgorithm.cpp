//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution
{
    public:
        vector <int> search(string pat, string txt)
        {
            //code here
            // int i=0,j=0;
            vector<int>v;
            
            for(int i=0;i<txt.size()-pat.size()+1;i++)
            {
                if(txt[i]==pat[0])
                {
                string s1=txt.substr(i,pat.size());
                if(s1==pat) v.push_back(i+1);
                }
            }
            return v;
            
           
            
        }
     
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string S, pat;
        cin >> S >> pat;
        Solution ob;
        vector <int> res = ob.search(pat, S);
        if (res.size()==0)
            cout<<-1<<endl;
        else {
            for (int i : res) cout << i << " ";
            cout << endl;
        }
    }
    return 0;
}

// Contributed By: Pranay Bansal

// } Driver Code Ends