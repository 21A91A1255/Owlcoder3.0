'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    def removeLoop(self, head):
        slow=head
        fast=head
        p=0
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                break
        else:
            return False
        
        slow=head
        while(fast!=slow):
            fast=fast.next
            slow=slow.next
        
        while(fast.next!=slow):
            fast=fast.next
        fast.next=None
            
            
            
            
        
        