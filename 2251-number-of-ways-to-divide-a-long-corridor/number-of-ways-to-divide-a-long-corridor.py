class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7

        n = corridor.count('S')
        if not n or n & 1:
            return 0
        if n == 2:
            return 1

        res = 1
        c = 0
        gap = 0 

        for ch in corridor:
            if ch == 'S':
                c += 1
                if c == 2:
                    if gap > 0:
                        res = (res * (gap + 1)) % MOD
                    gap = 0
                elif c == 3:
                    c = 1
            else:
                if c == 2:
                    gap += 1

        return res