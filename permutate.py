class Solution:
    def perm(self, prefix, A, idx, sols):
        if idx >= len(A):
            sols.append(prefix[:])

        # starting with idx perm rem idx+1...len
        for i in range(idx, len(A)):
            # swap i and idx
            A[i], A[idx] = A[idx], A[i]
            prefix.append(A[idx])
            self.perm(prefix, A, idx+1, sols)
            prefix.pop()
            A[i], A[idx] = A[idx], A[i]

    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        R = []
        self.perm([], A, 0, R)
        return R


s = Solution()
A = [1, 2, 3]
R = s.permute(A)
print(R)
