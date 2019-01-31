# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    def invertRecur(self,A):
        if A == None:
            return
        L = A.left
        R = A.right
        self.invertRecur(A.left)
        self.invertRecur(A.right)
        A.left = R
        A.right = L
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        self.invertRecur(A)
        return A
