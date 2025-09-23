#from collections import deque
class Solution:
    def reverseQueue(self, q):
        # code here
        st=[]
        while q:
            st.append(q.popleft())
        while st:
            q.append(st.pop())
        return q
            
        