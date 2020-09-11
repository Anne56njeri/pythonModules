# define node class
class Node(object):
    # constructor
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None 

# define binary tree class
class BinaryTree(object):
    def __init__(self,root):
        # converting data
        self.root = Node(root) 
        # root -->left--->right(preorder)
    def preorder_print(self,start,traversal):
        if start:
            traversal += (str(start.value) + "_")
            # calling the function recursively
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.)

     
# 1 is root 
# creating left child
    '''
       1
    # /    \
    2       3
   / \
   4  5
    '''

tree = BinaryTree(1)      
tree.root.left = Node(2)  
tree.root.right = Node(3)
tree.root.left.left = Node(4)   
tree.root.left.right = Node(5)  
tree.root.right.right = Node(7)
tree.root.right.left = Node(6)

