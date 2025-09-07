'''
class Node:
    def _init_(self, x):
        self.data = x
        self.next = None
'''
import heapq
class Solution:
    def mergeKLists(self, arr):
        # code here
        heap=[]
        new=Node(0)
        head=new
        for i in range(len(arr)):
            l=arr[i]
            while(l!=None):
                heapq.heappush(heap,(l.data,l))
                l=l.next
        while heap:
            val,node = heapq.heappop(heap)
            head.next = Node(val)
            head = head.next
        
        return new.next