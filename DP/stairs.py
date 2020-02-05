class Solution:
    def cRec(self,n,nSteps={}):
        if n in nSteps:
            return nSteps[n]
        nSteps[n] = self.cRec(n-1,nSteps) + self.cRec(n-2,nSteps)
        return nSteps[n]

    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        nSteps = {}
        nSteps[0] = 0
        nSteps[1] = 1
        nSteps[2] = 2

        return self.cRec(A,nSteps)

A = 8
print(Solution().climbStairs(A))


