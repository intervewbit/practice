class Solution:
    def isValidQuad(self, a, b, c, d, result):
        if a < b and c < d and a < c and b != c and b != d:
            if len(result) <= 0 or result > [a, b, c, d]:
                return True
        return False

    def augResult(self, result, a, b, c, d):
        if self.isValidQuad(a, b, c, d, result):
            result[:] = [a, b, c, d]

    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        result = []
        sumDic = {}
        if len(A) <= 3:
            return result

        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                s = A[i] + A[j]
                a, b = sumDic.get(s, (-1, -1))
                if a == -1:
                    sumDic[s] = (i, j)
                else:
                    self.augResult(result, a, b, i, j)

        return result


A = [3, 4, 7, 1, 2, 9, 8]
r = Solution().equal(A)
print(r)
