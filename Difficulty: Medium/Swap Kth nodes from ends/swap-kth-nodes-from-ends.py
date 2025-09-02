'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def swapKth(self, head, k):
        # code here
        temp=head
        l=[]
        while(head!=None):
            l.append(head.data)
            head=head.next
        if(k>len(l)):
            return temp
        (l[k-1],l[-k])=(l[-k],l[k-1])
        x=Node(l[0])
        t=x
        for i in range(1,len(l)):
            y=Node(l[i])
            t.next=y
            t=t.next
        return x
        
