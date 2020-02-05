# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sRecur(self, A, left, right):
        if left > right:
            return None
        mid = left + (right-left)/2
        leftRoot = self.sRecur(A, left, mid-1)
        rightRoot = self.sRecur(A, mid+1, right)
        node = TreeNode(A[mid])
        node.left = leftRoot
        node.right = rightRoot
        return node

    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        if A == None:
            return None
        return self.sRecur(A, 0, len(A)-1)
