# Create a node and assign a value to the node
# A tree node contains data then pointer to left child and pointer to right child 

class Node:
    def __init__(self,data):
        # designate one node as root 
        self.data = data 
        # then the two others as child nodes
        self.left = None 
        self.right = None 
def inorder(root,newArr):
    if root:
        # Traverse left 
       
        inorder(root.left,newArr)
        newArr.append(root.data)
        print(newArr)
        inorder(root.right,newArr)
    return new    
            


root = Node(1)
root.left = Node(2)
root.right = Node(3) 
root.left.right = Node(4)
inorder(root)


        