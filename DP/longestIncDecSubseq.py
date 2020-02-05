class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        lis = [1 for x in A]
        lds = [0 for x in A]

        if not A:
            return 0

        for i in range(1,len(A)):
            for j in range(0,i):
                if A[i]>A[j]:
                    if lis[i]<lis[j]+1:
                        lis[i] = lis[j] + 1                
        
        for i in range(len(A)-2,-1,-1):
            for j in range(i+1,len(A)):
                if A[i]>A[j]:
                    if lds[i] < lds[j] + 1:
                        lds[i] = lds[j] + 1
        
        currMax = 0
        for i,j in zip(lis,lds):
            if i+j>currMax:
                currMax = i+j
        return currMax


A = [ 7, 6, 8, 10, 2, 5, 12, 30, 31, 20, 22, 18 ]
print(Solution().longestSubsequenceLength(A))