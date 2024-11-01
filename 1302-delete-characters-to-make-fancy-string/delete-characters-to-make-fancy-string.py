class Solution:
    def makeFancyString(self, s: str) -> str:
        a=''
        c=0
        for i in range(len(s)-1):
            if(s[i]==s[i+1]):
                c+=1
                if(c>=2):
                    a+=''
                elif(c==2):
                    a+=s[i]
                else:
                    a+=s[i]
            else:
                a+=s[i]
                c=0
        a+=s[-1]
        return a