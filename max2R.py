class Solution:
    def getMaxGap(self, A, index, max2Right):
        val = A[index]
        gap = -1
        nxt = max2Right[index]
        while nxt>-1 and A[nxt] >= val:
            gap = nxt - index
            nxt = max2Right[nxt]
        return gap
        
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        maxGap = -1
        # keep a max2Right
        max2Right = [-1 for x in A]
        for index in range(len(A)-2,-1,-1):
            nxt = index+1
            if max2Right[index+1] != -1 and A[nxt] <= A[max2Right[index+1]]:
                nxt = max2Right[index+1]
            max2Right[index] = nxt
        
        for index in range(len(A)):
            gap = self.getMaxGap(A, index, max2Right)
            if gap > maxGap:
                maxGap = gap
        
        return maxGap

A = ( 1, 10)
r = Solution()
maxGap = r.maximumGap(A)