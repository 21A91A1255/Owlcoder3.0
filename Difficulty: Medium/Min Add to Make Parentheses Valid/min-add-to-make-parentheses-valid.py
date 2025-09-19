class Solution:
    def minParentheses(self, s):
        st=[]
        c=0
        for i in range(len(s)):
            if(s[i]=='('):
                st.append('(')
            elif(s[i]==')'):
                if st and st[-1]=='(':
                    st.pop()
                else:
                    c+=1
        return len(st)+c