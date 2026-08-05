# Corrected rule set, consolidated:

# 1. If current token is an operand → append to output.
# 2. If current token is ( → push onto stack.
# 3. If current token is ) → pop and output operators until you pop a matching ( (discard both parens).
# 4. If current token is an operator:
#     i. While the stack is non-empty, the top is not (, and (top's precedence > current's precedence, or (top's precedence == current's precedence and current operator is left-associative)) → pop top to output.
#     ii. Then push current operator.
# 5. After the string is fully scanned, pop all remaining operators from the stack to the output.

class Solution:
    def infixToPostfix(self, s):
        res = []
        stack = []
        prec = {"+":1, "-":1, "*":2, "/":2, "^":3}
        operators = {"+", "-", "*", "/", "^", "(", ")"}
        
        def mustPop(curr):
            top = stack[-1]
            
            if top == "(":
                return False
            
            cond1 = prec[top] > prec[curr]
            cond2 = (prec[top] == prec[curr]) and (curr in {"+", "-", "*", "/"})
            
            return cond1 or cond2
            
        for e in s:
            if e not in operators:
                res.append(e)
            else:
                if e == "(":
                    stack.append(e)
                elif e == ")":
                    while len(stack)!=0 and stack[-1]!="(":
                        res.append(stack.pop())
                    stack.pop() # Removing "(" 
                else:
                    while len(stack)!=0 and mustPop(e):
                        res.append(stack.pop())
                    stack.append(e)
         
        while len(stack)!=0:
            res.append(stack.pop())
            
        return "".join(res)