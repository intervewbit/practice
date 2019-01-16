class Solution:
    def comb(self,remainingSum,currSol,setToUse, resCombinations,idx):
        if remainingSum == 0:            
            resCombinations.append(currSol[:])
            return True
        if remainingSum < 0:
            return True

        # try add min from set
        """ minimum = setToUse[0]
        currSol.append(minimum)
        remainingSum -= minimum
        ret = self.comb(remainingSum,currSol,setToUse,resCombinations)
        currSol.pop()
        remainingSum += minimum
        if ret:            
            if len(setToUse)<=1 or remainingSum<setToUse[1]: return True

        setToUse = setToUse[1:]
        self.comb(remainingSum,currSol,setToUse,resCombinations)
        return False """
        while idx<len(setToUse) and remainingSum>=setToUse[idx]:
            remainingSum -= setToUse[idx]
            currSol.append(setToUse[idx])
            self.comb(remainingSum,currSol,setToUse,resCombinations,idx)
            remainingSum += setToUse[idx]
            currSol.pop()
            idx += 1

    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):        
        setToUse = sorted(list(set(A)))
        reqSum = B
        resCombinations = []
        currSol = []
        self.comb(reqSum,currSol,setToUse,resCombinations,0)
        return resCombinations

s = Solution()
A = [ 1,1,2,3,5,6,4,8,7 ]
r = s.combinationSum(A,6)
print(r)