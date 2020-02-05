class Solution:
    # @param A : tuple of integers
    # @return an integer
    @staticmethod
    def solve(a):
        if not a:
            return 0
        elif len(a) == 1:
            return 1
        pos_map = {}
        length = len(a)
        dp = [[2 for x in range(length)] for y in range(length)]
        max_len = 2
        for i in range(len(a) - 1):
            if i > 0:
                pos_map[a[i - 1]] = i - 1
            for j in range(i + 1, len(a)):
                dp[i][j] = 2
                x = 2 * a[i] - a[j]
                if x in pos_map:
                    dp[i][j] = max(dp[i][j], dp[pos_map[x]][i] + 1)
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
        return max_len


S = Solution()
# A = [100, 10, 8, 300, 6, 1, 4, 2]
A = [100]
B = S.solve(A)
print(B)
