"""
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def minValue(self, root):
        if root is None:
            return -1
            
        if root.left is None:
            return root.data
            
        return self.minValue(root.left)