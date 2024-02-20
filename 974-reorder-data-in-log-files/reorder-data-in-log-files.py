class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        d='1234567890'
        k=[]
        p=[]
        for i in range(len(logs)):
            m=logs[i].split()
            if m[1][0] in d:
                k.append(logs[i])
            else:
                p.append(logs[i])
        p = sorted(p, key=lambda x: (x.split()[1:], x.split()[0]))
        ans=p+k
        return ans
            
        