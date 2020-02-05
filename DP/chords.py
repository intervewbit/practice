class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        # A is the num of pairs
        mem = []
        mem.append(1)
        mem.append(1)
        mem.append(2)
        for c in range(3,A+1):
            left = 0
            right = c - 1
            curr = 0
            mem.append(0)
            while right>=0:
                curr += mem[left] * mem[right]
                left += 1
                right -= 1
            mem[c] = curr
        return mem[A] % 1000000007

A = 4
print(Solution().chordCnt(A))

