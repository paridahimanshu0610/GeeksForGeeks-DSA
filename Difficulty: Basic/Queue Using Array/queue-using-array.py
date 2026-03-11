class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.arr = [-1]*n
        self.size = n
        self.front = 0
        self.rear = -1
        self.count = 0
    
    
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        # Check if queue is full
        return self.count == self.size
    
    def enqueue(self, x):
        # Enqueue
        if self.isFull():
            return
        
        self.rear = (self.rear+1) % self.size
        self.arr[self.rear] = x
        self.count += 1
    
    def dequeue(self):
        # Dequeue
        if self.isEmpty():
            return -1
            
        val = self.arr[self.front]
        self.front = (self.front+1) % self.size
        self.count -= 1
        
        return val
    
    def getFront(self):
        # Get front element
        if self.isEmpty():
            return -1
            
        return self.arr[self.front]
    
    def getRear(self):
        # Get rear element
        if self.isEmpty():
            return -1
            
        return self.arr[self.rear]