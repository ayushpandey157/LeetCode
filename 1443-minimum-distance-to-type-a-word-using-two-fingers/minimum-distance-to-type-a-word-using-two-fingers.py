from typing import List

_D = tuple(
    tuple(abs(a // 6 - b // 6) + abs(a % 6 - b % 6) for b in range(26))
    for a in range(26)
)

class Solution:
    def minimumDistance(self, word: str) -> int:
        w = [ord(c) - 65 for c in word]
        INF = float('inf')
        dp = [INF] * 27
        dp[26] = 0  

        for i in range(1, len(w)):
            cur, prev = w[i], w[i-1]
            d_pc   = _D[prev][cur]   
            D_cur  = _D[cur]        
            ndp    = [INF] * 27
            best_prev = INF

            for other in range(27):
                cost = dp[other]
                if cost == INF: continue
                c1 = cost + d_pc
                if c1 < ndp[other]: ndp[other] = c1
                c2 = cost + (D_cur[other] if other < 26 else 0)
                if c2 < best_prev: best_prev = c2

            if best_prev < ndp[prev]: ndp[prev] = best_prev
            dp = ndp

        return min(dp)