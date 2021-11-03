class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ballGrid = [[-1 for j in range(len(grid[0]))] for i in range(len(grid)+1)]
        for i in range(len(grid[0])):
            ballGrid[0][i] = i
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if ballGrid[i][j] != -1:
                    if grid[i][j] >= 0:
                        znak = 1
                    else:
                        znak = -1
                    if j+znak >= 0 and j + znak < len(grid[0]) and grid[i][j] == grid[i][j + znak]:
                        ballGrid[i+1][j+znak] = ballGrid[i][j]
                    ballGrid[i][j] = -1
        answer = [-1 for i in range(len(grid[0]))]
        for i in range(len(grid[0])):
            if ballGrid[len(ballGrid) - 1][i] != -1:
                answer[ballGrid[len(ballGrid) - 1][i]] = i
        return answer