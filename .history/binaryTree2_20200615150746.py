# Create a node and assign a value to the node

class Node:
    def __init__(self,data):
        # designate one node as root 
        self.data = data 
        # then the two others as 
        self.left = None 
        self.right = None
    def printTree(self):
        print(self.data)

root = Node(10) 
root.printTree()            