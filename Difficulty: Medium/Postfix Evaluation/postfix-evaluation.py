import math
class Solution:
    def isoperand(self,i):
        try:
            return -10**4 < int(i) <10**4
        except ValueError:
            return False

    def evaluatePostfix(self, arr):
        stack = []
        for i in arr:
            if self.isoperand(i):
                stack.append(int(i))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if i == '+':
                    ans = op1 + op2
                elif i == '-':
                    ans = op1 - op2
                elif i == '*':
                    ans = op1 * op2
                elif i == '^':
                    ans = op1 ** op2  
                else: 
                    if op2 == 0:
                        raise ValueError("Division by 0")
                    ans = math.floor(op1 / op2)
                stack.append(ans)
        return stack[0]
