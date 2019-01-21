from heapq import *


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        if len(B) <= 0:
            return 0

        maxHeap = [-x for x in B]
        heapify(maxHeap)
        chocs = 0
        for t in range(A):
            val = heappop(maxHeap)
            val = abs(val)
            chocs += val
            val //= 2
            if val > 0:
                heappush(maxHeap, -val)
            if len(maxHeap) <= 0:
                break
        return chocs


A = 2
B = [4, 2, 18,29]
r = Solution().nchoc(A, B)
print(r)
