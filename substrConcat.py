class Solution:
    def isMatch(self, startIdx, A, freqDic, wordLen):
        while True:
            currStr = A[startIdx:startIdx+wordLen]
            if currStr in freqDic:
                freqDic[currStr] = freqDic[currStr] - 1
                if freqDic[currStr] == 0:
                    freqDic.pop(currStr)
                if len(freqDic) == 0:
                    break
                startIdx += wordLen
            else:
                return False
        return True

    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        result = []
        freqDic = {}
        totalWords = len(B)
        wordLen = 0
        if B:
            wordLen = len(B[0])
        if wordLen == 0:
            return list(range(len(A)))

        for word in B:
            freqDic[word] = freqDic.get(word, 0) + 1

        for idx in range(len(A) - totalWords*wordLen + 1):
            dirtyDic = {k: v for k, v in freqDic.items()}
            if self.isMatch(idx, A, dirtyDic, wordLen):
                result.append(idx)
            idx += 1

        return result


A = "1"
B = ("2", "1")
R = Solution().findSubstring(A, B)
print(R)
