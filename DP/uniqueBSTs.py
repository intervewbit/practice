class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        totWith = [0 for _ in range(A+1)]
        totWith[0] = 0
        totWith[1] = 1

        for i in range(2, A+1):
            s = 0
            for root in range(1, i+1):
                left = max(totWith[root - 1], 1)
                right = max(totWith[i-root], 1)
                s += left * right
            totWith[i] = s
        return totWith[A]


S = Solution()
print(S.numTrees(5))
