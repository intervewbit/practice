# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    def kthRecur(self,A,B):
        if A == None:
            return 0,None
        
        leftCount,res = self.kthRecur(A.left,B)
        if leftCount>=B:
            return B+1,res
        elif leftCount==B-1:
            return B+1,A.val

        rightCount,res = self.kthRecur(A.right,B-leftCount-1)
        return leftCount+rightCount+1,res
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
    def kthsmallest(self, A, B):
        count,res = self.kthRecur(A,B)
        return res