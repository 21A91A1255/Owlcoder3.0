class Solution:
    def maxEdgesToAdd(self, V, edges):
        # code here
        p=(V*(V-1))//2
        return p-len(edges)