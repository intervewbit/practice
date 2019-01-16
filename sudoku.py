class Solution:
    def getSudoSetNum(self, row, col):
        return (3*(row//3) + col//3)

    def getSets(self, A, rowDic={}, colDic={}, sudoSets={}):
        for rowNum, rowChars in enumerate(A):
            # rowSet = {x for x in rowChars if x != '.'}
            rowSet = set()
            for c in rowChars:
                if c != '.':
                    if c in rowSet:
                        return False
                    rowSet.add(c)
            rowDic[rowNum] = rowSet
            for colNum, colChars in enumerate(rowChars):
                colSet = colDic.get(colNum, set())
                sNum = self.getSudoSetNum(rowNum, colNum)
                sudoSets[sNum] = sudoSets.get(sNum,set())
                if colChars in sudoSets[sNum]:
                    return False                
                if colChars != '.':
                    if colChars in colSet:
                        return False
                    if colChars in sudoSets[sNum]:
                        return False
                    sudoSets[sNum].add(colChars)
                    colSet.add(colChars)
                    colDic[colNum] = colSet
        return True

    def isCharTaken(self, row, col, ch, rowDic={}, colDic={}, sudoSets={}):
        if (row in rowDic and ch in rowDic[row]) or (col in colDic and ch in colDic[col]):
            return True
        sNum = self.getSudoSetNum(row, col)
        if sNum in sudoSets and ch in sudoSets[sNum]:
            return True
        return False

    def getNextRC(self, row, col):
        r = row
        c = col
        c += 1
        if c > 8:
            r += 1
            c = 0
        return r, c

    def useChAtRC(self, row, col, A, ch, useFlag, rowDic={}, colDic={}, sudoSets={}):
        sNum = self.getSudoSetNum(row, col)
        if useFlag:            
            rowDic.setdefault(row,set()).add(ch)
            colDic.setdefault(col,set()).add(ch)
            A[row][col] = ch
            sudoSets.setdefault(sNum,set()).add(ch)
        else:
            rowDic[row].remove(ch)
            colDic[col].remove(ch)
            A[row][col] = '.'
            sudoSets[sNum].remove(ch)

    def tryFixSudo(self, row, col, A, rowDic={}, colDic={}, sudoSets={}):
        if row > 8 :
            return True

        rNxt, cNxt = self.getNextRC(row, col)
        if A[row][col] == '.':
            for chOrd in range(ord('1'), ord('9')+1):
                ch = chr(chOrd)
                if self.isCharTaken(row, col, ch, rowDic, colDic, sudoSets):
                    continue
                self.useChAtRC(row, col, A, ch, True, rowDic, colDic, sudoSets)
                if self.tryFixSudo(rNxt, cNxt, A, rowDic, colDic, sudoSets):
                    return True
                self.useChAtRC(row, col, A, ch, False,
                               rowDic, colDic, sudoSets)
        else:
            if self.tryFixSudo(rNxt, cNxt, A, rowDic, colDic, sudoSets):
                return True
        #print("Backtracking at r,c",row,col)
        return False

    # @param A : list of list of chars like [.23...18.]
    # @return nothing
    def solveSudoku(self, A):
        rowDic = {}
        colDic = {}
        sudoSets = {}
        self.getSets(A, rowDic, colDic, sudoSets)
        self.tryFixSudo(0, 0, A, rowDic, colDic, sudoSets)


s = Solution()
A = ["53..7....", "6..195...", ".98....6.", "8...6...3", 
    "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
B = [[x for x in A[y]] for y in range(9)]
print("Solving for :-",B)
s.solveSudoku(B)
for row in B:
    print(row)
