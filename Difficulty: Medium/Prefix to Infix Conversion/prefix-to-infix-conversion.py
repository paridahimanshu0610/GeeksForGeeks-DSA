class Solution:
    def preToInfix(self, s):
        res = []
        stack = []
        operators = {"+", "-", "*", "/", "^"}
        
        for e in s[::-1]:
            if e not in operators:
                stack.append(e)
            else:
                var1, var2 = stack.pop(), stack.pop()
                stack.append("("+var1+e+var2+")")
                
        return stack.pop()