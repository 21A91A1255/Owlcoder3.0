#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    #code here
	    if(n<=1):return 0
	    if(arr[0]==0):return -1;
	    m=0
	    mr=0
	    jump=0
	    for i in range(n):
	        m=max(m,i+arr[i])
	        if(mr==i):
	            mr=m
	            jump+=1
	            if(mr>=n-1):
	                return jump
	    return -1
	            

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends