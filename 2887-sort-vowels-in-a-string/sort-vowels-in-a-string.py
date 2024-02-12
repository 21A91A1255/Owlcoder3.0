class Solution:
    def sortVowels(self, s: str) -> str:
        o='AEIOUaeiou'
        ans=''
        p=''
        for i in s:
            if i in o:
                p+=i
                ans+='0'
            else:
                ans+=i
        p=sorted(p)
        res=''
        for i in range(len(ans)):
            if(ans[i]=='0'):
                res+=p[0]
                p.remove(p[0])
            else:
                res+=ans[i]
        return res