class Solution:
    def __init__(self):
        self.mapping = {
            '0': ['0'],
            '1': ['1'],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

    def getCombination(self,A,idx,sols,curr):
        if idx == len(A):
            sols.append(curr)
            return
        
        # get the mapping for current digit
        currList = self.mapping[A[idx]]
        for c in currList:
            curr = curr + c
            self.getCombination(A,idx+1,sols,curr)
            curr = curr[:len(curr)-1]


    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        result = []
        self.getCombination(A,0,result,"")
        return result

S = Solution()
A = "23"
R = S.letterCombinations(A)
print(R)