#User function Template for python3


class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        c={}
        for i in range(len(arr)):
            p=''.join(sorted(arr[i]))
            if p in c:
                c[p].append(arr[i])
            else:
                c[p]=[arr[i]]
        return list(c.values())



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends