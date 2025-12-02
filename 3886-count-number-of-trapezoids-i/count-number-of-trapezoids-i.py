class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = (10 ** 9) + 7
        res = 0
        d = Counter(y for _,y in points)
        y_points = tuple(v * (v-1) // 2 for v in d.values())
        s = sum(y_points)
        for y in y_points:
            s -= y
            res += y * s
        return res % MOD