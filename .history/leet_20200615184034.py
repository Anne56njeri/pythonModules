# how a binary tree works is the smaller numbers are 
# on the left then the bigger ones are on the right 
# returning the node also returns the children which is what 
# you want 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search(self,root:TreeNode,val:int)-> TreeNode:
    if root is None:
        return []
    elif root.val == val:
        print(root)
        return root   
    else:
        if val > root.val :
            print("root",root.val)
            # move to the right side with new root as one on the right
            return self.search(root.right,val)
        else:
            print("root",root.left)
            return self.search(root.left,val)          



print(search([4,2,7,1,3],2))    