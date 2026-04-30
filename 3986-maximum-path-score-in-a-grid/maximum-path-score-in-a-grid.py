class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        # dp[i][j] = dict{cost:max_score}
        def get_cost(val):
            return 0 if val == 0 else 1
        def get_score(val):
            return val
        dp = [[dict() for _ in range(n)] for _ in range(m)]
        start_cost = get_cost(grid[0][0])
        if start_cost > k:
            return -1
        dp[0][0][start_cost] = get_score(grid[0][0])
        for i in range(m):
            for j in range(n):
                for cost, score in list(dp[i][j].items()):
                    for di, dj in [(0,1),(1,0)]:
                        ni, nj = i+di, j + dj
                        if ni <m and nj <n :
                            val = grid[ni][nj]
                            new_cost = cost + get_cost(val)
                            if new_cost <= k:
                                new_score = score + get_score(val)
                                if new_cost not in dp[ni][nj] or dp[ni][nj][new_cost] < new_score:
                                    dp[ni][nj][new_cost] = new_score
        if not dp[m-1][n-1]:
            return -1
        return max(dp[m-1][n-1].values())
        