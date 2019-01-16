class Solution:
    def getRank(self, num, A):
        count = 0
        equals = 0
        for n in A:
            if n <= num:
                count += 1
            if n == num:
                equals += 1
        return count, equals

    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        if B > len(A):
            return -1

        low = min(A)
        high = max(A)

        while low <= high:
            mid = low + (high-low)//2
            rank, equals = self.getRank(mid, A)
            if equals > 0:
                if rank == B:
                    return mid
                elif equals > 1 and abs(rank-B) < equals:
                    return mid
            if rank < B:
                low = mid+1
            elif rank >= B:
                high = mid-1

        return -1


s = Solution()
A = [12, 4, 5, 10, 10, 10, 10, 1, 10]
B = 4
n = s.kthsmallest(A, B)

print("%d smallest is %d" % (B, n))
