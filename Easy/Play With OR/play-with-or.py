#User function Template for python3

class Solution:
    def game_with_number (self, arr,  n) : 
        #Complete the function
        k=[]
        for i in range(len(arr)-1):
            p=(arr[i]|arr[i+1])
            k.append(p)
        k.append(arr[-1])
        return k


#{ 
 # Driver Code Starts

#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.game_with_number(arr, n);
    print(*res)




# } Driver Code Ends