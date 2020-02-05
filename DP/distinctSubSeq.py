class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct(self, A, B):
        if len(B)>len(A):
            return 0
        if len(B) == len(A):
            if B == A:
                return 1
            else:
                return 0
        
        m = len(A) + 1
        n = len(B) + 1
        s = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            s[0][i] = 1
        for r in range(1, n):
            for c in range(m):
                if c == 0:
                    s[r][c] = 0
                    continue
                if A[c-1] == B[r-1]:
                    s[r][c] = s[r-1][c-1] + s[r][c-1]
                else:
                    s[r][c] = s[r][c-1]
        return s[n-1][m-1]

S = Solution()
s = "RARABBBIT"
t = "RABBIT"
print(S.numDistinct(s,t))
