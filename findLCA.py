# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x,L,R):
        self.val = x
        self.left = L
        self.right = R

class Solution:
    # @eturn a tuple bool1, bool2, node
    def exists(self, node, v1, v2):
        if node == None:
            return False, False, None
        
        b1,b2,n = False,False,None
        if node.val == v1:
            b1 = True
        if node.val == v2:
            b2 = True
        
        leftB1,leftB2,leftN = self.exists(node.left,v1,v2)
        # if found both with node and LEFT
        if (b1 or leftB1) and (b2 or leftB2):
            if b1 or b2:
                return True, True, node
            else:
                return True,True,leftN
        # if found only ONE value with node and LEFT
        elif (b1 or leftB1) or (b2 or leftB2):
            # search right Node 
            rightB1, rightB2, rightN = self.exists(node.right, v1, v2)
            # is the other found? Since there are no dupes
            if rightB1 or rightB2:
                # ONE in LEFT other in RIGHT, node is the root
                return True,True,node
            else:
                # Not Found
                return b1 or leftB1 or rightB1, b2 or leftB2 or rightB2, None
        else:
            # Not Found any in Node and Left
            return self.exists(node.right, v1,v2)

        
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        b1,b2,n = self.exists(A,B,C)
        if n != None:
            return n.val
        else:
            return -1

A = TreeNode(1,None,None)
R = Solution().lca(A,1,1)
print(R)