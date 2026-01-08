from collections import deque
''' class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        node = root
        res = float('inf')
        found = False
        
        while node:
            if node.data==x:
                return x
            elif node.data > x:
                found = True
                res = min(node.data, res)
                node = node.left
            else:
                node = node.right
        

        return res if found else -1