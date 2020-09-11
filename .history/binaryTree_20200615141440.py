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
