def toInt(cells):
    d = 0
    for cell in cells:
        d = d | cell
        d = d << 1
    d = d >> 1
    return d

def toArr(d):
    cell = []
    while d != 0:
        cell.append(d % 2)
        d = d >> 1
    while len(cell) != 8:
        cell.append(0)
    return reversed(cell)

class Solution:
    def permutate(self):
        resCells = []
        for i in range(len(self.cells)):
            if i == 0:
                resCells.append(0)
            elif i == len(self.cells) - 1:
                resCells.append(0)

            elif self.cells[i-1] == self.cells[i + 1]:
                resCells.append(1)
            else: resCells.append(0)
        self.cells = resCells

    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        self.cells = cells
        visited = {}
        loop = []
        toIter = n
        
        while (visited.get(toInt(self.cells)) is None and toIter != 0):
            state = toInt(self.cells)
            visited[state] = True
            loop.append(state)
            self.permutate()
            toIter -= 1
        if (toIter == 0):
            return self.cells
        startInd = 0
        startState = toInt(self.cells)
        while loop[startInd] != startState:
            startInd += 1
        n = (toIter % (len(loop) - startInd)) + startInd
        # return [startInd, startState, n]
        # return loop
        return toArr(loop[n])
        