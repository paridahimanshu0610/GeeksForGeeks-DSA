class Solution:
	def prevSmaller(self, a):
	    n = len(a)
	    stack = []
	    res = [None]*n
	    
	    for i in range(n):
	        while len(stack)>0 and stack[-1]>=a[i]:
	            stack.pop()
	            
	        if len(stack)>0:
	            res[i] = stack[-1]
	        else:
	            res[i] = -1
	            
	        stack.append(a[i])
	        
	    return res