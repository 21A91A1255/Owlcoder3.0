class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m=len(matrix)
        n=len(matrix[0])
        j=0
        k=[]
        while(j<n):
            l=[]
            for i in range(m):
                p=matrix[i]
                l.append(p[0])
                p.remove(p[0])
            k.append(l)
            j+=1
        return k