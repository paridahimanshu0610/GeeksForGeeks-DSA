class Solution:
    def infixToPrefix(self, s):
        stack = []
        res = []
        prec = {"+":1, "-":1, "*":2, "/":2, "^":3, "(":-1, ")":-1}
        
        def mustPop(curr):
            top = stack[-1]
            
            if top == ")":
                return False
            
            cond1 = prec[top] > prec[curr]
            cond2 = (curr == "^") and (prec[top] == prec[curr]) 
            
            return cond1 or cond2 
            
        for e in s[::-1]:
            if e not in prec.keys():
                res.append(e)
            elif e == ")":
                stack.append(e)
            elif e == "(":
                while len(stack)!=0 and stack[-1]!=")":
                    res.append(stack.pop())
                stack.pop()
            else:
                while len(stack)!=0 and mustPop(e):
                    res.append(stack.pop())
                stack.append(e)
                
        while len(stack)!=0:
            res.append(stack.pop())
            
        return "".join(res[::-1])