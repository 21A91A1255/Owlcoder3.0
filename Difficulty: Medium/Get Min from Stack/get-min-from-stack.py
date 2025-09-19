class SpecialStack:

    def __init__(self):
        # Define Stack
        self.stack=[]
        self.minstack=[]
    
    def push(self, x):
        # Add an element to the top of Stack
        self.stack.append(x)
        if not self.minstack or x<=self.minstack[-1]:
            self.minstack.append(x)
    
    def pop(self):
        # Remove the top element from the Stack
        if not self.stack:
            return -1
        val=self.stack.pop()
        if(val==self.minstack[-1]):
            self.minstack.pop()
        return val
        
    
    def peek(self):
        # Returns top element of Stack
        if self.stack:
            return self.stack[-1]
        else:
            return -1
        
    def isEmpty(self):
        # Check if the stack is empty
        if len(self.stack)==0:
            return True
            
    
    def getMin(self):
        # Finds minimum element of Stack
        if len(self.stack)>=1:
            return self.minstack[-1]
        else:
            return -1