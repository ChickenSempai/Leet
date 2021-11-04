class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                if not grid[i][j] == 1 :
                    grid[i][j] = 10000
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                if not grid[i][j] == 1 :
                    if j > 0: grid[i][j] = min(grid[i][j-1]+1,grid[i][j])
                    if i > 0: grid[i][j] = min(grid[i][j],grid[i-1][j]+1)
        
        finalMax = 0
        for i in reversed(range(0, len(grid))):
            for j in reversed(range(0, len(grid))):
                if not grid[i][j] == 1 :
                    if j < len(grid)-1: grid[i][j] = min(grid[i][j+1]+1,grid[i][j])
                    if i < len(grid)-1: grid[i][j] = min(grid[i][j],grid[i+1][j]+1)
                    finalMax = max(finalMax, grid[i][j])
        if finalMax == 10000:
            return -1
        return finalMax - 1