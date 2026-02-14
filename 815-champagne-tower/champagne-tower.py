class Solution:
    def champagneTower(self, poured: int, r: int, c: int) -> float:
        dp = [[0] * (r+1) for _ in range(r+1)]
        dp[0][0] = poured
        
        for i in range(r):
            for j in range(i+1):
                if dp[i][j] > 1:
                    rem = (dp[i][j]-1.)/2.
                    dp[i+1][j] += rem
                    dp[i+1][j+1] += rem
        
        return min(dp[r][c], 1) 