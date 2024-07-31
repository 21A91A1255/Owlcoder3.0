#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        if(len(arr)==1):return arr[0]
        x=''
        for i in range(min(len(arr[0]),len(arr[1]))):
            if(arr[0][i]==arr[1][i]):
                x+=arr[0][i]
            else:
                break
        for j in range(2,len(arr)):
            a=''
            for k in range(min(len(x),len(arr[j]))):
                if(arr[j][k]==x[k]):
                    a+=x[k]
                else:
                    break
            x=a
        if(x==''):
            return -1
        return x
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends