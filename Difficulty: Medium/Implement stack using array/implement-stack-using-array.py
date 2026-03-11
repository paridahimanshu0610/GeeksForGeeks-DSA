class myStack:
    def __init__(self, n):
        self.arr = [-1]*n
        self.size = n
        self.curr_ptr = -1

    def isEmpty(self):
        return self.curr_ptr == -1
    
    def isFull(self):
        return self.curr_ptr == self.size-1

    def push(self, x):
        if self.isFull():
            return
        
        self.curr_ptr += 1
        self.arr[self.curr_ptr] = x
    
    def pop(self):
        if self.isEmpty():
            return -1
        
        val = self.arr[self.curr_ptr]
        self.arr[self.curr_ptr] = -1
        self.curr_ptr -= 1
        
        return val
    
    def peek(self):
        if self.isEmpty():
            return -1
        
        return self.arr[self.curr_ptr]