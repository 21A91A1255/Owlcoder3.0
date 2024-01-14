from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if(len(word1)!=len(word2)):
            return False
        elif(sorted(word1)==sorted(word2)):
            return True
        else:
            word1=sorted(word1)
            word2=sorted(word2)
            c=Counter(word1)
            d=Counter(word2)
            p=set(word1)
            q=set(word2)
            l=[]
            for i in c.values():
                l.append(i)
            m=[]
            for i in d.values():
                m.append(i)
            l.sort()
            m.sort()
            if(l==m and p==q):
                return True
            else:
                return False
    

