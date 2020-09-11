# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# base case if root is empty count = 0 
class Solution:
    def countNodes(self, root: TreeNode) -> int:
#         base case
        if root ==   None:
            return 0
        left = root 
        right = root
        # pointers left and right 
        h_l = 0 
        h_r = 0 
        while left != None:
            h_l +=1 
            left = left.left 
        while right != None:
            h_l +=1 
            right = right.right 
        if h_l == h_r:
            return (2**h_l ) -1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)