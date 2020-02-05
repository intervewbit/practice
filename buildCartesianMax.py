# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    def addToLeftMost(self, root, nodeToAdd):
        if root == None:
            return nodeToAdd
        else:
            curr = root
            prev = None
            while curr and curr.left and curr.val > nodeToAdd.val:
                prev = curr
                curr = curr.left
            if curr.val > nodeToAdd.val:
                curr.left = nodeToAdd
            else:
                assert prev != None
                prev.left = nodeToAdd
                nodeToAdd.right = curr
        return root

    def addAsParent(self, root, nodeToAdd):
        nodeToAdd.right = root
        return nodeToAdd

    # returns the root of the Cartesian tree
    def buildRecur(self, A):
        currRoot = None
        for idx in range(len(A)-1,-1,-1):
            newNode = TreeNode(A[idx])
            if currRoot == None:
                currRoot = newNode
            elif newNode.val < currRoot.val:
                currRoot = self.addToLeftMost(currRoot,newNode)
            else:
                currRoot = self.addAsParent(currRoot, newNode)
        return currRoot

    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        if len(A) <= 0:
            return None
        return self.buildRecur(A)
