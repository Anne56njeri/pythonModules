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
        # point the new node to the current head
        new_node.set_next(self.head)
        # set head as the new node
        self.head = new_node 
        self.count +=1
    def find(self,val):
        # Find the first element with a given value 
        item = self.head 
        # we check if item is not none and equal to the val we are looking for 
        while item !=None:
            if item.get_data() == val:
                return item 
            else:
                item.get_next()    
        return None
    def deleteAt(self,idx):
        # to delete an item at a given index 
        if idx > self.count-1:
            return 
        if idx == 0:
            self.head = self.head.get_next()
        else:
            # we have to go back to the number before the one we want to delete 
            tempIdx = 0 
            node = self.head
            while tempIdx < idx-1:
                node = node.get_next()
                tempIdx +=1 
            node.set_next(node.get_next)     

    def dump_list(self):
        tempnode = self.head 
        while tempnode != None:
            print("Node: ",tempnode.get_data())
            tempnode = tempnode.get_next()
#  create a linked list and insert some items 
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)
itemlist.dump_list()

# excercise the list 
print("item count: ",itemlist.get_count)
print("Finding item: ",itemlist.find(13))


       


