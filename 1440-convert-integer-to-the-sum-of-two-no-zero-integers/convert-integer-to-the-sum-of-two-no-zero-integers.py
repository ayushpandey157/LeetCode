class Solution:
    def noZero(self, x: int) -> bool:
        while x > 0:
            if x % 10 == 0:
                return False
            x //= 10
        return True
    def getNoZeroIntegers(self, n: int) -> list[int]:
        for a in range(1, n):
            b = n - a
            if self.noZero(a) and self.noZero(b):
                return [a, b]
        return []
        