class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        p=''
        m=len(s)
        d=s
        for i in range(m):
            if(s==goal):
                return True
            else:
                p+=d[i]
                s=d[i+1:m]
                s=s+p
        return False
        