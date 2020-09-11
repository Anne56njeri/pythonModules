# Create a node and assign a value to the node

class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None
    def printTree(self):
        print(self.data)
        
            