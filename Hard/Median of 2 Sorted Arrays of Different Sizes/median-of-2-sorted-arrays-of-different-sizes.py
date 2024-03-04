#User function Template for python3
import math
class Solution:
    def MedianOfArrays(self, array1, array2):
            #code here
            k=array1+array2
            k.sort()
            if(len(k)%2!=0):
                return k[len(k)//2]
            else:
                p=(k[len(k)//2]+k[(len(k)//2)-1])
                if(p%2==0):
                    return p//2
                return p/2

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends