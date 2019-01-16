class Solution:
    def combinations(self, prefix, A, k, res):
        if not A or k == 0:
            part = [x for x in prefix]
            res.append(part)
            return res
        elif len(A) == k:            
            part = [x for x in prefix]
            part.extend(A[0:k])
            res.append(part)
            return res

        # with
        prefix.append(A[0])
        self.combinations(prefix, A[1:], k-1, res)
        prefix.pop()
        self.combinations(prefix, A[1:], k, res)
        return res

    # @param A : integer
    # @param B : integer
    # @return a list of list of integers

    def combine(self, A, B):
        R = range(1, A+1)
        if len(R)<B:
            return []
        result = self.combinations([], R, B, list())
        return result