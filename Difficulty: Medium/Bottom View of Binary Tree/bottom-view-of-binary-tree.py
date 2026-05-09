'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
from collections import deque

class Solution:
    def bottomView(self, root):
        if root is None:
            return []
            
        dq = deque()
        dq.appendleft((root, (0, 0)))
        view_dict = {}
        minc = float('inf')
        
        while len(dq) != 0:
            node, (r, c) = dq.pop()
            
            view_dict[c] = node.data
            if c < minc: minc = c
            
            if node.left: dq.appendleft((node.left, (r+1, c-1)))
            if node.right: dq.appendleft((node.right, (r+1, c+1)))
            
        res = [None]*len(view_dict)
        
        for key, val in view_dict.items():
            res[key-minc] = val
            
        return res