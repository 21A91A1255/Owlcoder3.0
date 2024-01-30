class Solution {
public:
    int evalRPN(vector<string>& s) {
        stack<int>st;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]!="*" && s[i]!="/" && s[i]!="+" && s[i]!="-")
            {
                st.push(stoi(s[i]));
                continue;
            }
            else
            {
                int q=st.top();
                st.pop();
                int p=st.top();
                st.pop();
                if(s[i]=="*")
                {
                    int m=p*q;
                    st.push(m);
                }
                else if(s[i]=="-")
                {
                    int m=p-q;
                    st.push(m);
                }
                else if(s[i]=="/")
                {
                    int m=p/q;
                    st.push(m);
                }
                else
                {
                    int m=p+q;
                    st.push(m);
                }
            }
        }
        return st.top();
    }
};