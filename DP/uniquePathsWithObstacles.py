class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        if not A or A[0][0] == 1:
            return 0

        m = len(A)
        n = len(A[0])
        uniquePaths = [[0 for _ in range(n)] for _ in range(m)]
        uniquePaths[0][0] = 1
        for c in range(1, n):
            if A[0][c] == 1:
                break
            uniquePaths[0][c] = 1 if A[0][c-1] == 0 else 0
        for r in range(1, m):
            if A[r][0] == 1:
                break
            uniquePaths[r][0] = 1 if A[r-1][0] == 0 else 0
        for r in range(1, m):
            for c in range(1, n):
                if A[r][c] == 1:
                    continue
                uniquePaths[r][c] = uniquePaths[r-1][c] + uniquePaths[r][c-1]
        return uniquePaths[m-1][n-1]


S = Solution()
""" A = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
] """
A = [
    [0,0,1]
]
B = S.uniquePathsWithObstacles(A)
print(B)
