class Solution:
    def reverseWords(self, s: str) -> str:
        p=''
        st=''
        for i in s.split():
            st+=i
            st+=" "
        st=st[::-1]
        for i in st.split():
            p+=i[::-1]
            p+=" "
        p=p[:len(p)-1]
        return p