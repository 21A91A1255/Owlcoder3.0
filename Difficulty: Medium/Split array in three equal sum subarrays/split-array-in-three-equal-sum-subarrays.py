#User function Template for python3
class Solution:
    
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        d=sum(arr)
        t=d//3
        if(d%3!=0):
            return [-1,-1]
        cs=0
        l=[]
        for i in range(len(arr)):
            cs+=arr[i]
            if(cs==t):
                l.append(i)
                cs=0
            if(len(l)==2):
                break
        v=sum(arr[i+1:])
        if(len(l)==2 and v==t):
            return [l[0],l[1]]
        return [-1,-1]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.findSplit(arr)

        if (result == [-1, -1]) or len(result) != 2:
            print("false")
        else:
            sum1 = sum2 = sum3 = 0
            for i in range(len(arr)):
                if i <= result[0]:
                    sum1 += arr[i]
                elif i <= result[1]:
                    sum2 += arr[i]
                else:
                    sum3 += arr[i]

            if sum1 == sum2 == sum3:
                print("true")
            else:
                print("false")
        print("~")

# } Driver Code Ends