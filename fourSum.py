class Solution:
    def findNums(self, A, start, end, B):
        ret = []
        while start < end:
            s = A[start] + A[end]
            if s > B:
                end -= 1
            elif s < B:
                start += 1
            else:
                ret.append((start, end))
                start += 1
                while start < end and A[start] == A[start-1]:
                    start += 1
        return ret

    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        result = []
        sA = sorted(A)
        if len(sA) >= 4:
            i = 0            
            while i<len(A)-3:
                j = i+1
                while j < len(A)-2:
                    l = self.findNums(sA, j+1, len(sA)-1, B - sA[i] - sA[j])
                    for s, e in l:
                        partSol = [sA[i], sA[j], sA[s], sA[e]]
                        result.append(partSol)
                    j += 1
                    while (j < len(A) - 2) and (sA[j] == sA[j-1]):
                        j += 1
                i += 1
                while (i<len(A)-3) and (sA[i]== sA[i-1]):
                    i+=1                
            
        return result


s = Solution()
A = [1, 0, -1, 0, -2, 2]
r = s.fourSum(A, 0)

print(r)
