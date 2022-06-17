class Solution:
    def numTrees(self, n: int) -> int:
        s = {}
        def rec(n):
            if n in s:
                return s[n]
            if n == 0:
                return 1
            sum = 0
            for i in range(n):
                sum += rec(n-1-i) * rec(i)
            sum = max(sum, 1)
            s[n] = sum
            return sum
        return rec(n) 