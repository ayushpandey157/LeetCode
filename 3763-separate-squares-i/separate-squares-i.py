class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        minY = 0.0
        totalArea = 0.0
        maxY = 0.0
        for x, y, l in squares:
            top = float(y) + float(l)
            if top > maxY:
                maxY = top
            totalArea += float(l) * float(l)
        while maxY - minY > 1e-5:
            m = (minY + maxY) / 2.0
            below = 0.0
            for x, y, l in squares:
                if float(y) < m:
                    cut = m - float(y)
                    h = cut if cut < float(l) else float(l)
                    below += float(l) * h
            above = totalArea - below
            if above - below > 0.0:
                minY = m
            else:
                maxY = m
        return minY