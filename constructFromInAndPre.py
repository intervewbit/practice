# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructRecur(self, preOrder=[], inOrder=[]):
        if preOrder is None or len(preOrder) == 0:
            return None
        # root node is the first in pre order
        root = preOrder[0]
        idx = inOrder.index(root)
        leftLen = idx

        # create the root node and attach to left and right
        rootNode = TreeNode(root)
        rootNode.left = self.constructRecur(preOrder[1:leftLen+1], inOrder[:idx])
        rootNode.right = self.constructRecur(preOrder[leftLen+1:], inOrder[idx+1:])

        return rootNode

    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        return self.constructRecur(A,B)        
        
