# Create a node and assign a value to the node
# A tree node contains data then pointer to
class Node:
    def __init__(self,data):
        # designate one node as root 
        self.data = data 
        # then the two others as child nodes
        self.left = None 
        self.right = None
        