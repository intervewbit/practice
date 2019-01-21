from heapq import * 

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        minHeap = []
        n = len(B)

        for a in A:
            for b in B:
                s = a + b
                if len(minHeap) < n:
                    heappush(minHeap, s)
                elif minHeap[0] < s:
                    heappop(minHeap)
                    heappush(minHeap, s)

        result = []
        for i in range(len(minHeap)):
            result.append(heappop(minHeap))

        return list(reversed(result))


A = [1, 4, 3, 2]
B = [2, 5, 1, 6]
r = Solution().solve(A, B)
print(r)
