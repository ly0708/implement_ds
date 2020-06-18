class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
        new_node = DoublyNode(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return 

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

        
    def prepend(self, data):
        new_node = DoublyNode(data)
        
        if self.head == None:
            self.append(data)
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1