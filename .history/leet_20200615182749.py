# how a binary tree works is the smaller numbers are 
# on the left then the bigger ones are on the right 
# returning the node also returns the children which is what 
# you want 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search(self,root:TreeNode,val:int):
    if root is None:
        return []
    elif root.val == val:
        print(root)
        return root   
    else:
        if val > root.val :
            print("root",root.val)
            # move to the right side with new root as one on the right
            return search(root.right,val)
        else:
            print("root",root.left)
            return search(root.left,val)          

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode
print(search([4,2,1,7,3],2))    