class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, N, S):
        arr = [[0 for j in range(S + 1)] for i in range(N + 1)]
        arr[0][0] = 1
        for n in range(1, N+1):
            for s in range(S+1):
                if s > 9*n:
                    break
                for digit in range(10):
                    if s - digit >= 0:
                        arr[n][s] += arr[n-1][s-digit]
                    else:
                        break
        return (arr[N][S] - arr[N-1][S]) % 1000000007


S = Solution()
A = 3
B = 3
print(S.solve(A, B))
