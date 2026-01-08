'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def findFloor(self, root, x):
        res = float('-inf')
        found = False
        node = root
        
        while node:
            if node.data==x:
                return x
            elif node.data < x:
                found = True
                res = max(res, node.data)
                node = node.right
            else:
                node = node.left
        
        return res if found else -1