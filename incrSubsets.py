class Solution:

    # gets subsets 
    def getSubset(self,A):
        if len(A)==1:
            return [[A[0]]]
        
        start = A[0]
        tail = A[1:]
        trailing = self.getSubset(tail)
        res = [[start]]
        for partSet in trailing:
            withStart = [start]
            withStart.extend(partSet)
            res.append(withStart)
        res.extend(trailing)
        return res

    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        B = sorted(A)
        res = [[]]
        if not B:
            return res

        res1 = self.getSubset(B)
        res.extend(res1)

        return res

s = Solution()
A = [4,3,1,2]
B = s.subsets(A)
print("sets are ", B)