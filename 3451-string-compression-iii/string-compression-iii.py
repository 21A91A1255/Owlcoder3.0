class Solution:
    def compressedString(self, word: str) -> str:
        c=0
        ans=''
        for i in range(len(word)-1):
            if(word[i]==word[i+1]):
                c+=1
                if(c==9):
                    ans+=str(c)
                    ans+=word[i]
                    c=0
            elif(word[i]!=word[i+1]):
                ans+=str(c+1)
                ans+=word[i]
                c=0
        if(len(word)>=2):
            ans+=str(c+1)
            ans+=word[i+1]
        else:
            ans+='1'
            ans+=word[0]
        return ans
