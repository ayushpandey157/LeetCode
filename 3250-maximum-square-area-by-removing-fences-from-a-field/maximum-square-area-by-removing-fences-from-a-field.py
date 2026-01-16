class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def diff(f): return {y-x for x,y in combinations(sorted(f), 2)}
        return max(diff([1,n]+vFences) & diff([1,m]+hFences) | {0})**2 % int(1e9+7) or -1
        