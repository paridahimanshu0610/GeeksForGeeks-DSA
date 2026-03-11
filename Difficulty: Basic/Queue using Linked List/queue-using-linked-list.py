# Node class
class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Queue class template
class myQueue:

    def __init__(self):
        # Initialize your data members
        self.head = None
        self.rear = None
        self.curr_capacity = 0

    def isEmpty(self):
        # Return True if queue is empty, else False
        return self.curr_capacity == 0 

    def enqueue(self, x):
        # Add element x to the rear
        node = Node(x)
        self.curr_capacity += 1
        
        if self.head is None:
            self.head = node
            self.rear = node
            return
        
        self.rear.next = node
        self.rear = node
        
    def dequeue(self):
        # Remove the front element
        if self.isEmpty():
            return -1
            
        val = self.head.data
        self.head = self.head.next
        self.curr_capacity -= 1
        
        return val

    def getFront(self):
        # Return front element
        # return -1 if empty
        if self.isEmpty():
            return -1
        
        val = self.head.data
        return val

    def size(self):
        # Return current size
        return self.curr_capacity