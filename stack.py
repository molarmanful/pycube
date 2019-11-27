class Stack:
    
    def __init__(self):
        
        self.items = []
        
        
    def push(self, *ms):
        
        for m in ms:
            self.items.insert(0, m)
    
    
    def add(self, *ms):
        
        self.items.extend(ms)
    
    
    def pop(self):
        
        return self.items.pop()
    
    
    def get(self, i):
        
        return None if not len(self.items) else self.items[i]
