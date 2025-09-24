from collections import deque

class SpecialQueue:
    def __init__(self):
        self.q = deque()
    
    def enqueue(self, x):
        self.q.append(x)
    
    def dequeue(self):
        if self.q:
            return self.q.popleft()
        return None
    
    def getFront(self):
        if self.q:
            return self.q[0]
        return None
    
    def getMin(self):
        if self.q:
            return min(self.q)
        return None
    
    def getMax(self):
        if self.q:
            return max(self.q)
        return None
