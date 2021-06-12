class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])
		
        zerol = False
        zeroc = False
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        zerol = True
                    if col == 0:
                        zeroc = True
                    matrix[row][0] = matrix[0][col] = 0
                    
        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]
        

        if zerol:
            for col in range(n):
                matrix[0][col] = 0
        
        if zeroc:
            for row in range(m):
                matrix[row][0] = 0
        