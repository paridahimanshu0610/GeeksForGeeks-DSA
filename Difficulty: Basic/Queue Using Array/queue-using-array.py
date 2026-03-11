class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.arr = [-1]*n
        self.size = n
        self.front = 0
        self.rear = -1
    
    
    def isEmpty(self):
        return (self.rear==-1) or ((self.arr[self.rear] == -1) and (self.arr[self.front] == -1))
    
    def isFull(self):
        # Check if queue is full
        return (self.rear!=-1) and ((self.rear+1) % self.size == self.front) and ((self.arr[self.rear] != -1) and (self.arr[self.front] != -1))

    def enqueue(self, x):
        # Enqueue
        if self.isFull():
            return
        
        self.rear = (self.rear+1) % self.size
        self.arr[self.rear] = x
    
    def dequeue(self):
        # Dequeue
        if self.isEmpty():
            return -1
            
        val = self.arr[self.front]
        self.arr[self.front] = -1
        self.front = (self.front+1) % self.size
        
        return val
    
    def getFront(self):
        # Get front element
       return self.arr[self.front]
    
    def getRear(self):
        # Get rear element
        if self.isEmpty():
            return -1
            
        return self.arr[self.rear]