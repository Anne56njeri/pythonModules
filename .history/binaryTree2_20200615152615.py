# Create a node and assign a value to the node

class Node:
    def __init__(self,data):
        # designate one node as root 
        self.data = data 
        # then the two others as child nodes
        self.left = None 
        self.right = None
    # A function to print in order traversal 
def inorder_traversal(root):
    # if the root is not empty 
    if root:
        inorder_traversal(root.left)
        print(root.data)
        inorder_traversal(root.right)



root = Node(1)
           