class Solution:
    def uniqueCSum(self, S, A, curr, result, idx):
        if S == 0:
            result.append(curr[:])
            return
        if S < 0 or idx >= len(A):
            return

        minimum = A[idx]
        S -= minimum
        curr.append(minimum)
        self.uniqueCSum(S, A, curr, result, idx+1)
        while idx < len(A) - 1 and A[idx] == A[idx+1]:
            idx += 1
        curr.pop()
        S += minimum
        if idx<len(A)-1 and S<A[idx+1]:
            return
        self.uniqueCSum(S, A, curr, result, idx+1)

    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers

    def combinationSum(self, A, B):
        nList = sorted(A)
        result = []
        self.uniqueCSum(B, nList, [], result, 0)
        return result


s = Solution()
A = [1, 3, 1, 4, 2, 2,18,16,8,7,18,19]
B = 19
r = s.combinationSum(A, B)
print(r)
