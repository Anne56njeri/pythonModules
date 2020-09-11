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
        


