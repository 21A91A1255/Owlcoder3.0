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
        if(head.next==None or head==None):
            return head
        prev=None
        current= head
        while(current!=None):
            prev=current.prev
            current.prev=current.next
            current.next=prev
            
            current=current.prev
        return prev.prev