#User function Template for python3
class Solution:
	def printString(self, s, ch, count):
		# code here
		if ch not in s:
		    return ""
		c=0
		r=-1
		for i in range(len(s)):
		    if(s[i]==ch):
		        c+=1
		        if(c==count):
		            r=i
		            break
		if(c!=count):
		    return ""
		else:
		    return s[r+1:]
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ch = input()[0]
        count = int(input())
        ob = Solution()
        answer = ob.printString(s, ch, count)

        print(answer)

# } Driver Code Ends