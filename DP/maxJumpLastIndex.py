class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        nxtMinReq = 1
        canReach = True
        for i in range(len(A)-2,-1,-1):
            if A[i] < nxtMinReq:
                nxtMinReq = nxtMinReq + 1
                canReach = False
            else:
                nxtMinReq = 1
                canReach = True
        return 1 if canReach else 0

S = Solution()
#A = [2,3,1,1,4]
A = [4,2,1,0,4]
B = S.canJump(A)
print('Can Jump ', B)
        