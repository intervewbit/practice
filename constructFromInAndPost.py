# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructRecur(self, postOrder=[], inOrder=[]):
        if postOrder is None or len(postOrder) == 0:
            return None
        # root node is the last in post order
        root = postOrder[-1]
        idx = inOrder.index(root)
        leftLen = idx

        # create the root node and attach to left and right
        rootNode = TreeNode(root)
        rootNode.left = self.constructRecur(
            postOrder[:leftLen], inOrder[:idx])
        rootNode.right = self.constructRecur(
            postOrder[leftLen:-1], inOrder[idx+1:])

        return rootNode

    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        return self.constructRecur(B, A)


Post = [1, 2, 3]
In = [1, 3, 2]
R = Solution().buildTree(Post, In)
