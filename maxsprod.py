class Solution:
    def __init__(self):
        pass

    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        lsv = [0 for x in A]
        rsv = [0 for x in A]
        for index in range(1, len(A)):
            if A[index-1] > A[index]:
                lsv[index] = index-1
            else:
                startIndex = index-1
                while startIndex > 0:
                    startIndex = lsv[startIndex]
                    if startIndex > 0 and A[startIndex] > A[index]:
                        lsv[index] = startIndex
                        break
        
        for index in range(len(A)-2, -1, -1):
            if A[index+1] > A[index]:
                rsv[index] = index+1
            else:
                startIndex = index+1
                while startIndex>0 and startIndex < len(A) - 1:
                    startIndex = rsv[startIndex]
                    if (startIndex < len(A) - 1) and A[startIndex] > A[index]:
                        rsv[index] = startIndex
                        break

        msv = [x*y for x, y in zip(lsv, rsv)]
        maximum = 0
        for val in msv:
            if maximum < val:
                maximum = val
        return maximum % 1000000007


A = [6, 5, 4, 9, 9, 6, 5, 4, 5, 9, 9]
r = Solution()
maxs = r.maxSpecialProduct(A)

print("maxs = %d" % maxs)
