# Linked List implementation 

# implements the node type 
# stores a single data field ---> val 

class Node(object):
    def __init__(self,val):
        self.val = val 
        self.next = None 
    def get_data(self):
        return self.val 
    def set_data(self,val):
        self.val = val 
    def get_next(self):
        return self.next
    def set_next(self,next):
        self.next = next 
class LinkedList(object):
    def __init__(self,head=None):
        self.head = head 
        self.count = 0 
    def get_count(self):
        return self.count 
    def insert(self,data):
        # insert a new node 
        new_node = Node(data)
        new_node.set_next(self.head)
        
    def find(self,val):
        # Find the first element with a given value 
        item = self.head 
        return None
    def deleteAt(self,idx):
        # to delete an item at a given index 
        if idx > self.count-1:
            return 
    def dump_list(self):
        tempnode = self.head 
        while tempnode != None:
            print("Node: ",tempnode.get_data())
            tempnode = tempnode.get_next()


       


