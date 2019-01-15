class Solution:
    def isPalindrome(self,A,start,end):
        while start < end:
            if A[start] != A[end]:
                return False
            start += 1
            end -= 1
        return True
    def partitionAt(self,A,idx,curr,result):
        if idx >= len(A):
            result.append(curr[:])
            return
        # starting at idx try to find palidromes of increasing len
        for termIdx in range(idx,len(A)):
            if self.isPalindrome(A,idx,termIdx):
                curr.append(A[idx:termIdx+1])
                self.partitionAt(A,termIdx+1,curr,result)
                curr.pop()
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        result = []
        curr = []
        self.partitionAt(A,0,curr,result)
        return result

s = Solution()
A = "aabaa"
r = s.partition(A)
print(r)