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
        
        inorder(root.right,newArr)
        print(newArr)
    return newArr  
def morris_traversal(root):
    # function for iterative inorder tree traversal 
    current = root 
    while current is not None:
        # do the following 
        if current.left is None:
            yield current.data 
        else:
            # find the current in order predecessor of current 
            pre = current.left
            while pre.right is not None and pre.right 


           
            


root = Node(1)
root.left = Node(2)
root.right = Node(3) 
root.left.right = Node(4)
root.left.left = Node(7)
print(inorder(root,[]))


        