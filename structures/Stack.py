class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        
        removed = self.stack.pop()
        return removed
    
    def len(self):
        return len(self.stack)
    
    def last(self):
        if len(self.stack) == 0:
            return None 
        
        return self.stack[-1]