class Solution:
    def getSubsetsStartingAt(self, sols, curr, A, currIdx):
        if currIdx >= len(A):
            return

        # include current
        elem = A[currIdx]
        curr.append(elem)
        # only current
        sols.append(curr[:])

        while currIdx < len(A)-1:
            currIdx += 1
            self.getSubsetsStartingAt(sols, curr, A, currIdx)
            while currIdx < len(A)-1 and A[currIdx+1] == A[currIdx]:
                currIdx += 1
        curr.pop()

    # @param A : list of integers
    # @return a list of list of integers

    def subsetsWithDup(self, A):
        result = [[]]
        prev = None
        B = sorted(A)
        for idx in range(len(B)):
            if prev and B[idx]==prev:
                continue
            self.getSubsetsStartingAt(result, [],B, idx)
            prev = B[idx]
        return result

s = Solution()
A = [1,3,2,2]
R = s.subsetsWithDup(A)
print(R)
