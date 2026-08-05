class Solution:
    def postToInfix(self, s):
        stack = []
        operators = {"+", "-", "*", "/", "^"}
        
        for e in s:
            if e not in operators:
                stack.append(e)
            else:
                var2, var1 = stack.pop(), stack.pop()
                stack.append("("+var1+e+var2+")")
                
        return stack.pop()