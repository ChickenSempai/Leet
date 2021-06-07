class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n+1 for x in range(n+1)]
        dp[n] = 0
        for i in range(n, 0, -1):
            k = 1
            while k*k  <= i:
                dp[i - k*k] = min(dp[i - k*k], dp[i] + 1)
                k += 1
        return dp[0]
        