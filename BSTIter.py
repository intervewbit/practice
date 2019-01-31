# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.stack = []
        self.nextProbeAt = self.root        

    def __setupnext__(self, node):
        curr = node
        if curr:
            self.stack.append(curr)
        while curr and curr.left:
            self.stack.append(curr.left)
            curr = curr.left
        return curr

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if len(self.stack) <= 0:
            if self.nextProbeAt == None:
                return False
            else:
                self.__setupnext__(self.nextProbeAt)
                self.nextProbeAt = None
                return len(self.stack)>0
        else:
            if self.nextProbeAt:
                self.__setupnext__(self.nextProbeAt)
                self.nextProbeAt = None
            return True
        
    # @return an integer, the next smallest number
    def next(self):
        next = self.stack.pop()
        self.nextProbeAt = next.right
        return next.val        

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
