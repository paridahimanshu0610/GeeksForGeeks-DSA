class Solution:
    def postToPre(self, s):
        stack = []
        operators = {"+":1, "-":1, "*":2, "/":2, "^":3, "(":-1, ")":-1}
        
        for e in s:
            if e not in operators.keys():
                stack.append(e)
            else:
                var2, var1 = stack.pop(), stack.pop()
                stack.append((var1, e, var2))
                
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
            cond1 = operators[top] > operators[curr]
            cond2 = (operators[top] == operators[curr]) and (curr == "^")
            
            return cond1 or cond2
            
        for e in infix[::-1]:
            if e not in operators.keys():
                res.append(e)
            else:
                if e == ")":
                    stack.append(e)
                elif e == "(":
                    while len(stack)!=0 and stack[-1]!=")":
                        res.append(stack.pop())
                    stack.pop()
                else:
                    while len(stack)!=0 and mustPop(e):
                        res.append(stack.pop())
                    stack.append(e)
                    
        return "".join(res[::-1])