from itertools import permutations
class Solution:
    def uniquePerms(self, arr):
        p=list(permutations(arr))
        s=set(p)
        l=[]
        for i in s:
            l.append(list(i))
        l.sort()
        return l