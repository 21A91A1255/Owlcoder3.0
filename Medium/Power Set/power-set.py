#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		k=1<<len(s)
		p=[]
		for i in range(k):
		    k=[]
		    for j in range(len(s)):
		        if(i&(1<<j)):
		            k.append(s[j])
		    p.append(k)
		ans=[]
		for i in range(len(p)):
		    m="".join(p[i])
		    if(m!=''):
		        ans.append(m)
		ans.sort()
	    return ans


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends