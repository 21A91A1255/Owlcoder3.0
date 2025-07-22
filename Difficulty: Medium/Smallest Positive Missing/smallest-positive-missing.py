class Solution:
    def missingNumber(self, arr):
        # code here
        s=set(arr)
        l=list(s)
        a=[]
        for i in range(len(l)):
            if(l[i]>=0):
                a.append(l[i])
        a.sort()
        if(len(a)==0):
            return 1
        if(len(a)==1 and a[0]==0):
            return 1
        if(a[0]==0):
            a.remove(a[0])
        for i in range(len(a)):
            if(a[i]!=i+1):
                return i+1
        return a[-1]+1
                
                