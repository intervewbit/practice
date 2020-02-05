class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        if not A:
            return 0
        dec = [1 for x in A]        
        dec.append(0)
        for i,v in enumerate(A):
            if v <= '0' or v>'9':
                if v == '0' and i>0 and int(A[i-1]) <= 2:
                    dec[i+1] = dec[i]
                    continue
                return 0

            curr = dec[i]
            if i>0 and int(A[i-1])<=2 and int(A[i-1])>0 and int(A[i])<7:
                curr += dec[i-1]
            dec[i+1] = curr
        return dec[len(A)]


A = "1234120"
print(Solution().numDecodings(A))