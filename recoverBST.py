# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    def updateInvalids(self, firstInvalid, secondInvalid, prev, curr):
        fI = firstInvalid
        sI = secondInvalid
        if firstInvalid == None:
            if prev == None or prev.val < curr.val:
                fi = None
            elif prev.val > curr.val:
                fI = prev

        if fI != None and secondInvalid == None:
            if curr.val < prev.val:
                sI = curr
            else:
                sI = None
        elif secondInvalid != None:
            if curr.val < prev.val and curr.val < secondInvalid.val:
                sI = curr
        return fI, sI

    # returns a tuple with the values of replaced nodes
    # the first has property that it is < next
    # the second number is < prev
    def morrisTraversal(self, A):
        prev = None
        curr = A
        firstInvalid = None
        secondInvalid = None

        while curr:
            firstInvalid, secondInvalid = self.updateInvalids(
                firstInvalid, secondInvalid, prev, curr)
            # if firstInvalid != None and secondInvalid != None:
            #    return firstInvalid,secondInvalid
            # should not pre-empt as we need to correct the tree
            if curr.left == None:
                # visit point
                prev = curr
                curr = curr.right
            else:
                # find the rightmost (or last to be processed node in subtree at curr.left)
                start = curr.left
                while start and start.right and start.right != curr:
                    start = start.right
                if start.right == None:
                    start.right = curr  # loopback here
                    curr = curr.left
                    # this is not the visit point
                else:
                    # visited the loopback
                    start.right = None
                    # visit point
                    prev = curr
                    curr = curr.right

        return firstInvalid, secondInvalid

    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        f, s = self.morrisTraversal(A)
        return [s.val, f.val]
