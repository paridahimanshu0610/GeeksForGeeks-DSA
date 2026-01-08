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
        res = -1
        
        while node:
            if node.data==x:
                return x
            elif node.data > x:
                res = node.data
                node = node.left
            else:
                node = node.right
        
        return res