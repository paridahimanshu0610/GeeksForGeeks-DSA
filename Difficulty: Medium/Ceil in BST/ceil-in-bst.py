'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self, root, x):
        if root is None:
            return -1
            
        if root.data == x:
            return root.data
        elif root.data > x:
            temp = self.findCeil(root.left, x)
            return temp if temp > 0 else root.data
        else:
            return self.findCeil(root.right, x)