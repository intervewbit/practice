class Solution:
    def isAttacked(self, usedColumns, row, col):
        if col in usedColumns:
            return True
        for c, r in usedColumns.items():
            # shouldnt happen but just to be safe
            if r == row:
                return True
            rDiff = abs(r-row)
            cDiff = abs(c-col)
            if rDiff == cDiff:
                return True
        return False

    def getPlacement(self, row, col, A, usedColumns):
        placement = ""
        if not self.isAttacked(usedColumns, row, col):
            for idx in range(A):
                if idx == col:
                    placement += "Q"
                else:
                    placement += "."
        return placement

    def placeQueen(self, A, row, result, curr, usedColumns={}):
        if row == A:
            result.append(curr[:])
            return
        # try placing it in all columns
        for col in range(A):
            if col not in usedColumns:                
                placement = self.getPlacement(row, col, A, usedColumns)
                if not placement:
                    continue
                usedColumns[col] = row
                curr.append(placement)
                self.placeQueen(A, row+1, result, curr, usedColumns)
                curr.pop()
                usedColumns.pop(col)

    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        result = []
        curr = []
        self.placeQueen(A, 0, result, curr)
        return result


s = Solution()
A = 2
r = s.solveNQueens(A)
print(r)
