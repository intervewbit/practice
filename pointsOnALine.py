class Solution:
    def gcd(self, y, x):
        if x > y:
            x, y = y, x
        while x > 0:
            y, x = x, y % x
        return y

    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        maxCount = 1 if len(A) == 1 else 0
        points = list(zip(A, B))
        slopes = {}
        same = {}
        maxSame = 0
        perpCount = {}
        perpCountMax = 0
        for i, pt1 in enumerate(points):
            sameCount = same.get(pt1,0)
            sameCount += 1
            same[pt1] = sameCount
            if maxSame < sameCount:
                maxSame = sameCount
            if sameCount>1:continue
            for j in range(i+1, len(points)):
                pt2 = (points[j][0],points[j][1])
                yDiff = points[j][1] - pt1[1]
                xDiff = points[j][0] - pt1[0]
                if xDiff == 0:
                    pSet = perpCount.get(pt1[0],set())
                    if pt1 not in pSet:
                        pSet.add(pt1)                                            
                    if pt2 not in pSet:
                        pSet.add(pt2)
                    c = len(pSet)
                    if c>perpCountMax:
                        perpCountMax = c
                    perpCount[pt1[0]] = pSet
                else:
                    slope = (0, 0)
                    if yDiff != 0:
                        g = self.gcd(yDiff, xDiff)
                        slope = (yDiff/g, xDiff/g)
                    slopeSet = slopes.get(slope, set())
                    if pt1 not in slopeSet:
                        slopeSet.add(pt1)
                    if pt2 not in slopeSet:
                        slopeSet.add(pt2)
                    slopeCount = len(slopeSet)
                    slopes[slope] = slopeSet
                    if maxCount < slopeCount:
                        maxCount = slopeCount
        return max((maxCount,maxSame,perpCountMax))


A = [-6 ,-17 ,5 ,-16 ,-18 ,-17]
B = [2 ,-4 ,5 ,-13 ,-2 ,20]
#A = [1,1,1,1,1]
#B = [1,1,1,1,1]
r = Solution().maxPoints(A, B)
print(r)
