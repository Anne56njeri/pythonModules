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
# 1 is root 
# creating left child
'''
'''

tree = BinaryTree(1)      
tree.root.left = Node(2)  
tree.root.right = Node(3)
tree.root.left.left = Node(4)   
tree.root.left.right = Node(5)    
