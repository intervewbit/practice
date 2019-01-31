class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
    def dNums(self, A, B):
        dic = {}
        for idx in range(B):
            if idx >= len(A):
                break
            dic[A[idx]] = dic.get(A[idx],0) + 1
        
        idx = 0
        result = []
        while idx < len(A) - B + 1:
            result.append(len(dic))
            dic[A[idx]] = dic[A[idx]] - 1
            if dic[A[idx]] == 0:
                dic.pop(A[idx])
            idx += 1
            nIdx = idx + B - 1
            if  nIdx < len(A):
                dic[A[nIdx]] = dic.get(A[nIdx],0) + 1
        
        return result

A = [1,2,2,3,4,5,6,6,6]
B = 3
R = Solution().dNums(A,B)
print(R)