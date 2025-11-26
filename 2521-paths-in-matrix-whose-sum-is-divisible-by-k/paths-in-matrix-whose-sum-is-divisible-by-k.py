class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * k for _ in range(len(grid[0]))]
        dp[0][grid[0][0] % k] = 1
        for i in range(1, len(grid[0])):
            tmp = [0] * k
            for idx, j in enumerate(dp[i - 1]):
                tmp[(idx + grid[0][i]) % k] += j
                tmp[(idx + grid[0][i]) % k] %= MOD
            dp[i] = tmp

        for cnt in range(1, len(grid)):
            tmp1 = [[0] * k for _ in range(len(grid[0]))]
            for i in range(len(grid[0])):
                tmp = [0] * k
                for idx, j in enumerate(dp[i]):
                    tmp[(idx + grid[cnt][i]) % k] += j
                    tmp[(idx + grid[cnt][i]) % k] %= MOD
                if i > 0:
                    for idx, j in enumerate(tmp1[i - 1]):
                        tmp[(idx + grid[cnt][i]) % k] += j
                        tmp[(idx + grid[cnt][i]) % k] %= MOD
                tmp1[i] = tmp
            dp = tmp1
        return dp[-1][0] % MOD


