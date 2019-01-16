class Solution:
    def getMinMax(self, A, start, end):
        if start < 0 or end >= len(A):
            return -1, -1
        minimum, maximum = A[start], A[start]
        for index in range(start+1, end+1):
            if minimum > A[index]:
                minimum = A[index]
            elif maximum < A[index]:
                maximum = A[index]
        return minimum, maximum

    def mergeWithLeft(self, A, leftStart, leftEnd, islandMin, islandMax, islandStart):
        if leftEnd == -1:
            return islandStart, islandMax
        newStart = leftStart
        while newStart >= 0 and newStart < islandStart and A[newStart] <= islandMin:
            newStart = newStart+1
        if newStart < islandStart and A[leftEnd] > islandMax:
            islandMax = A[leftEnd]
        return newStart, islandMax

    def mergeWithRight(self, A, rightStart, rightEnd, islandMin, islandMax, islandEnd):
        if rightStart == -1 or rightStart>=len(A):
            return islandEnd
        newEnd = rightEnd
        while A[newEnd] >= islandMax and newEnd > islandEnd:
            newEnd = newEnd - 1
        return newEnd

    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        if len(A) <= 1:
            return [-1]

        leftStart, leftEnd = 0, 0
        rightStart, rightEnd = len(A)-1, len(A)-1

        # fix left island
        prev = A[leftStart]
        for index in range(1, len(A)):
            if A[index] >= prev:
                leftEnd = index
                prev = A[index]
            else:
                break

        # fix right island
        prev = A[len(A)-1]
        for index in range(len(A)-2, -1, -1):
            if A[index] <= prev:
                rightStart = index
                prev = A[index]
            else:
                break

        if leftEnd == len(A) - 1:
            return [-1]
        
        if rightStart-leftEnd==1:
            rightStart= rightStart+1

        islandStart, islandEnd = leftEnd+1, rightStart-1
        
        islandMin, islandMax = self.getMinMax(A, islandStart, islandEnd)
        islandStart, islandMax = self.mergeWithLeft(
            A, leftStart, leftEnd, islandMin, islandMax, islandStart)
        islandEnd = self.mergeWithRight(
            A, rightStart, rightEnd, islandMin, islandMax, islandEnd)
        return [islandStart, islandEnd]


A = [1,20,30,40,39,38,19,28,18,10,11,12,110,140]
# A = [16, 15, 16, 20]
r = Solution()
start, end = r.subUnsort(A)
print("(%d,%d)" % (start,end))
