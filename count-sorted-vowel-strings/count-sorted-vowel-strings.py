class Solution:
    
    cell = {(0,0):1, (0,1):1,(0,2):1, (0,3):1, (0,4):1}
    
    def vowel(self,n:int, c):
        if (n,c) in self.cell:
            return self.cell[(n,c)]
        res = 0
        for clow in reversed(range(0, c+1)):
            res = res + self.vowel(n-1, clow)
        self.cell[(n,c)] = res
        return self.cell[(n,c)]
    
    def countVowelStrings(self, n: int) -> int:
        res = 0
        res = res + self.vowel(n-1, 4)
        res = res + self.vowel(n-1, 3)
        res = res + self.vowel(n-1, 2)
        res = res + self.vowel(n-1, 1)
        res = res + self.vowel(n-1, 0)
        return res
    
    