class Solution:
    def maxArea(self,mat,R,C): 
        hist = [[0 for i in range(C + 1)]  
                for i in range(R + 1)] 
    
        for i in range(0, C, 1): 
            
            hist[0][i] = mat[0][i] 
    
            for j in range(1, R, 1): 
                if ((mat[j][i] == 0)): 
                    hist[j][i] = 0
                else: 
                    hist[j][i] = hist[j - 1][i] + 1
    
        for i in range(0, R, 1): 
            count = [0 for i in range(R + 1)] 
    
            for j in range(0, C, 1): 
                count[hist[i][j]] += 1
    
            col_no = 0
            j = R 
            while(j >= 0): 
                if (count[j] > 0): 
                    for k in range(0, count[j], 1): 
                        hist[i][col_no] = j 
                        col_no += 1
    
                j -= 1
                
        max_area = 0
        for i in range(0, R, 1): 
            for j in range(0, C, 1): 
                curr_area = (j + 1) * hist[i][j] 
                if (curr_area > max_area): 
                    max_area = curr_area 
    
        return max_area 

    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        if not A:
            return 0
        if not A[0]:
            return 0
        R = len(A)
        C = len(A[0])
        return self.maxArea(A,R,C)

A = [
    [1,0,1],
    [0,1,1],
    [1,0,1]
]

print(Solution().solve(A))
        
