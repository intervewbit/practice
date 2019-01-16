class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        R = len(A)
        if R <= 0:
            return []

        C = len(A[0])

        # iter over columns
        res = []
        for c in range(0, C):
            startingC = c
            startingR = 0
            currentDiag = []
            while startingC >= 0 and startingR < len(A):
                currentDiag.append(A[startingR][startingC])
                startingC = startingC - 1
                startingR = startingR + 1
            res.append(currentDiag)

        for r in range(1, R):
            startingC = C - 1
            startingR = r
            currentDiag = []
            while startingR < R and startingC >= 0:
                currentDiag.append(A[startingR][startingC])
                startingR = startingR + 1
                startingC = startingC - 1
            res.append(currentDiag)

        return res


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = Solution().diagonal(A)
print(B)
