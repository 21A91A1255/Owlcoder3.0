#User function Template for python3
from collections import Counter
class Solution:
    def sameFreq(self, s):
        # code here
        l=[]
        v=0
        c=Counter(s)
        d=0
        for i in c.keys():
            d+=1
            if c[i] in l:
                v+=1
            l.append(c[i])
        if(len(set(l))==1):
            return 1
        if((v+1)!=(d-1)):
            return 0
        else:
            k=list(l)
            l.sort()
            l[0]=l[0]-1
            if((l[0])==0):
                l.remove(l[0])
            if(len(set(l))==1):
                return 1
            else:
                k.sort()
                k[len(k)-1]=k[len(k)-1]-1
                if((k[len(k)-1])==0):
                    k.remove(k[len(k)-1])
                if(len(set(k))==1):
                    return 1
        return 0
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends