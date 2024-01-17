//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution
{
    public:
    //Function to check if brackets are balanced or not.
    bool ispar(string x)
    {
        stack<char>s;
        for(int i=0;i<x.size();i++)
        {
            if(x[i]=='[' || x[i]=='{' || x[i]=='(')
            {
                s.push(x[i]);
                //cout<<s.top()<<" ";
            }
            else{
                if(!s.empty())
                {
                    //cout<<s.top()<<"hi ";
                    if(x[i]==']' && s.top()=='[')
                    {
                        s.pop();
                    }
                    else if(x[i]=='}' && s.top()=='{')
                    {
                        s.pop();
                    }
                    else if(x[i]==')' && s.top()=='(')
                    {
                        s.pop();
                    }
                    else
                    {
                         return false;
                    }
                }
                else
                {
                    return false;
                }
            }
        }
        return s.empty();
    }

};

//{ Driver Code Starts.

int main()
{
   int t;
   string a;
   cin>>t;
   while(t--)
   {
       cin>>a;
       Solution obj;
       if(obj.ispar(a))
        cout<<"balanced"<<endl;
       else
        cout<<"not balanced"<<endl;
   }
}
// } Driver Code Ends