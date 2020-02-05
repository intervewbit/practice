class Solution:
    def getSumWithPrev(self, r, c, A):
        if r == 0:
            return 0, 0
        left = None
        right = None
        if c > 0:
            left = A[r][c] + A[r-1][c-1]
        if c < len(A[r]) - 1:
            right = A[r][c] + A[r-1][c]
        return left, right

    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        if not A:
            return 0
        sums = A[:]
        minSum = A[0][0]
        for r in range(1, len(A)):
            minForRow = None
            for c in range(len(A[r])):
                left, right = self.getSumWithPrev(r, c, sums)
                minHere = left if right is None else (
                    right if left is None else (min(left, right)))
                minForRow = min(
                    minForRow if minForRow is not None else minHere, minHere)
                sums[r][c] = minHere
            minSum = minForRow
        return minSum


S = Solution()
""" A = [
    [0],
    [0,5],
    [6, 7,8],
    [0,6,5,7],
    [3,4,3,0,4],
    [8,7,5,9,5,3],
    [2,7,3,9,7,7,9],
    [5,3,3,3,8,5,8,9]
] """
A = [
    [0],
    [0, 9]
]
print(S.minimumTotal(A))
