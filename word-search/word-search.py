class Solution:

    def exist(self, board: List[List[str]], word: str):
        visited = {}           
        
        for i in range(len(board)):
            for j in range(len(board[0])):

                if self.dfs(board, word, i, j,visited ):
                    return True;
                    
        return False;
        
    
    moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def dfs(self, board: List[List[str]], word: str, i,j , visited, wordIndex = 0):
        
        if wordIndex == len(word):
            return True
        
        
        
        
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited.get((i, j)) or word[wordIndex] != board[i][j]:
            return False
        
        visited[(i,j)] = True;
        
        for x,y in self.moves:
            if self.dfs(board, word, i + x, j + y, visited, wordIndex + 1) == True:
                return True
        visited[(i,j)] = False;        
        return False;
    
