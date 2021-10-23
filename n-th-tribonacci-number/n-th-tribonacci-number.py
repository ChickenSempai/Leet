class Solution:
    
    cell = {0:0, 1:1, 2:1}
    
    def tribonacci(self, n: int) -> int:
        if n in self.cell:
            return self.cell[n]
        self.cell[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.cell[n]
    
        