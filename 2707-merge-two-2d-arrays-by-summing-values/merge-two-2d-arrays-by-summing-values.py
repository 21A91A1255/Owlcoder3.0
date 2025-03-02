class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        p=nums1+nums2
        p.sort()
        x=[]
        a=[]
        z=[]
        c=0
        for i in range(0,len(p)-1,1):
            m=p[i]
            n=p[i+1]
            c=0
            if(m[0]==n[0]):
                x=[m[0],m[1]+n[1]]
                a.append(x)
                z.append(m)
                z.append(n)
                c=1
            else:
                if m not in z and n not in z:
                    a.append(m)
        if(c==0):
            a.append(p[-1])
        return a