import heapq
import math


class Solution:

    def buildSegTree(self, start, end, node, tree=[]):
        if start == end:
            tree[node] = [(start, end), 1]
            return 1

        mid = start + (end-start)//2
        emptyNodes = self.buildSegTree(
            start, mid, node*2+1, tree) + self.buildSegTree(mid+1, end, node*2+2, tree)
        tree[node] = [(start, end), emptyNodes]
        return tree[node][1]

    def findAndUpdateIdx(self, start, end, node, tree, result, value, inFront):
        if start == end:
            result[start] = value
            tree[node] = [(start, end), 0]
            return 0

        leftCount = tree[node*2+1][1]
        mid = start + (end-start)//2
        if leftCount > inFront:
            self.findAndUpdateIdx(start, mid, node*2+1,
                                  tree, result, value, inFront)
        else:
            self.findAndUpdateIdx(mid+1, end, node*2+2,
                                  tree, result, value, inFront-leftCount)
        tree[node] = [tree[node][0], tree[node][1]-1]

    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, A, B):
        h = list(zip(A, B))
        heapq.heapify(h)

        result = [-1 for x in A]
        size = 2*(2**math.ceil(math.log2(len(A))))
        tree = [[(-1,-1),-1] for x in range(size)]
        self.buildSegTree(0, len(A)-1, 0, tree)
        while h:
            lowest = heapq.heappop(h)
            self.findAndUpdateIdx(0,len(A)-1,0,tree,result,lowest[0],lowest[1])
        return result


A = [5, 3, 2, 6, 1, 4]
B = [0, 1, 2, 0, 3, 0]

print(Solution().order(A, B))
