# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    def leftMostChildOfNextNode(self, node):
        if node == None:
            return None
        start = node.next
        while start != None:
            if start.left != None:
                return start.left
            elif start.right != None:
                return start.right
            else:
                start = start.next
        return None
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None:
            return 
        
        root.next = None
        currLvl = root
        while currLvl != None:
            curr = currLvl
            while curr != None:
                if curr.left:
                    if curr.right:
                        curr.left.next = curr.right
                    else:
                        curr.left.next = self.leftMostChildOfNextNode(curr)
                if curr.right:
                    curr.right.next = self.leftMostChildOfNextNode(curr)
                curr = curr.next
            if currLvl.left:
                currLvl = currLvl.left
            elif currLvl.right:
                currLvl = currLvl.right
            else:
                currLvl = self.leftMostChildOfNextNode(currLvl)
