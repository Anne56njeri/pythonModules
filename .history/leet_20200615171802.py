# how a binary tree works is the smaller numbers are 
# on the left then the bigger ones are on the right 
# returning the node also returns the children which is what 
# you want 

def search(root,val):
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


print(search([4,2,1,7,3],2))    