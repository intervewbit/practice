from math import log2, floor, factorial


class Solution:
    def comb(self,N,c):
        num = 1
        for i in range(c+1,N+1):
            num*=i
        return num//factorial(N-c)

    def getL(self, N):
        # height of the heap
        h = floor(log2(N))
        internalNodes = 2**h - 1
        # maxNodes in last level
        m = 2**h
        # actual nodes in last
        p = N - internalNodes
        if p >= m//2:
            return 2**h - 1
        else:
            return (2**h - 1 - (m//2 - p))

    def solveForN(self, N):
        if N <= 2:
            return 1
        elif N == 3:
            return 2
        
        L = self.getL(N)
        R = N - L - 1
        return self.solveForN(L)*self.solveForN(R)*self.comb(N-1,L)


    # @param A : integer
    # @return an integer
    def solve(self, A):
        return floor(self.solveForN(A) % 1000000007)


print(Solution().solve(100))
       
