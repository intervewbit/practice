class Solution:
    def seqExists(self, key, seqMap, end, j):
        for i in range(end):
            if key in seqMap[i] and j != seqMap[i][key][1]:
                return True
        return False

    # @param A : string
    # @return an integer
    def anytwo(self, A):
        if len(A) <= 2:
            return 0
        # enough to find subseq with length 2
        seqMap = [{} for _ in range(len(A)-1)]
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                seq = A[i], A[j]
                if seq not in seqMap[i]:
                    seqMap[i][seq] = i,j
                if self.seqExists(seq, seqMap, i, j):
                    return 1
        return 0


S = Solution()
A = "abba"
print(S.anytwo(A))
