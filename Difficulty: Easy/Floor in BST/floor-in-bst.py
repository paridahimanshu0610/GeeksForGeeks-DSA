'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        node = root
        res = -1
        
        while node:
            if node.data == k:
                return k
            elif node.data < k:
                res = max(res, node.data)
                node = node.right
            else:
                node = node.left
                
        return res