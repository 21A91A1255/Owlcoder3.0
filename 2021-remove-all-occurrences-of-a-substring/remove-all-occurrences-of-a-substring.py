class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        d=s.find(part)
        while(d!=-1):
            p=s.find(part)
            if(p==-1):
                break
            r=p+len(part)
            s=s[:p]+s[r:]
        return s