class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A)<=1:
            return 0
        maxUntilNow = 0
        minL = [-1 for x in A]
        minL[0] = A[0]
        for i in range(1,len(A)):
            if A[i]<minL[i-1]:
                minL[i] = A[i]
            else:
                minL[i] = minL[i-1]
            profit = A[i] - minL[i]
            if profit>maxUntilNow:
                maxUntilNow = profit
        return maxUntilNow

A = [3,2,4,9,1,6,2,10]
print(Solution().maxProfit(A))
