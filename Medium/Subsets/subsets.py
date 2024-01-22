#User function Template for python3

class Solution:
    def subsets(self, l):
        n=len(l)
        p=1<<(len(l))
        k1=[]
        for i in range(p):
           k=[]
           for j in range(n):
               if(i&(1<<j)):
                    k.append(l[j])
           k1.append(k)
        return sorted(k1)
               
                #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        A = list(map(int,input().strip().split()))
        
        ob=Solution()
        result =ob.subsets(A)
        
        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j],end=" ")
                
            print()
            
            

# } Driver Code Ends