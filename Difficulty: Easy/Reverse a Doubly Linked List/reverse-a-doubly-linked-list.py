"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        st=[]
        temp=head
        while(temp!=None):
            st.append(temp.data)
            temp=temp.next
        temp=head
        while(temp!=None):
            temp.data=st[-1]
            st.pop()
            temp=temp.next
        return head
        
        