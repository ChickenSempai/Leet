class Solution:
    def integerReplacement(self, n):
        if n < 1: return 2147483647
        if n == 1: return 0
        minact = 2147483647
        if n % 2 == 0: 
            minact = min(minact, self.integerReplacement(n / 2))
        else :
            minact = min(minact, self.integerReplacement(n - 1) )
            minact = min(minact, self.integerReplacement(n + 1) )
        return minact + 1