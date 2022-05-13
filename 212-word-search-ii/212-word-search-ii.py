class Solution:
    visited = set()
    res = set()
    
    def buildtrie(self, word, i, trie):
        if i == len(word):
            trie['word'] = word
            return
        if word[i] not in trie:
            trie[word[i]] = {}
        self.buildtrie(word, i+1, trie[word[i]])
            
    
    def dfs(self, board, i , j, trie):
        s = set()
        if 'word' in trie:
            s.add(trie['word'])
            trie.pop('word')
        if (i,j) in self.visited:
            return s
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return s
        if board[i][j] not in trie:
            return s
        self.visited.add((i,j))
        s = s.union(self.dfs(board, i+1, j, trie[board[i][j]]))
        s = s.union(self.dfs(board, i, j+1, trie[board[i][j]]))
        s = s.union(self.dfs(board, i-1, j, trie[board[i][j]]))
        s = s.union(self.dfs(board, i, j-1, trie[board[i][j]]))
        if len(trie[board[i][j]]) == 0:
            trie.pop(board[i][j])
        self.visited.remove((i,j))
        return s
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            self.buildtrie(word, 0, trie)
        s = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                s = s.union(self.dfs(board, i, j, trie))
        return s