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
    def print_tree(self,traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root," ")
        elif traversal_type == "inorder":
            return self.inorder_print (tree.root,"")
        elif traversal_type == "postorder":
            re       
        else:
            print("Traversal type" + str(traversal_type) + "is not supported.")   
            return False 

        # root -->left--->right(preorder)
    def preorder_print(self,start,traversal):
        if start:
            traversal += (str(start.value) + "-")
            # calling the function recursively
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal   
        # left - root -right
    def inorder_print(self,start,traversal):
        if start:
            traversal = self.inorder_print(start.left,traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right,traversal)
        return traversal   
        # left ->right -> root
    def postorder_print(self,start,traversal):
        if start:
            traversal = self.postorder_print(start.left,traversal)
            traversal = self.postorder_print(start.right,traversal)
            traversal +=(str(start.value) + "-" )
        return traversal    



     
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

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))