class Queue:
    def __init__(self):
        self.q = []
    
    def size(self):
        return len(self.q)
    
    def enq(self, data):
        self.q.append(data)
    
    def deq(self):
        return self.q.pop(0)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<top of queue>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q[::-1]])
            s += "\n_________________\n<bottom of queue>"
            return s
        
        else:
            return "<queue is empty>"