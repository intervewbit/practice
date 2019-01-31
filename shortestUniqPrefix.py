class Solution:
    def pushFurther(self, currChr, currPrefix, mainDic={}):
        nextDicToUse = None
        if currChr in mainDic:
            if mainDic[currChr][0]:
                old = mainDic[currChr][1]
                chrKey = old[len(currPrefix):len(currPrefix)+1]
                newDic = {}
                newDic[chrKey] = True, old
                mainDic[currChr] = False, newDic
                nextDicToUse = newDic
            else:
                nextDicToUse = mainDic[currChr][1]
        return nextDicToUse

    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        mainDic = {}
        for s in A:
            currDic = mainDic
            currPrefix = ""
            for ch in s:
                currPrefix += ch
                nextDic = self.pushFurther(ch, currPrefix, currDic)
                if not nextDic:
                    currDic[ch] = True, s
                    break
                currDic = nextDic

        result = []
        for s in A:
            currPrefix = ""
            currDic = mainDic
            for ch in s:
                currPrefix += ch
                assert ch in currDic
                if currDic[ch][0]:
                    result.append(currPrefix)
                    break
                else:
                    currDic = currDic[ch][1]
        return result


A = ["dog", "dock","zeebra","donkey","deer"]
R = Solution().prefix(A)
print(R)
