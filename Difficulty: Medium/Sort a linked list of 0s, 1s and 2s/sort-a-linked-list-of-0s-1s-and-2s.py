'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
import heapq
class Solution:
    def segregate(self, head):
        #code here
        if(head is None or head.next is None):
            return head
        min_heap=[]
        curr=head
        temp=head
        while(curr!=None):
            heapq.heappush(min_heap,curr.data)
            curr=curr.next
        while temp:
            temp.data=heapq.heappop(min_heap)
            temp=temp.next
        return head
    