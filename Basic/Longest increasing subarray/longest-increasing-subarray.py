#User function Template for python3

class Solution:
    def lenOfLongIncSubArr(self, arr, n):
        #Code here]
        m=0
        c=0
        for i in range(len(arr)-1):
            if(arr[i+1]>arr[i]):
                c+=1
                if(c>m):
                    m=c
            else:
                c=0
        #print(m+1)
        return m+1
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        print(Solution().lenOfLongIncSubArr(a, n))
        
        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends