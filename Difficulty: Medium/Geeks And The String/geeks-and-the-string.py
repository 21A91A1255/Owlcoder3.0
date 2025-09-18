#User function Template for python3

class Solution:
    
    #Function to remove pair of duplicates from given string using Stack.
    def removePair(self,s):
        # code here
        st=[]
        for i in range(len(s)):
            if st and st[-1]==s[i]:
                st.pop()
            else:
                st.append(s[i])
        ans=""
        while st:
            ans=st.pop()+ans
        if(ans==""):
            return -1
        return ans