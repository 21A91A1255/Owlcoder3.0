class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def fun(self, root, l):
        if root is None:
            return
        self.fun(root.left, l)
        l.append(root.data)
        self.fun(root.right, l)
    
    def kthSmallest(self, root, k): 
        l = []
        self.fun(root, l)
        if(k<=len(l)):
            return l[k - 1]
        return -1
