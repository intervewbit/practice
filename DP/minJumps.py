class Solution:
    def maxRangeIndex(self, start, end, A):
        maxRange = 0
        maxRangeIndex = start
        maxIndex = len(A) - 1
        for i in range(start, end+1):
            if i >= maxIndex:
                return maxIndex
            if i+A[i] > maxRange:
                maxRange = i+A[i]
                maxRangeIndex = i
        return maxRangeIndex

    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        maxIndex = len(A) - 1
        if len(A) <= 1:
            return 0

        i = 0
        jumps = 0
        while i < maxIndex:
            nextIndex = self.maxRangeIndex(i, i+A[i], A)
            if nextIndex > i:
                jumps = jumps + 1
                i = nextIndex
            else:
                return -1
        return jumps


S = Solution()
#A = [4, 5, 5, 1, 0, 4, 7, 7]
#A = [5, 1, 0, 1, 4, 0]
A = [1, 2, 1, 3, 0, 0, 1, 4, 1, 0, 3]

B = S.jump(A)
print(B)
