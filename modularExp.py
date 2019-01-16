class Solution:
    def modDriver(self,A,B,C):
        if B == 0:
            return 1
        if B%2==0:
            k = self.modDriver(A,B//2,C)
            return (k*k)%C
        else:
            k1 = self.modDriver(A,B-1,C)
            k2 = A%C
            return (k1*k2)%C


    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def Mod(self, A, B, C):
        if A <= 1:
            return 1
        
        return self.modDriver(A,B,C)
        