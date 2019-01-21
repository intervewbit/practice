class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def fractionToDecimal(self, A, B):       
        if A == 0:
            return "0" 
        result = "" if A*B>0 else "-"
        A = abs(A)
        B = abs(B)
        full = A//B
        remaining = A%B
        result += str(full) 
        idxDic = {}
        frac = "." if remaining>0 else ""
        isRep = False
        idxStart = -1
        
        while remaining>0:
            remaining *= 10
            if remaining in idxDic:
                isRep = True
                idxStart = idxDic[remaining]            
                break
            idxDic[remaining] = len(frac)
            d = remaining//B            
            frac += str(d)
            remaining = remaining%B
        if isRep:
            toRep = frac[idxStart:]
            frac = frac[0:idxStart] + "(" + toRep + ")"
        result += frac
        return result

s = Solution()
A = 1
B = -2
r = s.fractionToDecimal(A,B)
print(r)

