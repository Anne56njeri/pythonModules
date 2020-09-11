# define node class
class Node(object):
    # constructor
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None 

# define b
class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)       
