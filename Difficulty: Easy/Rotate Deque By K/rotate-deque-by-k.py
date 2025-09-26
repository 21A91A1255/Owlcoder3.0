from collections import deque
class Solution:    
    def rotateDeque(self, dq, type, k):
        #code here
        if(type==1):
            while dq and k>0:
                d=dq[-1]
                dq.pop()
                dq.appendleft(d)
                k-=1
            return dq
        else:
            while dq and k>0:
                d=dq[0]
                dq.popleft()
                dq.append(d)
                k-=1
            return dq
                
        
