class stack:
    def __init__(self):
        self.stack = []
            
    def size(self):
        return len(self.stack)
    
    def pop(self):
        if self.size() == 0:
            return None
        return self.stack.pop()
    
    def push(self, data):
        self.append(data)
        
    def __repr__(self):
        if len(self.stack) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.stack[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"

class stack_2:
    def __init__(self, size = 10):
        self.stack = [0 for _ in range(size)]
        self.next_index = 0
        self.size = 0
        
    def pop(self):
        if self.size == 0:
            self.next_index = 0
            return None
        self.next_index -= 1
        self.size -= 1
        return self.stack[next_index]
    
    def push(self, data):
        if self.next_index == len(self.arr):
            print("Out of space! Increasing array capacity ...")
            self.full_capacity()
            
        self.stack[self.next_index] = data
        self.next_index += 1
        self.size += 1
        
    def full_capacity(self):
        old_arr = self.stack
        self.arr = [0 for _ in range(len(2 * old_arr))]
        for index, value in enumerate(old_arr):
            self.arr[index] = value

    def __repr__(self):
        if len(self.stack) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.stack[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"