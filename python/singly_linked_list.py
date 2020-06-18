class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def print_list(self):
        if self.head == None:
            print("Empty List")
        else:
            cur = self.head
            while cur != None:
                print(cur.data)
                cur = cur.next
        
    def append(self, data):
        new_node = SinglyNode(data)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        
        self.tail.next = new_node
        self.tail = new_node 
        self.size += 1
    
    def prepend(self, data):
        new_node = SinglyNode(data)
        
        if self.head == None:
            self.append(data)
            return 
        
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def insert(self, data, index):
        if index == 0:
            self.prepend(data)
            return
        elif index == self.size - 1:
            self.append(data)
            return
        
        new_node = SinglyNode(data)
        cur = self.head
        for i in range(index):
            prev = cur 
            cur = cur.next 
        
        print(type(cur))
        prev.next = new_node
        new_node.next = cur
        self.size += 1
    
    def remove(self, data):
        cur = self.head
        while cur.data != data:
            prev = cur
            cur = cur.next
            if cur == self.tail:
                print("Not found")
                return
            next_node = cur.next
            
        prev.next = next_node
        if cur == self.head:
            self.head = self.head.next
        if cur == self.tail:
            self.tail = prev
        self.size -= 1
    
    def search(self, data):
        cur = self.head
        index = 0
        if cur == None:
            print("Not found")
        
        while cur.data != data:
            cur = cur.next
            index += 1
            if cur == self.tail:
                print("Not found")
                return 
        return index
    
    def merge(self, list2):
        self.tail.next = list2.head
        self.tail = list2.tail
        self.size += list2.size
        
    def reverse(self):
        if self.head == self.tail:
            return 
        
        cur = self.head
        prev = None
        self.tail = cur
        while cur != None:
            next_node = cur.next
            cur.next = prev 
            prev = cur
            cur = next_node
        self.head = prev