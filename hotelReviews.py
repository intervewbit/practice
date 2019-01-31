class Solution:
    def creGoodWordSet(self,S=str()):
        goodWords = S.split('_')
        return set(goodWords)
    
    def getGoodness(self,goodWords,S=str()):
        words = S.split('_')
        goodness = 0
        for word in words:
            if word in goodWords:
                goodness+=1
        return goodness

    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        goodWords = self.creGoodWordSet(A)
        resDic = {}
        for i,s in enumerate(B):
            goodness = self.getGoodness(goodWords,s)
            L = resDic.get(goodness,list())
            L.append(i)
            resDic[goodness] = L
        
        result = []
        order = list(sorted(resDic.keys()))
        for goodness in reversed(order):
            result.extend(resDic[goodness])
        
        return result

A = "cool_ice_wifi"
B = ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]
R = Solution().solve(A,B)
print(R)