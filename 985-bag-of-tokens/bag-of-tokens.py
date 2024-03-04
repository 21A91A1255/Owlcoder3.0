class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i=0
        maxi=0
        c=0
        j=len(tokens)-1
        while(i<=j):
            if(power>=tokens[i]):
                power-=tokens[i]
                c+=1
                i+=1
                maxi=max(maxi,c)
            elif(c>0):
                power+=tokens[j]
                c-=1
                j-=1
            else:
                break
        return maxi
                