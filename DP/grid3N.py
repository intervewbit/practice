class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        threes = 24
        twos = 12

        # nextThrees = 11* threes + 10* twos
        # nextTwos = 7*twos + 5* threes
        for i in range(1, A):
            nextThrees = 11*threes + 10*twos
            nextTwos = 7*twos + 5*threes
            twos, threes = nextTwos, nextThrees

        return (twos + threes) % 1000000007


s = Solution()
print(s.solve(2))
