'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque

class Solution:
    def topView(self, root):
        if root is None:
            return []
            
        dq = deque()
        dq.appendleft((root, (0, 0)))
        view_dict = {}
        left, right = float('inf'), -float('inf')
        curr_level = 1
        
        while len(dq) != 0:
            curr_size = len(dq)
            # print(f"current level: {curr_level}")
            
            for i in range(curr_size):
                node, (r, c) = dq.pop()
                # print(node.data, "(", r, ",", c, ")")
                
                if c < left: 
                    left = c
                    left_val = node.data
                if c > right: 
                    right = c
                    right_val = node.data
                
                if node.left: dq.appendleft((node.left, (r+1, c-1)))
                if node.right: dq.appendleft((node.right, (r+1, c+1)))
            
            curr_level += 1
            # print(left, right)
            
            if left not in view_dict: view_dict[left] = left_val
            if right not in view_dict: view_dict[right] = right_val
            
            # print(view_dict)
            
        return [val for _, val in sorted(view_dict.items(), key = lambda x: x[0])]