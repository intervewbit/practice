class Solution:
    def getMinSudNum(self, row, col):
        return (3*(row//3) + col//3)
    # @param A : tuple of strings
    # @return an integer

    def isValidSudoku(self, A):
        colDic = {}
        miniDic = {}
        for row, s in enumerate(A):
            rowSet = set()
            for col,ch in enumerate(s):
                if ch == '.':
                    continue
                if ch in rowSet:
                    return 0
                rowSet.add(ch)
                colSet = None
                if col in colDic:
                    colSet = colDic[col]
                else:
                    colSet = set()
                if ch in colSet:
                    return 0
                colSet.add(ch)
                colDic[col] = colSet
                miniS = self.getMinSudNum(row,col)
                miniSet = None
                if miniS in miniDic:
                    miniSet = miniDic[miniS]
                else:
                    miniSet = set()
                if ch in miniSet:
                    return 0
                miniSet.add(ch)
                miniDic[miniS] = miniSet
        return 1

A = [ "....5..1.", ".4.3.....", ".....3..1", "8......2.", "..2.7....", ".15......", ".....2...", ".2.9.....", "..4......" ]
s = Solution()
r = s.isValidSudoku(A)
print(r)