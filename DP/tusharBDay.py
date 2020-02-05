class Solution:
    def getResistance(self,friends,idxList):
        resistance = 0
        for i in idxList:
            resistance = resistance + friends[i]
        return resistance
    
    def getMaxKicks(self, bestList, resistance, friends, prunedIndexes):
        currResistance = self.getResistance(friends, bestList)
        for i in range(len(bestList)):
            for j in range(len(prunedIndexes)-1,-1,-1):                
                jIdx = prunedIndexes[j]
                deltaIncrease = friends[jIdx] - friends[bestList[i]]
                if deltaIncrease + currResistance > resistance:
                    break
                bestList[i] = jIdx
                currResistance = currResistance + deltaIncrease
        return bestList


    def pruneFriends(self, minIndex, friends, maxPossible, resistance):
        largest = friends[minIndex] - 1
        minVal = friends[minIndex]
        prunedIndexes = []
        for i in range(minIndex,-1,-1):
            if friends[i]>resistance:
                continue
            if friends[i]<largest:
                j = 0
                while prunedIndexes and friends[prunedIndexes[j]] > friends[i]:
                    j = j + 1
                prunedIndexes = prunedIndexes[j:]
                prunedIndexes.insert(0,i)
                largest = friends[i]
            prunedIndexes.insert(0,i)
            largest = friends[i]
        return prunedIndexes

    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        minStrength = min(B)
        minIndex = B.index(minStrength)
        maxPossible = A // minStrength
        prunedIndexes = self.pruneFriends(minIndex,B, maxPossible, A)        
        bestList = [minIndex] * maxPossible
        return self.getMaxKicks(bestList,A,B,prunedIndexes)


A = Solution()
ll = A.solve(7457, [ 2756, 16180, 11785, 10278, 227, 13710, 21712, 14662, 9942, 916, 3968, 6737, 12815, 15806, 23729, 22093, 21317, 15343, 17707, 11000, 1385, 23907, 2724, 1061, 180, 18198, 21568, 2515, 4019, 9025, 3233, 23118, 16548, 15009, 8387, 8118, 20062, 5090, 14123, 21347, 5998, 9435, 3076, 10156, 232, 1796, 7240, 21541, 17131, 16290, 23884, 9859, 15188, 1599, 2263, 15359, 11140, 23822, 17866, 6503, 24190, 21090, 4612, 15729, 2442 ])
print(*ll)
