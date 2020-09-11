# Create a node and assign a value to the node
# A tree node contains data then pointer to left child and pointer to right child 

class Node:
    def __init__(self,data):
        # designate one node as root 
        self.data = data 
        # then the two others as child nodes
        self.left = None 
        self.right = None 
def inorder(root):
    if root:
        # Traverse left 
        newArr = []
        inorder(root.left)
        newArr.append(root.data)
        print()
        inorder(root.right)
            


root = Node(1)
root.left = Node(2)
root.right = Node(3) 
root.left.right = Node(4)
inorder(root)


        