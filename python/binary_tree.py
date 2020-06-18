class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
    
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data
    
    def set_left(self, data):
        self.left = data
        
    def get_left(self):
        return self.left

    def set_right(self, data):
        self.right = data
        
    def get_right(self):
        return self.right
    
    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
class Tree:
    def __init__(self, data):
        self.root = Node(data)
    
    def get_root(self):
        return self.root