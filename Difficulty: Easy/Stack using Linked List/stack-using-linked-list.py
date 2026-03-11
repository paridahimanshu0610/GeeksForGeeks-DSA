# Node class
''' class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None 
'''

# Stack class template
class myStack:
    def __init__(self):
        self.head = None
        self.curr_capacity = 0

    def isEmpty(self):
        return self.curr_capacity == 0
        
    def push(self, x):
        # Adds element x to the top of the stack
        node = Node(x)
        self.curr_capacity += 1
        
        if self.head is None:
            self.head = node
            return
        
        node.next = self.head
        self.head = node

    def pop(self):
        # Removes an element from the top of the stack
        if self.isEmpty():
            return -1
        
        val = self.head.data
        self.head = self.head.next
        self.curr_capacity -= 1
        
        return val

    def peek(self):
        # Returns the top element of the stack
        # If the stack is empty, return -1
        if self.isEmpty():
            return -1
            
        return self.head.data

    def size(self):
        # Returns the current size of the stack
        return self.curr_capacity