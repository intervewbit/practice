class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        charIdxMap = {}
        maxLen = 0
        currStart = 0

        for i,ch in enumerate(A):
            prevIdx = charIdxMap.get(ch,-1)
            charIdxMap[ch] = i
            if prevIdx<currStart:                
                currLen = i - currStart + 1
                if currLen>maxLen:
                    maxLen = currLen
            else:
                currStart = prevIdx + 1
        return maxLen

A = "aabcadeb"
R = Solution().lengthOfLongestSubstring(A)
print(R)
