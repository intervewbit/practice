class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        if len(A) <= 0:
            return 0
        leh = [1 for _ in A]
        mUntilNow = 1
        for i in range(1, len(A)):
            mLen = 1
            for j in range(i):
                if A[j] < A[i]:
                    mLen = max(mLen, leh[j] + 1)
            leh[i] = mLen
            mUntilNow = max(mUntilNow,mLen)
            
        return mUntilNow
