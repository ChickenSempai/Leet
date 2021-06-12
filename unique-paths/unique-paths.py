class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def ways(posm, posn) -> int:
            if (posm, posn) in memo:
                return memo[(posm, posn)]
        
            if posm == m and posn == n:
                return 1
            if posm > m or posn > n:
                return 0
            memo[(posm, posn)] = ways(posm+1, posn) + ways(posm, posn+1)
            return memo[(posm, posn)]
        
        return ways(1,1)