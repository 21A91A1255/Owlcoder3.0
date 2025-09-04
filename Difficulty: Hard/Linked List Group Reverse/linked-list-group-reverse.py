"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""

class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        st=[]
        if(head is None or head.next is None):
             return head
        i=0
        temp=head
        curr=head
        while(curr!=None):
            i+=1
            st.append(curr.data)
            curr=curr.next
            if(i==k):
                while(st):
                    temp.data=st.pop()
                    temp=temp.next
                i=0
        while(st):
            temp.data=st.pop()
            temp=temp.next
        return head
            
                