# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:    
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        result = []
        L2RStack = []
        R2LStack = []
        # from left to right : add L then R in stack else R then R
        isL2R = True
        if A is None:
            return result
        L2RStack.append(A)
        currStack= L2RStack
        while currStack:
            nxtStack = L2RStack
            if isL2R:
                nxtStack = R2LStack
            # take elements out of currStack and pop nxtStack
            currList = []
            while currStack:
                currNode = currStack.pop()
                if currNode is None:continue
                if isL2R:
                    nxtStack.append(currNode.left)
                    nxtStack.append(currNode.right)
                else:                    
                    nxtStack.append(currNode.right)
                    nxtStack.append(currNode.left)
                currList.append(currNode.val)
            if len(currList)>0:
                result.append(currList)
            currStack = nxtStack
            isL2R = not isL2R
        return result
