class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for i in range(len(details)):
            s=details[i]
            t=s[11]+s[12]
            if(int(t)>60):
                c+=1
        return c        