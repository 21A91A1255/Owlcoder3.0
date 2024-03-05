#User function Template for python3

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,a, n): 
        ##Your code here
        i=0
        j=n-1
        m=0
        l=[]
        while(i<=j):
            if(a[i]<=a[j]):
                l.append(j-i)
                i+=1
                j=n-1
            else:
                j-=1
        #print(l)
        return max(l)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends