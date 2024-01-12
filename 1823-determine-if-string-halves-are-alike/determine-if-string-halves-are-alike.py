class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        p=s[:len(s)//2]
        q=s[(len(s)//2):]
        c=0
        d=0
        for i in p:
            if i in 'aeiouAEIOU':
                c+=1
        for i in q:
            if i in 'aeiouAEIOU':
                d+=1
        if(c==d):
            return True
        else:
            return False