class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def minWindow(self, A, B):
        if len(B) > len(A) or len(B) == 0 or len(A) == 0:
            return ""
        goldReq = {}
        for ch in B:
            goldReq[ch] = goldReq.get(ch, 0) + 1
        start = 0
        end = 0
        currMinLen = len(A) + 1
        minStart,minEnd = 0,-1
        req = {k:v for k,v in goldReq.items()}
        surplus = {}
        while start <= len(A) - len(B) and end<len(A):
            if A[start] not in goldReq:
                start += 1
                continue
            if end < start:
                end = start
            
            while end<len(A):
                ch = A[end]
                if ch in req:
                    req[ch] = req[ch] - 1
                    if req[ch] == 0:
                        req.pop(ch)
                    if len(req) == 0:
                        currLen = end - start + 1
                        if currLen<currMinLen:
                            minStart,minEnd = start,end
                            currMinLen = currLen
                            if currMinLen == 1:
                                return A[start:end+1]
                        end += 1
                        break                        
                elif ch in goldReq:
                    surplus[ch] = surplus.get(ch,0)+1
                end += 1
            
            if len(req)>0:
                break

            # skip start until we invalidate the current
            while A[start] not in goldReq or A[start] in surplus:
                if A[start] in surplus:
                    surplus[A[start]] = surplus[A[start]] - 1
                    if surplus[A[start]] == 0:
                        surplus.pop(A[start])
                start += 1
                if start>=len(A):break
            else:
                req[A[start]] = 1
                currLen = end - start + 1
                if currLen<currMinLen:
                    currMinLen = currLen
                    minStart,minEnd = start,end-1
                start += 1

        return A[minStart:minEnd+1]

A = "ADOBECODEBANC"
B = "ABC"
R = Solution().minWindow(A,B)
print(R)


