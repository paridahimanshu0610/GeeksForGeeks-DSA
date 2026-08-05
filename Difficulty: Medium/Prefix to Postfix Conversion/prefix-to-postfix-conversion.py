class Solution:
    def preToPost(self, s):
        stack = []
        prec = {"+":1, "-":1, "*":2, "/":2, "^":3, "(":-1, ")":-1}
        
        for e in s[::-1]:
            if e not in prec:
                stack.append(e)
            else:
                var1, var2 = stack.pop(), stack.pop()
                stack.append((var1,e,var2))
                
        root = stack.pop()
        infix = []
        
        def build(node):
            if isinstance(node, str):
                infix.append(node)
            else:
                var1, op, var2 = node
                infix.append("(")
                build(var1)
                infix.append(op)
                build(var2)
                infix.append(")")
                
        build(root)
        res = []
        
        def mustPop(curr):
            top = stack[-1]
            
            cond1 = prec[top] > prec[curr]
            cond2 = (prec[top] == prec[curr]) and (curr in {"+", "-", "*", "/"})
            
            return cond1 or cond2
            
        for e in infix:
            if e not in prec:
                res.append(e)
            elif e=="(":
                stack.append("(")
            elif e==")":
                while len(stack)!=0 and stack[-1]!="(":
                    res.append(stack.pop())
                stack.pop()
            else:
                while len(stack)!=0 and mustPop(e):
                    res.append(stack.pop())
                stack.append(e)
                
        return "".join(res)