'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def inorder(self, node, func, res):
        if node is None:
            return res
        
        res = self.inorder(node.left, func, res)
        res = func(res, node.data)
        res = self.inorder(node.right, func, res)
        
        return res
        
    def findMax(self,root):
        return self.inorder(root, max, float('-inf'))
        
    def findMin(self,root):
        return self.inorder(root, min, float('inf'))