from collections import deque

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):

        slidingQ = deque()
        for idx in range(B):
            while slidingQ and A[slidingQ[-1]]<= A[idx]:
                slidingQ.pop()
            slidingQ.append(idx)
        
        maxList = list()

        for idx in range(B,len(A)):
            maxList.append(A[slidingQ[0]])
            while slidingQ and slidingQ[0]<= idx - B:
                slidingQ.popleft()
            while slidingQ and A[slidingQ[-1]]<=A[idx]:
                slidingQ.pop()
            slidingQ.append(idx)
        
        maxList.append(A[slidingQ[0]])
        return maxList

A = (1,3,3,-1,-2,4,1,5)
s = Solution()
B = s.slidingMaximum(A,3)
print(B)