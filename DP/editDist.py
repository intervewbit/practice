class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        m = len(A)
        n = len(B)
        if m == 0 and n == 0:
            return 0
        elif m == 0:
            return n
        elif n == 0:
            return m

        # (m+1) x (n+1) matrix for dp
        ed = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(m+1):
            ed[0][i] = i
        for j in range(n+1):
            ed[j][0] = j
        for r in range(1, n+1):
            for c in range(1, m+1):
                if A[c-1] == B[r-1]:
                    ed[r][c] = ed[r-1][c-1]
                else:
                    ed[r][c] = min(ed[r-1][c] + 1, ed[r]
                                   [c-1] + 1, ed[r-1][c-1]+1)
        return ed[n][m]


S = Solution()
A = "Anshuman"
B = "Antihuman"
print(S.minDistance(A, B))
