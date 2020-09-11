# Create a node and assign a value to the node

class Node:
    def __init__(self,data):
        # designate one node as root 
        self.data = data 
        # then the two others as child nodes
        self.left = None 
        self.right = None
    def insert(self,data):
            
    def printTree(self):
        print(self.data)

root = Node(10) 
root.printTree()            