class Solution:
	def nextSmallerEle(self, a):
	    res = [None]*len(a)
	    stack = []
	    
	    for i in range(len(a)):
	        if (len(stack) == 0) or (a[i] >= a[stack[-1]]):
	            stack.append(i)
	        else:
	            while len(stack) > 0 and a[stack[-1]] > a[i]:
	                res[stack[-1]] = a[i]
	                stack.pop()
	            stack.append(i)
	            
	    while len(stack) > 0:
	        res[stack[-1]] = -1
	        stack.pop()
	        
	    return res